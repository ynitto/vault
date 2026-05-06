---
title: "GitHub Copilot サブエージェントによるオーケストレーター パターンの実践"
type: "topic"
tags:
  - "git"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/GitHub Copilot サブエージェントによるオーケストレーター パターンの実践.md"
summary: "VS Code v1.107の新機能である「カスタムエージェント（.agent.md）を`runSubagent`で直接呼び出す機能」を活用し、開発ワーク…"
---

# GitHub Copilot サブエージェントによるオーケストレーター パターンの実践

## 概要

VS Code v1.107の新機能である「カスタムエージェント（.agent.md）を`runSubagent`で直接呼び出す機能」を活用し、開発ワークフロー全体（Issue作成〜PR生成）を自動化するオーケストレーター構築の実践解説。

*発行: 2025-12-03 / [[git-code-review-copilot-https-zenn-dev-openjny-articles-e11450f61d067f-d0a5f9]]*

## 主要なトピック

- [[git]]
- [[code-review]]

## 詳細

- VS Code v1.107の新機能である「カスタムエージェント（.agent.md）を`runSubagent`で直接呼び出す機能」を活用し、開発ワークフロー全体（Issue作成〜PR生成）を自動化するオーケストレーター構築の実践解説。
- 要点まとめ
- **サブエージェント化のメリット**
- コンテキスト肥大化の防止、責任の明確化、保守性の向上。
- レビュープロセス等の特定フェーズの独立による品質確保。
- **設計のポイント：責任分離**
- 各エージェントに「Issue」「Plan」「Impl」「Review」「PR」の役割を特化させ、オーケストレーターは指揮者に徹する。
- エージェント定義には必要最小限のツールのみを指定（Context Rot対策）。
- **開発ワークフローの自動化**

*発行: 2025-12-03 / [[git-code-review-copilot-https-zenn-dev-openjny-articles-e11450f61d067f-d0a5f9]]*

## 関連テーマ

- [[git]]
- [[code-review]]

## 出典

- `60_Resources/GitHub Copilot サブエージェントによるオーケストレーター パターンの実践.md`
- https://zenn.dev/openjny/articles/e11450f61d067f
