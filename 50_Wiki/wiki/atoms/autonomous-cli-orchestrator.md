---
title: "自律的CLIオーケストレーター"
type: concept
tags: [autonomous, cli, orchestrator, kiro, spec-first, ai-agent]
created: 2026-05-03
updated: 2026-05-03
sources:
  - "自律的Kiro CLIオーケストレーター"
summary: "仕様優先アプローチとLLMの自律実行を組み合わせたCLIエージェント設計パターン。"
---

# 自律的CLIオーケストレーター

## 概要

仕様（spec）を先に定義し、LLMが自律的にタスクを実行・管理するCLIエージェントの設計パターン。Kiroの仕様優先アプローチとClaudeの自律機能を統合した形で実装される。

*発行: 2026-02-15*

## 詳細

### 設計思想

- **仕様優先（Spec-First）**: タスク実行前に仕様を明確化し、LLMがそれに従って自律実行する
- **スケーラブルな並列実行**: 小規模タスクはローカル、大規模タスク（60+）はEC2等クラウドで並列処理
- **モデル最適化**: タスク複雑度に応じてHaiku/Sonnet/Opusを使い分けることでコスト効率を向上

### 実装例

[[bob-the-builder|Bob-The-Builder]] がこのパターンの具体的な実装として公開されている。

## 関連

- [[bob-the-builder]]

## 出典

- [[60_Resources/自律的Kiro CLIオーケストレーター（2026-05-05）]]（Reddit r/kiroIDE, 2026-02-15）
