---
title: "Claude Code の集中力を保つ Agent Skills を作った"
type: "topic"
tags:
  - "ai-agent"
  - "claude-code"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md"
summary: "Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度…"
---

# Claude Code の集中力を保つ Agent Skills を作った

## 概要

Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度の低下を解決するため、複雑なタスクをステップごとに分割して順次実行する仕組みです。

*発行: 2026-01-13 / [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]*

## 主要なトピック

- [[ai-agent]]
- [[claude-code]]
- [[code-review]]

## 詳細

- Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度の低下を解決するため、複雑なタスクをステップごとに分割して順次実行する仕組みです。
- 要点まとめ
- **課題**: 複数の指示をまとめて投げると、後半の指示が無視されたり回答の質が低下したりする「注意力の分散」が発生する。
- **解決策**: タスクを細分化し、1ステップずつ指示を与えることで、モデルがその作業に集中できる環境を作る。
- **仕組み**: `workflows/` ディレクトリ配下にYAMLとプロンプトファイルを定義することで、ステップを順番に自動実行する。
- **メリット**: コードレビュー（セキュリティや命名規則など）、調査タスク、リファクタリング、TDDなど、複数の観点や手順が必要な作業の品質が向上する。
- **導入方法**: `7tsuno/claude-plugins` を追加し、インストールして利用可能。

*発行: 2026-01-13 / [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]*

## 関連テーマ

- [[ai-agent]]
- [[claude-code]]
- [[code-review]]

## 出典

- `../60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md`
- https://zenn.dev/cureapp/articles/c5016035a7d53d
