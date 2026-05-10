---
title: "Claude CodeにKiro CLIを使わせてみた"
source: "https://zenn.dev/ncdc/articles/5bed6cd2f9f22b"
author:
published: 2026-05-08
created: 2026-05-09
description:
tags:
  - "clippings"
---
### 概要
Claude Codeをメインの設計・管理エージェントとし、実装タスクをKiro CLIに委任するワークフローの構築に関する解説記事。

### 要点
- **目的**
  - Claude Codeのコスト削減と品質向上（複数エージェントによる分担）。
  - 役割：Claude Codeが「エンジニア（設計・検証）」、Kiroが「プログラマー（実装・テスト）」。

- **スキルの仕組み**
  - Kiro CLI v2.0の「ヘッドレスモード（--no-interactive --trust-all-tools）」を活用し、自動実行を実現。
  - Claude Codeが実行前にタスクを明文化・整理することで、Kiroへの指示精度を向上。
  - Monitorツールを使い、非同期で途中経過やエラーを監視。

- **メリット**
  - 複雑な指示が必要なため、Claude Code側が設計を精緻化する副次的効果がある。
  - 実装作業のみをKiroへオフロードすることで、全体のusage消費を抑制。

- **課題**
  - 責任の所在が曖昧になり、エラー時にエージェント間で責任転嫁が発生する場合がある。
  - AIエージェントの出力に対する「人間による最終確認」は依然として不可欠。
