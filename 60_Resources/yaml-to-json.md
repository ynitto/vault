---
title: "yaml-to-json"
source: "https://www.npmjs.com/package/yaml-to-json"
author:
published: 2014-11-21
created: 2026-05-01
description: "Convert YAML into JSON. Supports YAML frontmatter, YAML multidocs and other mixed text-and-yaml documents. Can process Textile, Markdown and AsciiDoc strings. Works on the command-line and in node.js.. Latest version: 0.3.0, last published: 11 years ago. Start using yaml-to-json in your project by running `npm i yaml-to-json`. There are 4 other projects in the npm registry using yaml-to-json."
tags:
  - "clippings"
---
### 概要
`yaml-to-json`は、YAMLファイルをJSON形式に変換するためのコマンドラインおよびNode.js用ライブラリです。特にフロントマターを含むドキュメントや、複数のYAMLドキュメントが混在するファイルの解析に最適化されています。

### 主な特徴と機能
* **柔軟な解析**: 複数のYAMLドキュメントをサポートし、ディレクトリ単位での一括変換が可能。
* **Fussy Parsing**: `--fussy`フラグにより、テキストとデータが混在する環境で誤変換を防ぐ厳密な解析が可能。
* **マークアップ変換**: Markdown、Textile、AsciiDocをHTMLに変換し、必要に応じて生データ（raw）を保持可能。
* **Proseモード**: `--prose`フラグを使用すると、ブログ記事などの「フロントマター＋本文」形式を、メタデータとコンテンツが統合された整理済みのJSON構造として出力可能。

### 導入方法
- **CLI**: `npm install yaml-to-json -g` でインストールし、`yaml2json <file>` で使用。
- **Node.js**: `require('yaml-to-json')` でプログラム内に組み込み可能（戻り値はJavaScriptオブジェクト）。