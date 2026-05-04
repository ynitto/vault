---
title: "Kiro CLIのKnowledge managementを試してみた"
source: "https://dev.classmethod.jp/articles/kiro-cli-knowledge-management-experimental/"
author:
  - "[[神野 雄大]]"
published: 2025-12-13
created: 2026-04-30
description:
tags:
  - "clippings"
---
### 概要
Kiro CLIの「Knowledge management」機能（実験的機能）について、ローカルデータのインデックス化とチャット内でのRAG（検索拡張生成）活用方法を解説しています。

### 要点まとめ
- **機能概要**: ローカルのファイル・ディレクトリを永続的にインデックス化し、チャットセッションを跨いで検索が可能。
- **インデックスタイプ**: 用途に応じて2種類を選択
    - **Fast (BM25)**: キーワード検索。高速で、ログ、設定ファイル、大規模コードベース向け。
    - **Best (all-MiniLM-L6-v2)**: セマンティック検索。文脈理解に優れ、ドキュメントや論文向け。
- **主な操作コマンド**:
    - `kiro-cli settings chat.enableKnowledge true`: 機能有効化
    - `/knowledge add`: ナレッジベース追加（name, path, index-typeを指定）
    - `/knowledge show`: インデックス状況確認
- **運用のコツ**:
    - **分離**: ナレッジが混ざらないよう、カスタムエージェント機能でエージェントを使い分ける。
    - **フィルタリング**: `exclude`オプションや設定で不要なファイル（`node_modules`等）を除外する。
    - **正確性**: 外部知識の混入を避けたい場合は、プロンプトで「ドキュメント外の情報を使わない」よう指定する。
- **注意点**: 現在は実験的機能のため、仕様変更の可能性があることに留意。
