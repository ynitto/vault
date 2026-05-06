---
title: "yaml-to-json"
type: "topic"
tags:
  - "javascript"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/yaml-to-json.md"
summary: "`yaml-to-json`は、YAMLファイルをJSON形式に変換するためのコマンドラインおよびNode.js用ライブラリです。特にフロントマターを含む…"
---

# yaml-to-json

## 概要

`yaml-to-json`は、YAMLファイルをJSON形式に変換するためのコマンドラインおよびNode.js用ライブラリです。特にフロントマターを含むドキュメントや、複数のYAMLドキュメントが混在するファイルの解析に最適化されています。

*発行: 2014-11-21 / [[javascript-node-js-yaml-to-json-https-www-npmjs-com-package-yaml-to-json-57a168]]*

## 主要なトピック

- [[javascript]]
- [[node-js]]

## 詳細

- `yaml-to-json`は、YAMLファイルをJSON形式に変換するためのコマンドラインおよびNode.js用ライブラリです。特にフロントマターを含むドキュメントや、複数のYAMLドキュメントが混在するファイルの解析に最適化されています。
- 主な特徴と機能
- **柔軟な解析**: 複数のYAMLドキュメントをサポートし、ディレクトリ単位での一括変換が可能。
- **Fussy Parsing**: `--fussy`フラグにより、テキストとデータが混在する環境で誤変換を防ぐ厳密な解析が可能。
- **マークアップ変換**: Markdown、Textile、AsciiDocをHTMLに変換し、必要に応じて生データ（raw）を保持可能。
- **Proseモード**: `--prose`フラグを使用すると、ブログ記事などの「フロントマター＋本文」形式を、メタデータとコンテンツが統合された整理済みのJSON構造として出力可能。
- 導入方法
- **CLI**: `npm install yaml-to-json -g` でインストールし、`yaml2json <file>` で使用。
- **Node.js**: `require('yaml-to-json')` でプログラム内に組み込み可能（戻り値はJavaScriptオブジェクト）。

*発行: 2014-11-21 / [[javascript-node-js-yaml-to-json-https-www-npmjs-com-package-yaml-to-json-57a168]]*

## 関連テーマ

- [[javascript]]
- [[node-js]]

## 出典

- `60_Resources/yaml-to-json.md`
- https://www.npmjs.com/package/yaml-to-json
