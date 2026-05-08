---
name: document-graph-pipeline
description: >
  Excel/PDF → Table Transformer → Document AST → Neo4j / GraphRAG パイプラインを構築するスキル。
  ドキュメントからテーブルを抽出し、AST化してNeo4jに取り込み、GraphRAGクエリを可能にする。
  Use when: the user wants to parse Excel/PDF documents into a graph database for RAG.
---

# Document Graph Pipeline Skill

## 概要

```
Excel / PDF
    ↓  [Step 1] 入力パーサー
Table Transformer
    ↓  [Step 2] テーブル抽出・構造化
Document AST
    ↓  [Step 3] グラフモデル変換
Neo4j / GraphRAG
    ↓  [Step 4] クエリ・RAG
```

## Workflow

TodoWriteで全タスクをリストアップしてから着手する。

---

### Step 0: 環境調査

既存のファイルと設定を確認する。

```bash
# 入力ファイルの確認
ls -la *.xlsx *.pdf 2>/dev/null || find . -name "*.xlsx" -o -name "*.pdf" | head -20

# Neo4j接続情報の確認
echo "NEO4J_URI=${NEO4J_URI:-bolt://localhost:7687}"
echo "NEO4J_USER=${NEO4J_USER:-neo4j}"
echo "NEO4J_PASSWORD=${NEO4J_PASSWORD:-(未設定)}"

# Python環境
python3 --version && pip list 2>/dev/null | grep -E "neo4j|transformers|pdfplumber|openpyxl|pandas|sentence"
```

不足しているものを把握してから次へ進む。

---

### Step 1: 依存ライブラリのインストール

```bash
pip install \
  pdfplumber \
  pymupdf \
  openpyxl \
  pandas \
  pillow \
  transformers \
  timm \
  torch \
  torchvision \
  neo4j \
  sentence-transformers \
  anthropic
```

**ライブラリ選定の理由:**
- `pdfplumber` — テキストベースPDFからテーブルを直接抽出
- `pymupdf (fitz)` — PDF→画像変換（Table Transformer用）
- `transformers` + `timm` — microsoft/table-transformer-detection モデル
- `openpyxl` / `pandas` — Excelパース
- `neo4j` — Neo4j Python ドライバ
- `sentence-transformers` — ベクトル埋め込み（GraphRAG用）

---

### Step 2: ディレクトリ構成の作成

```
pipeline/
├── __init__.py
├── parsers/
│   ├── __init__.py
│   ├── excel_parser.py      # Excel → raw tables
│   └── pdf_parser.py        # PDF → raw tables (pdfplumber + Table Transformer)
├── ast_builder.py           # raw tables → Document AST
├── neo4j_ingester.py        # Document AST → Neo4j
├── graphrag.py              # Neo4j + embedding → RAG query
├── models.py                # AST dataclass定義
└── main.py                  # エントリーポイント
```

```bash
mkdir -p pipeline/parsers
touch pipeline/__init__.py pipeline/parsers/__init__.py
```

---

### Step 3: データモデル (`models.py`)

Document ASTのノード型を定義する。

```python
# pipeline/models.py
from dataclasses import dataclass, field
from typing import List, Optional, Any
from enum import Enum
import uuid


class NodeType(str, Enum):
    DOCUMENT = "Document"
    SECTION = "Section"
    TABLE = "Table"
    ROW = "Row"
    CELL = "Cell"
    HEADER = "Header"


@dataclass
class ASTNode:
    node_type: NodeType
    node_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    children: List["ASTNode"] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    embedding: Optional[List[float]] = None

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "node_type": self.node_type.value,
            "content": self.content,
            "metadata": self.metadata,
        }
```

**グラフ関係の設計:**
```
(Document)-[:CONTAINS]->(Section)
(Section)-[:CONTAINS]->(Table)
(Table)-[:HAS_HEADER]->(Header)
(Table)-[:CONTAINS]->(Row)
(Row)-[:CONTAINS]->(Cell)
(Row)-[:NEXT]->(Row)         # 行間の順序
(Cell)-[:SAME_COLUMN]->(Cell) # 列方向の参照
```

---

