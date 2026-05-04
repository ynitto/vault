---
title: "Markdown ドキュメント間の整合性を検証する contextlint を作っている話"
type: "topic"
tags:
  - "claude-code"
  - "mcp"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Markdown ドキュメント間の整合性を検証する contextlint を作っている話.md"
summary: "`contextlint` は、AI 活用型開発（仕様駆動開発：SDD）において、Markdown ドキュメント間の整合性を自動検証する静的解析ツールです。"
---

# Markdown ドキュメント間の整合性を検証する contextlint を作っている話

## 概要

`contextlint` は、AI 活用型開発（仕様駆動開発：SDD）において、Markdown ドキュメント間の整合性を自動検証する静的解析ツールです。

*発行: 2026-03-07 / [[claude-code-mcp-markdown-contextlint-https-b7c780]]*

## 主要なトピック

- [[claude-code]]
- [[mcp]]

## 詳細

- `contextlint` は、AI 活用型開発（仕様駆動開発：SDD）において、Markdown ドキュメント間の整合性を自動検証する静的解析ツールです。
- 主な要点
- **課題**: ドキュメントが増えると手作業では相互参照やIDの整合性維持が困難。
- **静的解析の利点**: LLM を使った検証と異なり、高速（数秒）かつコストがゼロで、判定が決定論的（再現性が高い）。
- **主な検証カテゴリ**:
- **テーブル検証 (TBL)**: 必須カラムの確認や値の制約。
- **構造検証 (SEC/STR)**: 必須セクションやファイルの存在確認。
- **参照検証 (REF)**: ドキュメント間のリンクや ID の一貫性チェック。
- **グラフ検証 (GRP)**: 依存関係の分析（トレーサビリティの確保、循環参照の検出）。

*発行: 2026-03-07 / [[claude-code-mcp-markdown-contextlint-https-b7c780]]*

## 関連テーマ

- [[claude-code]]
- [[mcp]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Markdown ドキュメント間の整合性を検証する contextlint を作っている話.md`
- https://zenn.dev/nozomi_cobo/articles/contextlint-introduction
