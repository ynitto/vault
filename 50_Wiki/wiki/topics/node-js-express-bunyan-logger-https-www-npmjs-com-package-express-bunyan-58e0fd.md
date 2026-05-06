---
title: "express-bunyan-logger"
type: "topic"
tags:
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/express-bunyan-logger.md"
summary: "`express-bunyan-logger` は、Node.jsのログライブラリ「Bunyan」を利用した、Express用ロギングミドルウェアです。"
---

# express-bunyan-logger

## 概要

`express-bunyan-logger` は、Node.jsのログライブラリ「Bunyan」を利用した、Express用ロギングミドルウェアです。

*発行: 2018-03-24 / [[node-js-express-bunyan-logger-https-www-npmjs-com-package-express-bunyan-58e0fd]]*

## 主要なトピック

- [[node-js]]

## 詳細

- `express-bunyan-logger` は、Node.jsのログライブラリ「Bunyan」を利用した、Express用ロギングミドルウェアです。
- 主な特徴・機能
- **リクエストロギング**: リクエストおよびエラーログを自動生成。
- **柔軟な設定**: ログフォーマットのカスタマイズ、ログレベルの動的制御（`levelFn`）、情報の付加（`includesFn`）が可能。
- **セキュリティ対応**: `obfuscate`機能により、パスワードなどの機密情報をログから隠蔽可能。
- **リクエストID**: リクエストごとにユニークなIDを自動付与または外部から連携可能。
- **子ロガー**: 各リクエストオブジェクトに子ロガー（`req.log`）を自動付与し、手動でのログ出力も容易。
- 導入方法
- ```bash

*発行: 2018-03-24 / [[node-js-express-bunyan-logger-https-www-npmjs-com-package-express-bunyan-58e0fd]]*

## 関連テーマ

- [[node-js]]

## 出典

- `../60_Resources/express-bunyan-logger.md`
- https://www.npmjs.com/package/express-bunyan-logger
