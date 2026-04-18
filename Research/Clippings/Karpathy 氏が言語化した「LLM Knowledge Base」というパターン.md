---
title: "Karpathy 氏が言語化した「LLM Knowledge Base」というパターン"
source: "https://dev.classmethod.jp/articles/karpathy-llm-knowledge-base/"
author:
  - "[[森茂洋]]"
published: 2026-04-05
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 要約
Andrej Karpathy氏が提唱した「LLM Knowledge Base」という概念を紹介し、生のドキュメントをLLMに構造化・コンパイルさせることで、永続的なナレッジベースを構築する手法と自身の運用事例を解説しています。

### LLM Knowledge Baseの重要ポイント
- **コンセプト**: 生データ（Raw sources）をLLMが読み込み、規約（Schema）に基づいて整理・構造化されたWikiを生成・永続化する。
- **RAGとの違い**: 
    - **RAG**: 質問ごとに断片を検索（一時的）。
    - **LLM Knowledge Base**: 知識を事前に整理し蓄積（永続的）。回答をWikiへフィードバックし、知識を複利的に成長させる。
- **3つの操作**:
    - **Ingest**: ソースを統合・整理。
    - **Query**: 質問し、回答をWikiに還元。
    - **Lint**: 矛盾やリンク切れを検出し、情報の健全性を保つ。
- **役割分担**: LLMに「保守（相互参照、統合、チェック）」という退屈な作業を任せ、人間は「キュレーションと方向づけ」に集中する。
- **実践方法**:
    - Claude Codeを活用し、Rawフォルダの情報を「kb-compile」コマンドでWiki層に自動コンパイル。
    - メモリ基盤（Mem0等）と組み合わせることで、検索性能と俯瞰性の両立を目指す。