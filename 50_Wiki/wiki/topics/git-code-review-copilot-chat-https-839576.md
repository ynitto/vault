---
title: "GitHub Copilot Chat のサブエージェントを検証してみた: コンテキスト分離の効果と限界"
type: "topic"
tags:
  - "git"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/GitHub Copilot Chat のサブエージェントを検証してみた コンテキスト分離の効果と限界.md"
summary: "GitHub Copilot Chat サブエージェントの概要と活用"
---

# GitHub Copilot Chat のサブエージェントを検証してみた: コンテキスト分離の効果と限界

## 概要

GitHub Copilot Chat サブエージェントの概要と活用

*発行: 2025-12-03 / [[git-code-review-copilot-chat-https-839576]]*

## 主要なトピック

- [[git]]
- [[code-review]]

## 詳細

- GitHub Copilot Chat のサブエージェント（`agent/runSubagent`）は、複雑なタスクを独立したセッションで処理するための機能です。
- 主なメリット
- **コンテキスト分離**: メインのチャットセッションを肥大化させず、特定のタスクに集中したコンテキストを維持できる。
- **並列処理**: 複数のサブエージェントを並列実行可能（要 VS Code Insiders）。
- **効率化**: 複雑な調査、コード検索、段階的なタスクにおいて、メインエージェントの負荷を軽減できる。
- 活用におけるポイント
- **効果的な場面**:
- レビューや調査など、独立した視点が必要なタスク。
- ファイル単位で独立して処理可能な作業。

*発行: 2025-12-03 / [[git-code-review-copilot-chat-https-839576]]*

## 関連テーマ

- [[git]]
- [[code-review]]

## 出典

- `../60_Resources/GitHub Copilot Chat のサブエージェントを検証してみた コンテキスト分離の効果と限界.md`
- https://zenn.dev/openjny/articles/2619050ec7f167
