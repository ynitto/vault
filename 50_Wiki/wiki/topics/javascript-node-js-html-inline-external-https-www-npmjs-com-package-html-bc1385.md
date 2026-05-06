---
title: "html-inline-external"
type: "topic"
tags:
  - "javascript"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/html-inline-external.md"
summary: "外部ファイル（JavaScript, CSS, 画像など）を単一のHTMLファイルに埋め込み（インライン化）するためのNode.jsユーティリティです。"
---

# html-inline-external

## 概要

外部ファイル（JavaScript, CSS, 画像など）を単一のHTMLファイルに埋め込み（インライン化）するためのNode.jsユーティリティです。

*発行: 2023-01-07 / [[javascript-node-js-html-inline-external-https-www-npmjs-com-package-html-bc1385]]*

## 主要なトピック

- [[javascript]]
- [[node-js]]

## 詳細

- 外部ファイル（JavaScript, CSS, 画像など）を単一のHTMLファイルに埋め込み（インライン化）するためのNode.jsユーティリティです。
- 主な特徴
- **リソースの統合**: `<script>`, `<link>`, `<img>` タグで読み込まれている外部ファイルをHTML内に直接展開。
- **画像処理**: 画像（`<img>`）をBase64文字列に変換。
- **柔軟な出力**: コンソール出力、ファイル保存、クリップボードへのコピーに対応。
- **カスタマイズ**: 処理対象タグの指定や、出力の整形（Prettify）/最小化（Minify）が可能。
- 利用方法
- **CLI**: `npx html-inline-external --src index.html --dest output.html`
- **Node API**: `require('html-inline-external')` を使用してプログラムから呼び出し可能。

*発行: 2023-01-07 / [[javascript-node-js-html-inline-external-https-www-npmjs-com-package-html-bc1385]]*

## 関連テーマ

- [[javascript]]
- [[node-js]]

## 出典

- `../60_Resources/html-inline-external.md`
- https://www.npmjs.com/package/html-inline-external
