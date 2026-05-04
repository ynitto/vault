---
title: "html-inline-external"
source: "https://www.npmjs.com/package/html-inline-external"
author:
published: 2023-01-07
created: 2026-05-01
description: "Helps include/inline external Script/CSS/Images and compiles into a Single HTML page.. Latest version: 1.0.10, last published: 3 years ago. Start using html-inline-external in your project by running `npm i html-inline-external`. There are 0 other projects in the npm registry using html-inline-external."
tags:
  - "clippings"
---
### html-inline-external の概要
外部ファイル（JavaScript, CSS, 画像など）を単一のHTMLファイルに埋め込み（インライン化）するためのNode.jsユーティリティです。

### 主な特徴
- **リソースの統合**: `<script>`, `<link>`, `<img>` タグで読み込まれている外部ファイルをHTML内に直接展開。
- **画像処理**: 画像（`<img>`）をBase64文字列に変換。
- **柔軟な出力**: コンソール出力、ファイル保存、クリップボードへのコピーに対応。
- **カスタマイズ**: 処理対象タグの指定や、出力の整形（Prettify）/最小化（Minify）が可能。

### 利用方法
- **CLI**: `npx html-inline-external --src index.html --dest output.html`
- **Node API**: `require('html-inline-external')` を使用してプログラムから呼び出し可能。

### オプション例
- `--src`: 元のHTMLファイルパス
- `--dest`: 保存先ファイルパス
- `--pretty` / `--minify`: 出力コードのフォーマット設定