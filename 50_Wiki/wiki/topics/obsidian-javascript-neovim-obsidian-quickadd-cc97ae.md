---
title: "Neovimでしていたタスク管理をObsidianのQuickAddプラグインでやってみた"
type: "topic"
tags:
  - "obsidian"
  - "javascript"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Neovimでしていたタスク管理をObsidianのQuickAddプラグインでやってみた.md"
summary: "Neovimで実現していたタスク管理方法（タスクのファイル化・アーカイブ）を、ObsidianのQuickAddプラグインとJavaScriptを活用して…"
---

# Neovimでしていたタスク管理をObsidianのQuickAddプラグインでやってみた

## 概要

Neovimで実現していたタスク管理方法（タスクのファイル化・アーカイブ）を、ObsidianのQuickAddプラグインとJavaScriptを活用して再現する手順を解説します。

*発行: 2025-09-15 / [[obsidian-javascript-neovim-obsidian-quickadd-cc97ae]]*

## 主要なトピック

- [[obsidian]]
- [[javascript]]

## 詳細

- Neovimで実現していたタスク管理方法（タスクのファイル化・アーカイブ）を、ObsidianのQuickAddプラグインとJavaScriptを活用して再現する手順を解説します。
- Neovimでのタスク管理（以前の手法）
- `main.md`にタスクリストを記述。
- 各タスクの詳細は個別のMarkdownファイルに分割。
- **ConvertTask**: `main.md`のタスク行から詳細ファイルを作成し、リンクに変換。
- **ArchiveTask**: 完了したタスクのファイルをアーカイブディレクトリに移動。
- Obsidianでの実現方法
- 1. ディレクトリ構成
- `vault/scripts/`: QuickAddマクロ用のJavaScriptファイルを配置。

*発行: 2025-09-15 / [[obsidian-javascript-neovim-obsidian-quickadd-cc97ae]]*

## 関連テーマ

- [[obsidian]]
- [[javascript]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Neovimでしていたタスク管理をObsidianのQuickAddプラグインでやってみた.md`
- https://zenn.dev/moneyforward/articles/94d5a22f3ab4f1