### Step 4: Excelパーサー (`parsers/excel_parser.py`)

```python
# pipeline/parsers/excel_parser.py
import openpyxl
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any


def parse_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Excelファイルの全シートからテーブルを抽出する。
    Returns: [{"sheet_name": str, "headers": [...], "rows": [[...], ...]}, ...]
    """
    path = Path(file_path)
    result = []

    wb = openpyxl.load_workbook(path, data_only=True)
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        df = pd.DataFrame(ws.values)

        if df.empty:
            continue

        # 最初の非空行をヘッダーとして検出
        header_row_idx = _find_header_row(df)
        if header_row_idx is None:
            continue

        headers = [str(c) if c is not None else "" for c in df.iloc[header_row_idx]]
        rows = []
        for _, row in df.iloc[header_row_idx + 1:].iterrows():
            row_data = [str(v) if v is not None else "" for v in row]
            if any(v.strip() for v in row_data):  # 空行スキップ
                rows.append(row_data)

        result.append({
            "source": str(path),
            "sheet_name": sheet_name,
            "headers": headers,
            "rows": rows,
        })

    return result


def _find_header_row(df: pd.DataFrame) -> int | None:
    for i, row in df.iterrows():
        non_null = [v for v in row if v is not None and str(v).strip()]
        if len(non_null) >= 2:
            return i
    return None
```

---

### Step 5: PDFパーサー (`parsers/pdf_parser.py`)

2段階戦略: pdfplumber（テキストPDF）→ 失敗時に Table Transformer（画像PDF）

```python
# pipeline/parsers/pdf_parser.py
import pdfplumber
import fitz  # pymupdf
from pathlib import Path
from typing import List, Dict, Any
from PIL import Image
import io


def parse_pdf(file_path: str, use_table_transformer: bool = False) -> List[Dict[str, Any]]:
    """
    PDFからテーブルを抽出する。
    use_table_transformer=True でOCR/画像ベースPDFに対応。
    """
    path = Path(file_path)
    result = []

    with pdfplumber.open(path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            tables = page.extract_tables()
            if tables:
                for tbl_idx, table in enumerate(tables):
                    if not table or len(table) < 2:
                        continue
                    headers = [str(h) if h else "" for h in table[0]]
                    rows = [[str(c) if c else "" for c in row] for row in table[1:]]
                    result.append({
                        "source": str(path),
                        "page": page_num,
                        "table_index": tbl_idx,
                        "headers": headers,
                        "rows": rows,
                        "method": "pdfplumber",
                    })

    if not result and use_table_transformer:
        result = _extract_with_table_transformer(path)

    return result


def _extract_with_table_transformer(path: Path) -> List[Dict[str, Any]]:
    """
    Table Transformer (microsoft/table-transformer-detection) で
    画像ベースPDFからテーブルを検出・抽出する。
    """
    from transformers import AutoImageProcessor, TableTransformerForObjectDetection
    import torch

    detection_model_name = "microsoft/table-transformer-detection"
    structure_model_name = "microsoft/table-transformer-structure-recognition"

    det_processor = AutoImageProcessor.from_pretrained(detection_model_name)
    det_model = TableTransformerForObjectDetection.from_pretrained(detection_model_name)
    str_processor = AutoImageProcessor.from_pretrained(structure_model_name)
    str_model = TableTransformerForObjectDetection.from_pretrained(structure_model_name)

    doc = fitz.open(str(path))
    result = []

    for page_num, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")

        # テーブル領域の検出
        inputs = det_processor(images=img, return_tensors="pt")
        with torch.no_grad():
            outputs = det_model(**inputs)

        target_sizes = torch.tensor([img.size[::-1]])
        detections = det_processor.post_process_object_detection(
            outputs, threshold=0.9, target_sizes=target_sizes
        )[0]

        for box_idx, (score, label, box) in enumerate(
            zip(detections["scores"], detections["labels"], detections["boxes"])
        ):
            if label.item() == 0:  # 0 = table
                x0, y0, x1, y1 = [int(v) for v in box.tolist()]
                table_img = img.crop((x0, y0, x1, y1))
                table_data = _recognize_table_structure(
                    table_img, str_processor, str_model
                )
                if table_data:
                    result.append({
                        "source": str(path),
                        "page": page_num,
                        "table_index": box_idx,
                        "headers": table_data.get("headers", []),
                        "rows": table_data.get("rows", []),
                        "method": "table_transformer",
                        "bbox": [x0, y0, x1, y1],
                    })

    return result


def _recognize_table_structure(
    table_img: Image.Image, processor, model
) -> Dict[str, Any]:
    """Table Transformer で行・列構造を認識してセルテキストを返す（簡易版）。"""
    import torch

    inputs = processor(images=table_img, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)

    target_sizes = torch.tensor([table_img.size[::-1]])
    results = processor.post_process_object_detection(
        outputs, threshold=0.7, target_sizes=target_sizes
    )[0]

    # ラベル: 0=table, 1=table column, 2=table row, 3=table column header,
    #         4=table projected row header, 5=table spanning cell
    label_map = {v: k for k, v in model.config.label2id.items()}
    rows, headers = [], []

    for score, label, box in zip(
        results["scores"], results["labels"], results["boxes"]
    ):
        label_name = label_map.get(label.item(), "unknown")
        if label_name == "table row":
            rows.append(box.tolist())
        elif label_name == "table column header":
            headers.append(box.tolist())

    # NOTE: 実際のOCRにはpaddleocr/easyocrを組み合わせる
    # ここでは bbox情報のみ返す（拡張ポイント）
    return {
        "headers": [f"col_{i}" for i in range(len(headers))],
        "rows": [[] for _ in rows],
        "row_bboxes": rows,
        "header_bboxes": headers,
    }
```

