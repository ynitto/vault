---
title: "Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する"
type: "topic"
tags:
  - "ai-agent"
  - "claude-code"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する.md"
summary: "「generating-skills-from-logs」は、Claude Codeの操作履歴やターミナルのCLIコマンド履歴を分析し、ユーザーの繰り返し…"
---

# Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する

## 概要

「generating-skills-from-logs」は、Claude Codeの操作履歴やターミナルのCLIコマンド履歴を分析し、ユーザーの繰り返している作業を抽出して「Agent Skill」を自動生成するツールです。

*発行: 2026-02-11 / [[ai-agent-claude-code-claude-cli-agent-e8cd76]]*

## 主要なトピック

- [[ai-agent]]
- [[claude-code]]

## 詳細

- 「generating-skills-from-logs」は、Claude Codeの操作履歴やターミナルのCLIコマンド履歴を分析し、ユーザーの繰り返している作業を抽出して「Agent Skill」を自動生成するツールです。
- 要点
- **自動化の仕組み**: 過去の履歴をWHAT（ゴール）、HOW（手段）、FLOW（プロンプト連鎖）の3軸で分析し、スキル化の優先度を判定します。
- **分析ソース**: `~/.claude/history.jsonl`（Claudeの操作）と`~/.zsh_history`等のCLI履歴を統合してパターンを特定します。
- **プロセス**: 6つのフェーズ（データ収集→パターン抽出→適性評価→ユーザー選択→スキル生成→品質検証）で実行されます。
- **利点**:
- Anthropicの公式ベストプラクティスに基づいた高品質なSkillを作成可能。
- 既存のSkillとの重複を除外して効率的に自動化を推進。
- 面倒なSkill作成作業を大幅に省力化できる。

*発行: 2026-02-11 / [[ai-agent-claude-code-claude-cli-agent-e8cd76]]*

## 関連テーマ

- [[ai-agent]]
- [[claude-code]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する.md`
- https://zenn.dev/takiko/articles/claude-code-skill-from-logs
