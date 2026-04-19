---
original_source: 00_Inbox/Clippings/Claude Code の集中力を保つ Agent Skills を作った.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, 2026-04]
---

---
title: "Claude Code の集中力を保つ Agent Skills を作った"
source: "https://zenn.dev/cureapp/articles/c5016035a7d53d"
author:
published: 2026-01-13
created: 2026-04-19
description:
tags:
  - "clippings"
---
## 記事の要約
Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度の低下を解決するため、複雑なタスクをステップごとに分割して順次実行する仕組みです。

## 要点まとめ
- **課題**: 複数の指示をまとめて投げると、後半の指示が無視されたり回答の質が低下したりする「注意力の分散」が発生する。
- **解決策**: タスクを細分化し、1ステップずつ指示を与えることで、モデルがその作業に集中できる環境を作る。
- **仕組み**: `workflows/` ディレクトリ配下にYAMLとプロンプトファイルを定義することで、ステップを順番に自動実行する。
- **メリット**: コードレビュー（セキュリティや命名規則など）、調査タスク、リファクタリング、TDDなど、複数の観点や手順が必要な作業の品質が向上する。
- **導入方法**: `7tsuno/claude-plugins` を追加し、インストールして利用可能。