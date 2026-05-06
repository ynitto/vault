---
title: "PuppeteerのwaitForNavigationで正しくページ遷移を待つ"
type: "topic"
tags:
  - "meganii"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/PuppeteerのwaitForNavigationで正しくページ遷移を待つ.md"
summary: "Puppeteerにおける`page.waitForNavigation()`の正しい使い方を解説しています。ページ遷移を待つ際、クリック後に単独で呼び出…"
---

# PuppeteerのwaitForNavigationで正しくページ遷移を待つ

## 概要

Puppeteerにおける`page.waitForNavigation()`の正しい使い方を解説しています。ページ遷移を待つ際、クリック後に単独で呼び出すとタイムアウトエラーが発生するため、`Promise.all`を使用してクリックと同時に待機を開始するのが正しい実装です。

*発行: 2020-01-30T07:11:59Z0900 / [[meganii-puppeteer-waitfornavigation-https-www-meganii-com-blog-2020-01-3-9b23af]]*

## 主要なトピック

- [[meganii]]

## 詳細

- Puppeteerにおける`page.waitForNavigation()`の正しい使い方を解説しています。ページ遷移を待つ際、クリック後に単独で呼び出すとタイムアウトエラーが発生するため、`Promise.all`を使用してクリックと同時に待機を開始するのが正しい実装です。
- 要点
- **NGパターン**: `await click()`の後に`await waitForNavigation()`を記述すること。すでに遷移が終わっているためタイムアウトする。
- **OKパターン**: `Promise.all([page.waitForNavigation(), page.click()])`のように、クリックと待機を並列処理する。
- **理由**: `waitForNavigation`は呼び出し後の遷移イベントを監視するため、同時実行が必要。

*発行: 2020-01-30T07:11:59Z0900 / [[meganii-puppeteer-waitfornavigation-https-www-meganii-com-blog-2020-01-3-9b23af]]*

## 関連テーマ

- [[meganii]]

## 出典

- `60_Resources/PuppeteerのwaitForNavigationで正しくページ遷移を待つ.md`
- https://www.meganii.com/blog/2020/01/30/puppeteer-wait-for-navigation/
