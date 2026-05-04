---
title: "waitForNavigation doesn't work after evaluate fetch() or XMLHttpRequest() · Issue #1466 · puppeteer/puppeteer"
source: "https://github.com/puppeteer/puppeteer/issues/1466"
author:
  - "[[ghost]]"
published: 2017-11-24
created: 2026-05-01
description: "Puppeteer version: 0.13.0 Platform / OS version: Win10x64 / Chromium 64.0.3264.0 const puppeteer = require('puppeteer'); (async() => { const"
tags:
  - "clippings"
---
### 概要
Puppeteerにおいて、`page.evaluate()`内で実行された`fetch`や`XMLHttpRequest`（非同期通信）の完了を`page.waitForNavigation()`で待機できないという問題に関する議論です。

### 要点
- **原因**: `waitForNavigation`はURL遷移などのメインフレームのナビゲーションを待機するためのものであり、ページ内での非同期リクエストには反応しない。
- **解決策**: 
    - **`waitForSelector`や`waitForFunction`**: 非同期通信の結果としてDOMが変化する場合に有効。
    - **ネットワークイベントの監視**: `request`や`requestfinished`イベントを使用して通信の完了を独自にフックする。
    - **実装のコツ**: 通信が複数発生する場合、タイムアウトを伴う再帰的な待機関数を作成し、イベントリスナーには`.once()`を使用するのが推奨される。
