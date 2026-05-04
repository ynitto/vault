---
title: "puppeteerのpage.evaluate内でのlogをサーバーに出力する"
type: "topic"
tags:
  - "javascript"
  - "node-js"
  - "joryulife"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/puppeteerのpage.evaluate内でのlogをサーバーに出力する.md"
summary: "Puppeteerのデバッグログをサーバーに出力する方法"
---

# puppeteerのpage.evaluate内でのlogをサーバーに出力する

## 概要

Puppeteerのデバッグログをサーバーに出力する方法

*発行: 2023-01-10 / [[javascript-node-js-puppeteer-page-evaluate-log-35a449]]*

## 主要なトピック

- [[javascript]]
- [[node-js]]
- [[joryulife]]

## 詳細

- Puppeteerの `page.evaluate()` 内で実行した `console.log` は、通常ブラウザ側（Chromeのコンソール）にしか表示されません。これをNode.jsサーバー側のコンソールに出力するための解決策は以下の通りです。
- 解決策
- `puppeteer.launch()` でブラウザを起動する際、オプションに **`dumpio: true`** を指定します。
- ```javascript
- const browser = await puppeteer.launch({
- headless: true,
- dumpio: true, // ブラウザの出力をNode.jsプロセスに転送
- args: ['--lang=ja']
- });

*発行: 2023-01-10 / [[javascript-node-js-puppeteer-page-evaluate-log-35a449]]*

## 関連テーマ

- [[javascript]]
- [[node-js]]
- [[joryulife]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/puppeteerのpage.evaluate内でのlogをサーバーに出力する.md`
- https://qiita.com/joryulife/items/ce2af4fc50e0e2557958
