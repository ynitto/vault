---
title: "Markdown ドキュメント間の整合性を検証する contextlint を作っている話"
source: "https://zenn.dev/nozomi_cobo/articles/contextlint-introduction"
author:
published: 2026-03-07
created: 2026-04-30
description:
tags:
  - "clippings"
---
### 概要
`contextlint` は、AI 活用型開発（仕様駆動開発：SDD）において、Markdown ドキュメント間の整合性を自動検証する静的解析ツールです。

### 主な要点
- **課題**: ドキュメントが増えると手作業では相互参照やIDの整合性維持が困難。
- **静的解析の利点**: LLM を使った検証と異なり、高速（数秒）かつコストがゼロで、判定が決定論的（再現性が高い）。
- **主な検証カテゴリ**:
    - **テーブル検証 (TBL)**: 必須カラムの確認や値の制約。
    - **構造検証 (SEC/STR)**: 必須セクションやファイルの存在確認。
    - **参照検証 (REF)**: ドキュメント間のリンクや ID の一貫性チェック。
    - **グラフ検証 (GRP)**: 依存関係の分析（トレーサビリティの確保、循環参照の検出）。
    - **コンテキスト検証 (CTX)**: 用語集との一貫性やプレースホルダーの検出。
- **拡張機能**:
    - **CLI**: `impact`, `slice`, `graph` 等で構造を可視化・分析。
    - **MCP 対応**: Claude や Cursor などの AI ツールから直接 lint や分析を呼び出し可能。
    - **Context Compiler**: ドキュメントと設定から Claude Code 向けの `SKILL.md` を生成し、AI のコンテキスト理解を向上。
- **補完関係**: Markdown のフォーマットを検証する `markdownlint` と併用することで、より堅牢な「Docs as Code」環境を実現。