---

### Step 6: Document AST ビルダー (`ast_builder.py`)

```python
# pipeline/ast_builder.py
from typing import List, Dict, Any
from pathlib import Path
from .models import ASTNode, NodeType


def build_ast(tables: List[Dict[str, Any]], source_name: str = "") -> ASTNode:
    """
    抽出されたテーブルリストからDocument ASTを構築する。
    """
    doc_node = ASTNode(
        node_type=NodeType.DOCUMENT,
        content=source_name,
        metadata={"source": source_name, "table_count": len(tables)},
    )

    # シートまたはページ単位でSectionを作成
    sections: Dict[str, ASTNode] = {}

    for table_data in tables:
        section_key = _get_section_key(table_data)
        if section_key not in sections:
            section = ASTNode(
                node_type=NodeType.SECTION,
                content=section_key,
                metadata=_extract_section_meta(table_data),
            )
            sections[section_key] = section
            doc_node.children.append(section)

        table_node = _build_table_node(table_data)
        sections[section_key].children.append(table_node)

    return doc_node


def _get_section_key(table_data: Dict[str, Any]) -> str:
    if "sheet_name" in table_data:
        return f"sheet:{table_data['sheet_name']}"
    return f"page:{table_data.get('page', 1)}"


def _extract_section_meta(table_data: Dict[str, Any]) -> dict:
    meta = {"source": table_data.get("source", "")}
    if "sheet_name" in table_data:
        meta["sheet_name"] = table_data["sheet_name"]
    if "page" in table_data:
        meta["page"] = table_data["page"]
    return meta


def _build_table_node(table_data: Dict[str, Any]) -> ASTNode:
    headers = table_data.get("headers", [])
    rows = table_data.get("rows", [])

    table_node = ASTNode(
        node_type=NodeType.TABLE,
        content=f"Table with {len(rows)} rows, {len(headers)} columns",
        metadata={
            "column_count": len(headers),
            "row_count": len(rows),
            "method": table_data.get("method", "unknown"),
            "source": table_data.get("source", ""),
        },
    )

    # ヘッダー行ノード
    if headers:
        header_node = ASTNode(
            node_type=NodeType.HEADER,
            content="\t".join(headers),
            metadata={"columns": headers},
        )
        for col_name in headers:
            header_node.children.append(
                ASTNode(node_type=NodeType.CELL, content=col_name,
                        metadata={"role": "header"})
            )
        table_node.children.append(header_node)

    # データ行ノード
    for row_idx, row_values in enumerate(rows):
        row_node = ASTNode(
            node_type=NodeType.ROW,
            content="\t".join(row_values),
            metadata={"row_index": row_idx},
        )
        for col_idx, cell_val in enumerate(row_values):
            col_name = headers[col_idx] if col_idx < len(headers) else f"col_{col_idx}"
            row_node.children.append(
                ASTNode(
                    node_type=NodeType.CELL,
                    content=cell_val,
                    metadata={"column": col_name, "col_index": col_idx, "row_index": row_idx},
                )
            )
        table_node.children.append(row_node)

    return table_node
```

