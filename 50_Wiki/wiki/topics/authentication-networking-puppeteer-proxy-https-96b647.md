---
title: "puppeteerでproxyを利用する方法"
type: "topic"
tags:
  - "authentication"
  - "networking"
  - "kagasu"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/puppeteerでproxyを利用する方法.md"
summary: "Puppeteerを使用してブラウザ通信にプロキシを通すための2つの主要なアプローチを解説しています。"
---

# puppeteerでproxyを利用する方法

## 概要

Puppeteerを使用してブラウザ通信にプロキシを通すための2つの主要なアプローチを解説しています。

*発行: 2022-01-22 / [[authentication-networking-puppeteer-proxy-https-96b647]]*

## 主要なトピック

- [[authentication]]
- [[networking]]
- [[kagasu]]

## 詳細

- Puppeteerを使用してブラウザ通信にプロキシを通すための2つの主要なアプローチを解説しています。
- 要点
- **方法1：起動引数の設定**
- `puppeteer.launch` の `args` オプションで `--proxy-server=IP:PORT` を指定する。
- **制約:** 認証不要のHTTPプロキシのみ対応。
- **方法2：ライブラリを利用する方法**
- `puppeteer-proxy` と各種エージェントライブラリ（`https-proxy-agent` や `socks-proxy-agent`）を併用する。
- `page.setRequestInterception(true)` を有効にし、リクエストをフックしてプロキシ経由で中継させる。
- **利点:** 認証付きプロキシやSOCKS5プロキシにも対応可能。

*発行: 2022-01-22 / [[authentication-networking-puppeteer-proxy-https-96b647]]*

## 関連テーマ

- [[authentication]]
- [[networking]]
- [[kagasu]]

## 出典

- `60_Resources/puppeteerでproxyを利用する方法.md`
- https://kagasu.hatenablog.com/entry/2022/01/22/023324
