---
title: "Pandoc で Windows に作るmarkdown to html, docx 環境"
type: "topic"
tags:
  - "git"
  - "tsujimitsu"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Pandoc で Windows に作るmarkdown to html, docx 環境.md"
summary: "Windows環境において、Pandocを使用してMarkdownファイルをHTMLやWord（docx）形式に変換する手順とコマンドを解説した記事です。"
---

# Pandoc で Windows に作るmarkdown to html, docx 環境

## 概要

Windows環境において、Pandocを使用してMarkdownファイルをHTMLやWord（docx）形式に変換する手順とコマンドを解説した記事です。

*発行: 2015-04-18 / [[git-tsujimitsu-pandoc-windows-markdown-d3cbe5]]*

## 主要なトピック

- [[git]]
- [[tsujimitsu]]

## 詳細

- Windows環境において、Pandocを使用してMarkdownファイルをHTMLやWord（docx）形式に変換する手順とコマンドを解説した記事です。
- 要点
- **インストール手順**
- 公式GitHubからインストーラー（msi）を入手して実行。
- システム環境変数のPathにインストール先を追加。
- **変換コマンドの基本**
- `pandoc input.md -o output.ext` で出力形式を拡張子から自動判別。
- **HTML変換**
- `pandoc input.md -s --self-contained -c github.css -o out.html`

*発行: 2015-04-18 / [[git-tsujimitsu-pandoc-windows-markdown-d3cbe5]]*

## 関連テーマ

- [[git]]
- [[tsujimitsu]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Pandoc で Windows に作るmarkdown to html, docx 環境.md`
- https://qiita.com/tsujimitsu/items/907d7a2fae2057d0fb1f
