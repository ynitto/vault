---
title: "git commit 時に実装を理解しているのか claude code に質問させる"
type: "topic"
tags:
  - "claude-code"
  - "git"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/git commit 時に実装を理解しているのか claude code に質問させる.md"
summary: "AIエージェントへの実装丸投げによる「コード理解度の低下」を防ぐため、Gitの`pre-commit`フックを利用して「実装内容の自己確認」を自動化した取…"
---

# git commit 時に実装を理解しているのか claude code に質問させる

## 概要

AIエージェントへの実装丸投げによる「コード理解度の低下」を防ぐため、Gitの`pre-commit`フックを利用して「実装内容の自己確認」を自動化した取り組みについての記事です。

*発行: 2026-01-17 / [[claude-code-git-git-commit-claude-4cfdea]]*

## 主要なトピック

- [[claude-code]]
- [[git]]
- [[code-review]]

## 詳細

- AIエージェントへの実装丸投げによる「コード理解度の低下」を防ぐため、Gitの`pre-commit`フックを利用して「実装内容の自己確認」を自動化した取り組みについての記事です。
- 主な要点
- **課題意識**
- AI任せでコードを書くと、ロジックや意図（Why）が把握できず、トラブル対応やレビューに支障が出る。
- 「AIは思考をサボるツールではなく、思考を広げるツール」として活用する必要がある。
- **解決策：実装理解度チェックの自動化**
- `git commit`実行時にフックを起動し、ステージングされた差分をAI（Claude）に送信。
- AIが生成した「実装意図を確認するための質問リスト」をエディタ（Cursor）で表示。
- 特定の行（ブロッカー行）を削除して保存しない限りコミットできない仕組みを導入し、強制的に思考の時間を確保。

*発行: 2026-01-17 / [[claude-code-git-git-commit-claude-4cfdea]]*

## 関連テーマ

- [[claude-code]]
- [[git]]
- [[code-review]]

## 出典

- `60_Resources/git commit 時に実装を理解しているのか claude code に質問させる.md`
- https://zenn.dev/buno15/articles/bf8c2c7c5a137b
