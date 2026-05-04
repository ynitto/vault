---
title: "Pandoc で Windows に作るmarkdown to html, docx 環境"
source: "https://qiita.com/tsujimitsu/items/907d7a2fae2057d0fb1f"
author:
  - "[[tsujimitsu]]"
published: 2015-04-18
created: 2026-04-30
description: "Pandoc のインストール github pandoc から最新版の Pandoc-x.yy.z-windows.msi をダウンロード。 Pandoc-x.yy.z-windows.msi をインストール。 システム環境変数 Path に 「C:/UsersUs..."
tags:
  - "clippings"
---
### 概要
Windows環境において、Pandocを使用してMarkdownファイルをHTMLやWord（docx）形式に変換する手順とコマンドを解説した記事です。

### 要点
* **インストール手順**
    * 公式GitHubからインストーラー（msi）を入手して実行。
    * システム環境変数のPathにインストール先を追加。

* **変換コマンドの基本**
    * `pandoc input.md -o output.ext` で出力形式を拡張子から自動判別。

* **HTML変換**
    * `pandoc input.md -s --self-contained -c github.css -o out.html`
    * GitHub風のスタイルを適用可能。

* **Word（docx）変換**
    * 標準変換: `pandoc input.md -o output.docx`
    * スタイル指定: `reference.docx` を生成・編集し、`--reference-docx` オプションで適用することで書式をカスタマイズ可能。
