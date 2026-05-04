---
title: "リアル調査案件で使ったPuppeteer"
type: "topic"
tags:
  - "ovrmrw"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/リアル調査案件で使ったPuppeteer.md"
summary: "この記事は、計測タグの発火タイミング調査という反復的で困難な手動業務を、Puppeteerを用いて自動化し解決した実体験の記録です。"
---

# リアル調査案件で使ったPuppeteer

## 概要

この記事は、計測タグの発火タイミング調査という反復的で困難な手動業務を、Puppeteerを用いて自動化し解決した実体験の記録です。

*発行: 2018-05-22 / [[ovrmrw-puppeteer-https-qiita-com-ovrmrw-items-9de343f36f6d5e14ba80-72-dda7ba]]*

## 主要なトピック

- [[ovrmrw]]

## 詳細

- この記事は、計測タグの発火タイミング調査という反復的で困難な手動業務を、Puppeteerを用いて自動化し解決した実体験の記録です。
- 自動化のポイント
- **調査背景**: 72パターン×10回という膨大な計測が必要な「地味な地獄」を自動化で効率化。
- **環境再現**: `headless: false` や `devtools: true` を利用し、手動操作に近いブラウザ環境を再現。
- **通信制御**: `Network.emulateNetworkConditions` で通信速度を制限し、環境の揺らぎを抑制。
- **計測手法**:
- `performance.timing` を用いたイベントタイミングの取得。
- `request`/`response` イベントの監視とログ記録。
- `RxJS` を活用したネットワーク通信の完了待機処理。

*発行: 2018-05-22 / [[ovrmrw-puppeteer-https-qiita-com-ovrmrw-items-9de343f36f6d5e14ba80-72-dda7ba]]*

## 関連テーマ

- [[ovrmrw]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/リアル調査案件で使ったPuppeteer.md`
- https://qiita.com/ovrmrw/items/9de343f36f6d5e14ba80
