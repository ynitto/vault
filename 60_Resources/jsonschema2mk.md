---
title: "jsonschema2mk"
source: "https://www.npmjs.com/package/jsonschema2mk#load-external-plugins-option-plugin"
author:
published: 2026-03-30
created: 2026-05-01
description: "JSON schema to markdown generator. Latest version: 2.1.3, last published: a month ago. Start using jsonschema2mk in your project by running `npm i jsonschema2mk`. There are 1 other projects in the npm registry using jsonschema2mk."
tags:
  - "clippings"
---
### 概要
`jsonschema2mk`は、JSON Schema仕様からMarkdown形式のドキュメントを生成するツールです。

### 主な特徴
* **幅広い対応**: 基本属性、数値、文字列、配列、オブジェクト、論理演算（allOf/oneOf等）など、多岐にわたるJSON Schema機能に対応。
* **柔軟なカスタマイズ**: `partials`機能や独自のプラグインによる出力形式の変更が可能。
* **拡張機能**: YAML形式での例示やフロントマターの追加など、便利な拡張機能が利用可能。

### 基本的な使い方
* **インストール**: `npm install jsonschema2mk`
* **CLI実行**: `npx jsonschema2mk --schema schema.json > DOC.md`
* **ライブラリ利用**: Node.jsアプリケーション内でクラスとしてインスタンス化し、`convert`メソッドで変換可能。

### 注意点
* リモートや別ファイルにある `$ref` 参照には対応していません。