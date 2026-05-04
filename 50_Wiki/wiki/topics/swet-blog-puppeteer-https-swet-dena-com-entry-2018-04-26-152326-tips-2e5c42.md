---
title: "Puppeteerによるフルページスクリーンショットを画像遅延読み込みに対応させる"
type: "topic"
tags:
  - "swet-blog"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Puppeteerによるフルページスクリーンショットを画像遅延読み込みに対応させる.md"
summary: "PuppeteerによるフルページスクリーンショットのTips"
---

# Puppeteerによるフルページスクリーンショットを画像遅延読み込みに対応させる

## 概要

PuppeteerによるフルページスクリーンショットのTips

*発行: 2018-04-27 / [[swet-blog-puppeteer-https-swet-dena-com-entry-2018-04-26-152326-tips-2e5c42]]*

## 主要なトピック

- [[swet-blog]]

## 詳細

- Puppeteerを使用すると、ブラウザテストの一環としてウェブページ全体のスクリーンショットを簡潔に取得できます。
- 1. 基本的な実装
- `page.screenshot({ fullPage: true })` を使用することで、スクロールなしでページ全体のキャプチャが可能。
- Seleniumのように手動でスクロールして結合する手間が不要。
- 2. 画像遅延読み込みへの対策
- 遅延読み込みライブラリを使用しているページでは、読み込み前にキャプチャされるため、画像が欠ける問題が発生する。
- **回避策**: ページ全体を自動スクロールさせる関数を実装し、ページ下端まで移動させてコンテンツを全てロードさせてからキャプチャする。
- ページ内の `scrollHeight` が動的に変わる可能性があるため、ループ処理内で高さを再取得することが重要。
- 3. 注意点

*発行: 2018-04-27 / [[swet-blog-puppeteer-https-swet-dena-com-entry-2018-04-26-152326-tips-2e5c42]]*

## 関連テーマ

- [[swet-blog]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Puppeteerによるフルページスクリーンショットを画像遅延読み込みに対応させる.md`
- https://swet.dena.com/entry/2018/04/26/152326
