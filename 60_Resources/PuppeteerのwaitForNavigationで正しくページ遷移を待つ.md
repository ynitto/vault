---
title: "PuppeteerのwaitForNavigationで正しくページ遷移を待つ"
source: "https://www.meganii.com/blog/2020/01/30/puppeteer-wait-for-navigation/"
author:
  - "[[meganii]]"
published: 2020-01-30T07:11:59Z0900
created: 2026-05-01
description: "「Puppeteer入門 スクレイピング+Web操作自動処理プログラミング」 を読むまで、PuppeteerのwaitForNavigationの動きを誤って理解していました。ここでは、Puppeteerを利用して「ページ遷移を待つ」というよくある処理における誤った実装と正しい実装を紹介します。"
tags:
  - "clippings"
---
### 要約
Puppeteerにおける`page.waitForNavigation()`の正しい使い方を解説しています。ページ遷移を待つ際、クリック後に単独で呼び出すとタイムアウトエラーが発生するため、`Promise.all`を使用してクリックと同時に待機を開始するのが正しい実装です。

### 要点
- **NGパターン**: `await click()`の後に`await waitForNavigation()`を記述すること。すでに遷移が終わっているためタイムアウトする。
- **OKパターン**: `Promise.all([page.waitForNavigation(), page.click()])`のように、クリックと待機を並列処理する。
- **理由**: `waitForNavigation`は呼び出し後の遷移イベントを監視するため、同時実行が必要。
