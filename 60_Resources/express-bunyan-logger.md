---
title: "express-bunyan-logger"
source: "https://www.npmjs.com/package/express-bunyan-logger"
author:
published: 2018-03-24
created: 2026-05-01
description: "a bunyan logger middleware for express. Latest version: 1.3.3, last published: 8 years ago. Start using express-bunyan-logger in your project by running `npm i express-bunyan-logger`. There are 81 other projects in the npm registry using express-bunyan-logger."
tags:
  - "clippings"
---
### 概要
`express-bunyan-logger` は、Node.jsのログライブラリ「Bunyan」を利用した、Express用ロギングミドルウェアです。

### 主な特徴・機能
- **リクエストロギング**: リクエストおよびエラーログを自動生成。
- **柔軟な設定**: ログフォーマットのカスタマイズ、ログレベルの動的制御（`levelFn`）、情報の付加（`includesFn`）が可能。
- **セキュリティ対応**: `obfuscate`機能により、パスワードなどの機密情報をログから隠蔽可能。
- **リクエストID**: リクエストごとにユニークなIDを自動付与または外部から連携可能。
- **子ロガー**: 各リクエストオブジェクトに子ロガー（`req.log`）を自動付与し、手動でのログ出力も容易。

### 導入方法
```bash
npm install express-bunyan-logger
```

### 注意点
- 本パッケージは8年以上更新されておらず、現在メンテナンスが停滞しています。
