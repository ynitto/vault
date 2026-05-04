---
title: "puppeteerでproxyを利用する方法"
source: "https://kagasu.hatenablog.com/entry/2022/01/22/023324"
author:
  - "[[kagasu]]"
published: 2022-01-22
created: 2026-05-01
description: "Ⅰ. はじめに Ⅱ. 方法1（起動引数を設定する） 手順 1. サンプルプログラムを書く 実行結果 Ⅲ. 方法2（ライブラリを利用する方法） 手順 1. 必要なライブラリをインストールする 2. サンプルプログラムを書く 実行結果 参考 Ⅰ. はじめに タイトルの通り「puppeteerでproxyを利用する方法」です…"
tags:
  - "clippings"
---
### Puppeteerでプロキシを設定する方法の要約
Puppeteerを使用してブラウザ通信にプロキシを通すための2つの主要なアプローチを解説しています。

#### 要点
* **方法1：起動引数の設定**
    * `puppeteer.launch` の `args` オプションで `--proxy-server=IP:PORT` を指定する。
    * **制約:** 認証不要のHTTPプロキシのみ対応。

* **方法2：ライブラリを利用する方法**
    * `puppeteer-proxy` と各種エージェントライブラリ（`https-proxy-agent` や `socks-proxy-agent`）を併用する。
    * `page.setRequestInterception(true)` を有効にし、リクエストをフックしてプロキシ経由で中継させる。
    * **利点:** 認証付きプロキシやSOCKS5プロキシにも対応可能。