---

### Step 7: Neo4j インジェスター (`neo4j_ingester.py`)

```python
# pipeline/neo4j_ingester.py
import os
from neo4j import GraphDatabase
from typing import Optional
from .models import ASTNode, NodeType


NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")


def get_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def setup_schema(driver):
    """インデックスと制約を作成する。"""
    with driver.session() as session:
        session.run(
            "CREATE CONSTRAINT doc_id IF NOT EXISTS "
            "FOR (n:Document) REQUIRE n.node_id IS UNIQUE"
        )
        for label in ["Section", "Table", "Header", "Row", "Cell"]:
            session.run(
                f"CREATE INDEX {label.lower()}_id IF NOT EXISTS "
                f"FOR (n:{label}) ON (n.node_id)"
            )
        # ベクトルインデックス（Neo4j 5.x+）
        session.run("""
            CREATE VECTOR INDEX cell_embedding IF NOT EXISTS
            FOR (n:Cell) ON (n.embedding)
            OPTIONS {indexConfig: {
                `vector.dimensions`: 384,
                `vector.similarity_function`: 'cosine'
            }}
        """)


def ingest_ast(ast_root: ASTNode, driver=None, embed_fn=None):
    """
    Document ASTをNeo4jに投入する。
    embed_fn: content -> List[float] の関数（省略時は埋め込みなし）
    """
    driver = driver or get_driver()
    with driver.session() as session:
        _ingest_node(session, ast_root, parent_id=None, embed_fn=embed_fn)


def _ingest_node(
    session, node: ASTNode, parent_id: Optional[str], embed_fn, prev_row_id: Optional[str] = None
):
    props = node.to_dict()

    if embed_fn and node.content.strip():
        node.embedding = embed_fn(node.content)
        props["embedding"] = node.embedding

    # ノードの作成
    label = node.node_type.value
    session.run(
        f"MERGE (n:{label} {{node_id: $node_id}}) SET n += $props",
        node_id=node.node_id,
        props={k: v for k, v in props.items() if k != "node_id"},
    )

    # 親子関係
    if parent_id:
        rel_type = _get_rel_type(node.node_type)
        session.run(
            f"MATCH (p {{node_id: $pid}}), (c {{node_id: $cid}}) "
            f"MERGE (p)-[:{rel_type}]->(c)",
            pid=parent_id, cid=node.node_id,
        )

    # Row間の NEXT 関係
    if node.node_type == NodeType.ROW and prev_row_id:
        session.run(
            "MATCH (a {node_id: $aid}), (b {node_id: $bid}) MERGE (a)-[:NEXT]->(b)",
            aid=prev_row_id, bid=node.node_id,
        )

    # 子ノードの再帰投入
    prev = None
    for child in node.children:
        _ingest_node(session, child, parent_id=node.node_id, embed_fn=embed_fn,
                     prev_row_id=prev if child.node_type == NodeType.ROW else None)
        if child.node_type == NodeType.ROW:
            prev = child.node_id

    # 同一列Cellの SAME_COLUMN 関係
    if node.node_type == NodeType.TABLE:
        _link_same_column_cells(session, node)


def _get_rel_type(node_type: NodeType) -> str:
    return {
        NodeType.SECTION: "CONTAINS",
        NodeType.TABLE: "CONTAINS",
        NodeType.HEADER: "HAS_HEADER",
        NodeType.ROW: "CONTAINS",
        NodeType.CELL: "CONTAINS",
    }.get(node_type, "CONTAINS")


def _link_same_column_cells(session, table_node: ASTNode):
    """同じ列インデックスのCellノード間にSAME_COLUMNエッジを貼る。"""
    rows = [c for c in table_node.children if c.node_type == NodeType.ROW]
    if len(rows) < 2:
        return

    col_count = max(len(r.children) for r in rows)
    for col_idx in range(col_count):
        col_cells = []
        for row in rows:
            matching = [c for c in row.children
                        if c.metadata.get("col_index") == col_idx]
            if matching:
                col_cells.append(matching[0].node_id)

        for i in range(len(col_cells) - 1):
            session.run(
                "MATCH (a {node_id: $aid}), (b {node_id: $bid}) "
                "MERGE (a)-[:SAME_COLUMN]->(b)",
                aid=col_cells[i], bid=col_cells[i + 1],
            )
```

