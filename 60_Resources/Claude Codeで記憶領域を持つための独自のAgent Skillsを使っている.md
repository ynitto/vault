---
title: "Claude Codeで記憶領域を持つための独自のAgent Skillsを使っている"
source: "https://zenn.dev/yamadashy/articles/claude-code-agent-skills-agent-memory"
author:
published: 2026-01-05
created: 2026-04-30
description:
tags:
  - "clippings"
---
### 概要
Claude Codeで作業の中断・再開をスムーズにするための、Markdownベースの個人用記憶領域「agent-memory」スキルの導入方法と利点について解説しています。

### 要点まとめ
- **目的**: 差し込み作業時などに、現在のコンテキストや判断意図を記憶させ、後から容易に再開できるようにする。
- **仕組み**: 
    - `.claude/skills/agent-memory/` 配下に記憶をMarkdownファイルとして保存。
    - `rg` (ripgrep) を活用し、`summary` を基に再開時に必要なファイルのみを効率的に読み込む。
    - プライベート情報のため `.gitignore` で除外。
- **メリット**: 
    - 履歴を遡る手間を削減。
    - ファイルベースのため人間が直接編集・閲覧可能。
    - MCP等の他ツールに依存せず、ツールを跨いでのポータビリティがある。
- **導入手順**: 
    - 指定ディレクトリ作成、`SKILL.md` の配置、`.gitignore` による除外設定のみでシンプルに利用可能。
