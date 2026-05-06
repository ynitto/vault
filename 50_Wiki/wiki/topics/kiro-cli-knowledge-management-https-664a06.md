---
title: "Kiro CLIのKnowledge managementを試してみた"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Kiro CLIのKnowledge managementを試してみた.md"
summary: "Kiro CLIの「Knowledge management」機能（実験的機能）について、ローカルデータのインデックス化とチャット内でのRAG（検索拡張生…"
---

# Kiro CLIのKnowledge managementを試してみた

## 概要

Kiro CLIの「Knowledge management」機能（実験的機能）について、ローカルデータのインデックス化とチャット内でのRAG（検索拡張生成）活用方法を解説しています。

*発行: 2025-12-13 / [[kiro-cli-knowledge-management-https-664a06]]*

## 主要なトピック


## 詳細

- Kiro CLIの「Knowledge management」機能（実験的機能）について、ローカルデータのインデックス化とチャット内でのRAG（検索拡張生成）活用方法を解説しています。
- 要点まとめ
- **機能概要**: ローカルのファイル・ディレクトリを永続的にインデックス化し、チャットセッションを跨いで検索が可能。
- **インデックスタイプ**: 用途に応じて2種類を選択
- **Fast (BM25)**: キーワード検索。高速で、ログ、設定ファイル、大規模コードベース向け。
- **Best (all-MiniLM-L6-v2)**: セマンティック検索。文脈理解に優れ、ドキュメントや論文向け。
- **主な操作コマンド**:
- `kiro-cli settings chat.enableKnowledge true`: 機能有効化
- `/knowledge add`: ナレッジベース追加（name, path, index-typeを指定）

*発行: 2025-12-13 / [[kiro-cli-knowledge-management-https-664a06]]*

## 関連テーマ


## 出典

- `60_Resources/Kiro CLIのKnowledge managementを試してみた.md`
- https://dev.classmethod.jp/articles/kiro-cli-knowledge-management-experimental/