---

### Step 8: GraphRAG クエリ (`graphrag.py`)

```python
# pipeline/graphrag.py
import os
from neo4j import GraphDatabase
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

_embed_model = None


def get_embed_model(model_name: str = "all-MiniLM-L6-v2") -> SentenceTransformer:
    global _embed_model
    if _embed_model is None:
        _embed_model = SentenceTransformer(model_name)
    return _embed_model


def embed(text: str) -> List[float]:
    return get_embed_model().encode(text).tolist()


def search(
    query: str,
    driver=None,
    top_k: int = 10,
    hop: int = 2,
) -> List[Dict[str, Any]]:
    """
    GraphRAGクエリ:
    1. クエリをベクトル化してCellの近傍検索（Vector RAG）
    2. ヒットしたCellから graph hop でコンテキスト収集（Graph RAG）
    """
    driver = driver or GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
    )
    query_embedding = embed(query)

    with driver.session() as session:
        # ① ベクトル近傍検索
        vector_hits = session.run(
            """
            CALL db.index.vector.queryNodes('cell_embedding', $top_k, $embedding)
            YIELD node AS cell, score
            RETURN cell.node_id AS cell_id,
                   cell.content AS content,
                   cell.metadata AS metadata,
                   score
            ORDER BY score DESC
            """,
            top_k=top_k,
            embedding=query_embedding,
        ).data()

        if not vector_hits:
            return []

        cell_ids = [h["cell_id"] for h in vector_hits]

        # ② グラフホップでコンテキスト拡張
        graph_ctx = session.run(
            f"""
            MATCH (seed) WHERE seed.node_id IN $cell_ids
            CALL apoc.path.subgraphNodes(seed, {{
                maxLevel: {hop},
                relationshipFilter: 'CONTAINS>|<CONTAINS|NEXT>|<NEXT|SAME_COLUMN>|<SAME_COLUMN'
            }}) YIELD node
            RETURN DISTINCT
                node.node_id AS node_id,
                labels(node)[0] AS node_type,
                node.content AS content,
                node.metadata AS metadata
            """,
            cell_ids=cell_ids,
        ).data()

        return {
            "vector_hits": vector_hits,
            "graph_context": graph_ctx,
        }


def format_context_for_llm(search_result: Dict) -> str:
    """検索結果をLLMプロンプト用のテキストに整形する。"""
    lines = ["## 関連セル (ベクトル検索)"]
    for hit in search_result.get("vector_hits", []):
        meta = hit.get("metadata", {})
        col = meta.get("column", "?")
        lines.append(f"- [{col}] {hit['content']}  (score={hit['score']:.3f})")

    lines.append("\n## グラフコンテキスト (隣接ノード)")
    for node in search_result.get("graph_context", []):
        ntype = node.get("node_type", "")
        lines.append(f"- ({ntype}) {node['content']}")

    return "\n".join(lines)
```

---

### Step 9: エントリーポイント (`main.py`)

