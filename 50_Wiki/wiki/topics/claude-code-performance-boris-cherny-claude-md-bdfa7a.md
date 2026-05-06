---
title: "Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する"
type: "topic"
tags:
  - "claude-code"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する.md"
summary: "`CLAUDE.md`は、Claude Codeがセッション開始時に読み込む設定ファイルです。プロジェクトルートに配置することで、AIにチームのルールや作…"
---

# Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する

## 概要

`CLAUDE.md`は、Claude Codeがセッション開始時に読み込む設定ファイルです。プロジェクトルートに配置することで、AIにチームのルールや作業方針を事前に伝え、AIを外部メモリのように活用するための仕組みです。

*発行: 2026-02-23 / [[claude-code-performance-boris-cherny-claude-md-bdfa7a]]*

## 主要なトピック

- [[claude-code]]
- [[performance]]

## 詳細

- `CLAUDE.md`は、Claude Codeがセッション開始時に読み込む設定ファイルです。プロジェクトルートに配置することで、AIにチームのルールや作業方針を事前に伝え、AIを外部メモリのように活用するための仕組みです。
- 主要なワークフローと指針
- **Planモードの活用**: 3ステップ以上のタスクは計画を先行させ、曖昧さを排除する。
- **サブエージェント戦略**: コンテキストをクリーンに保つため、リサーチや並列処理は専用エージェントへ委譲する。
- **自己改善ループ**: 修正内容は`tasks/lessons.md`に記録し、同じミスを繰り返さない仕組みを構築する。
- **完了条件の厳守**: 動作証明（テスト・ログ確認）なしの完了を禁止する。
- **エレガントさの追求**: 過剰設計を避けつつ、重要な変更では「より良い手法がないか」を自問させる。
- **自律的修正**: CIの失敗やバグ修正において、質問を挟まず自律的に解決させる。
- タスク管理と原則

*発行: 2026-02-23 / [[claude-code-performance-boris-cherny-claude-md-bdfa7a]]*

## 関連テーマ

- [[claude-code]]
- [[performance]]

## 出典

- `../60_Resources/Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する.md`
- https://qiita.com/uno_ha07/items/5820d195510861b5be71
