# Wiki スキーマ

この Wiki は `60_Resources/` の技術資料を、再利用しやすい概念ページとトピックページへ整理するための知識ベースです。

## ディレクトリ構造

- `wiki/atoms/` — 個別トピックのページ（概念・用語・人物・製品・組織）
- `wiki/topics/` — 各リソースや複数概念を横断するまとめページ
- `wiki/meta/` — `hot.md`（最近のコンテキスト）

## ページ規約

- フロントマター必須（`title`, `type`, `tags`, `created`, `updated`, `sources`, `summary`）
- `type`: `concept | term | person | organization | product | topic`
- 内部リンクは `[[slug]]` 形式を使う
- ファイル名は原則として英小文字 + ハイフン
- 各ページに `## 関連` または `## 関連テーマ` セクションを置く
- 各ページに `## 出典` セクションを置き、元リソースを列挙する

## この Wiki のドメイン

- AI エージェント / LLM / 開発支援
- AWS / クラウドアーキテクチャ / 運用
- ソフトウェア設計 / テスト / レビュー
- Obsidian / PKM / 開発ワークフロー

## カスタムルール

- `60_Resources/` の各ファイルに対して少なくとも 1 つの `topics` ページを対応付ける
- 頻出概念は `atoms` に集約し、各 `topics` から相互リンクする
- 発行日が分かるソースは本文ブロック末尾に `*発行: YYYY-MM-DD / [[topic-slug]]*` を付ける