```python
# pipeline/main.py
import argparse
import sys
from pathlib import Path

from .parsers.excel_parser import parse_excel
from .parsers.pdf_parser import parse_pdf
from .ast_builder import build_ast
from .neo4j_ingester import get_driver, setup_schema, ingest_ast
from .graphrag import embed, search, format_context_for_llm


def run_ingest(file_path: str, use_table_transformer: bool = False):
    path = Path(file_path)
    suffix = path.suffix.lower()

    print(f"[1/4] Parsing {suffix} file: {path.name}")
    if suffix in (".xlsx", ".xls"):
        tables = parse_excel(file_path)
    elif suffix == ".pdf":
        tables = parse_pdf(file_path, use_table_transformer=use_table_transformer)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")

    print(f"  → {len(tables)} table(s) extracted")

    print("[2/4] Building Document AST")
    ast_root = build_ast(tables, source_name=path.name)
    total_nodes = _count_nodes(ast_root)
    print(f"  → {total_nodes} AST nodes")

    print("[3/4] Ingesting into Neo4j")
    driver = get_driver()
    setup_schema(driver)
    ingest_ast(ast_root, driver=driver, embed_fn=embed)
    print("  → Done")

    print("[4/4] Pipeline complete. Run queries with:")
    print("  python -m pipeline.main --query 'your question here'")


def run_query(query_text: str, top_k: int = 10):
    print(f"[Query] {query_text}")
    result = search(query_text, top_k=top_k)
    context = format_context_for_llm(result)
    print(context)
    return context


def _count_nodes(node) -> int:
    return 1 + sum(_count_nodes(c) for c in node.children)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Document Graph Pipeline")
    parser.add_argument("--ingest", metavar="FILE", help="Excel/PDFファイルを投入")
    parser.add_argument("--query", metavar="TEXT", help="GraphRAGクエリ")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--table-transformer", action="store_true",
                        help="PDFをTable Transformerで処理（画像PDF用）")
    args = parser.parse_args()

    if args.ingest:
        run_ingest(args.ingest, use_table_transformer=args.table_transformer)
    elif args.query:
        run_query(args.query, top_k=args.top_k)
    else:
        parser.print_help()
```

---

### Step 10: 動作確認

```bash
# 環境変数設定
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="your_password"

# Excelファイルの投入
python -m pipeline.main --ingest sample.xlsx

# PDFの投入（テキストPDF）
python -m pipeline.main --ingest report.pdf

# PDFの投入（スキャン画像PDF → Table Transformer使用）
python -m pipeline.main --ingest scanned.pdf --table-transformer

# GraphRAGクエリ
python -m pipeline.main --query "売上が最も高い月は？"
```

**Neo4j Browser で確認するクエリ:**
```cypher
// グラフ全体の俯瞰
MATCH (n) RETURN n LIMIT 200

// Document→Table→Row の経路確認
MATCH path=(d:Document)-[:CONTAINS*]->(r:Row)
RETURN path LIMIT 50

// 特定カラム列の縦断
MATCH (c:Cell {metadata: {column: '売上'}})
-[:SAME_COLUMN*]->(c2:Cell)
RETURN c.content, c2.content
```

---

### Step 11: Claude API連携（オプション）

GraphRAGの文脈でClaude APIを使った回答生成:

```python
import anthropic
from pipeline.graphrag import search, format_context_for_llm

def ask(question: str) -> str:
    result = search(question)
    context = format_context_for_llm(result)

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="あなたは表形式データに精通したアナリストです。",
        messages=[{
            "role": "user",
            "content": f"以下のコンテキストを参照して質問に答えてください。\n\n{context}\n\n質問: {question}"
        }]
    )
    return response.content[0].text
```

---

## 拡張ポイント

| 課題 | 解決策 |
|------|--------|
| スキャンPDFのOCR | `paddleocr` または `easyocr` を `_recognize_table_structure` に統合 |
| 大規模ファイル | バッチ投入 + `UNWIND` でNeo4j書き込みを最適化 |
| 多言語埋め込み | `paraphrase-multilingual-MiniLM-L12-v2` モデルを使用 |
| リアルタイム更新 | ファイル変更検知 (`watchdog`) → 差分投入 |
| Cypher生成AI | LangChain `GraphCypherQAChain` または直接Cypherプロンプト |

## Wrap up

完了時に以下をレポートする:
- 投入したファイル数・テーブル数・ノード数
- Neo4j の接続URI
- 動作確認クエリの結果サンプル
- 未解決の問題（OCR精度、スキーマ設計の懸念など）
