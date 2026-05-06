---
title: "WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata"
type: "topic"
tags:
  - "obsidian"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata.md"
summary: "WSL上のAI(CLI)とWindows側Obsidianの連携方法"
---

# WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata

## 概要

WSL上のAI(CLI)とWindows側Obsidianの連携方法

*発行: 2025-08-30 / [[obsidian-wsl-ai-cli-win-838938]]*

## 主要なトピック

- [[obsidian]]

## 詳細

- この記事では、WSL上のAIエージェント（CLIツール）とWindows上のObsidianを連携させ、効率的な情報管理と作業フローを実現する方法について解説しています。
- 要点
- **目的**: WSL/Linux側からObsidianのノートを直接編集できるようにし、「Linuxでの作業・Windowsでのノート整理」の二軸運用をストレスなく行う。
- **対象読者**: コマンド操作に慣れていない初心者。
- **所要時間**: 5〜15分。
- **推奨方法**: 方法B（automount方式）が安定性に優れるため推奨。
- 全体像
- 1.  **Obsidian Vault**: Windows上に配置（例: `C:\\Users\\...\\Obsidian\\MyNote`）。
- 2.  **WSLからのアクセス**: `/mnt/c/Users/50_Wiki/wiki/topics.50_Wiki/wiki/topics/Obsidian/MyNote` として認識。

*発行: 2025-08-30 / [[obsidian-wsl-ai-cli-win-838938]]*

## 関連テーマ

- [[obsidian]]

## 出典

- `60_Resources/WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata.md`
- https://note.com/hinatasatou/n/n46af3c6259eb
