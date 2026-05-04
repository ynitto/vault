---
title: "node-html-parser"
source: "https://www.npmjs.com/package/node-html-parser"
author:
published: 2026-03-03
created: 2026-05-01
description: "A very fast HTML parser, generating a simplified DOM, with basic element query support.. Latest version: 7.1.0, last published: 2 months ago. Start using node-html-parser in your project by running `npm i node-html-parser`. There are 1969 other projects in the npm registry using node-html-parser."
tags:
  - "clippings"
---
### node-html-parser 概要
`node-html-parser` は、パフォーマンスを最優先に設計された非常に高速なHTMLパーサーです。簡略化されたDOMツリーを生成し、CSSセレクタによる要素の抽出をサポートしています。

### 主な特徴
- **超高速性能**: 大規模なHTMLファイルの解析に適しています。
- **CSSクエリサポート**: `querySelector` や `querySelectorAll` 等による柔軟な要素選択が可能。
- **実用的な解析**: 多少のHTMLの不備（閉じタグ漏れなど）を許容して解析します。
- **TypeScript対応**: 型定義が組み込まれています。

### インストール
```bash
npm install --save node-html-parser
```

### 主な機能・メソッド
- **解析 (parse)**: HTML文字列からDOMツリーを構築。
- **DOM操作**: `appendChild`, `removeChild`, `setAttribute`, `set_content` など、ブラウザ標準に近い操作メソッドを提供。
- **クエリ**: CSSセレクタを用いた要素検索および走査。
- **プロパティ**: `text`, `innerHTML`, `outerHTML`, `attributes` などで内容や属性にアクセス可能。

### 注意点
- パフォーマンス重視のため、厳密なHTML5の仕様準拠よりは速度を優先しています。
- ルートノードに対して `set_content` を使用することは非推奨です。