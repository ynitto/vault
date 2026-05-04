---
title: "リアル調査案件で使ったPuppeteer"
source: "https://qiita.com/ovrmrw/items/9de343f36f6d5e14ba80"
author:
  - "[[ovrmrw]]"
published: 2018-05-22
created: 2026-05-01
description: "Meguro.es #15 @ Drecom 2018年5月22日 自己紹介 ちきさん Twitter/GitHub/Qiita: @ovrmrw 市ヶ谷のオプトという会社で働いています。初心者です。 今回のGitHubリポジトリ 今日話すこと 実際に降..."
tags:
  - "clippings"
---
### 要約
この記事は、計測タグの発火タイミング調査という反復的で困難な手動業務を、Puppeteerを用いて自動化し解決した実体験の記録です。

### 自動化のポイント
- **調査背景**: 72パターン×10回という膨大な計測が必要な「地味な地獄」を自動化で効率化。
- **環境再現**: `headless: false` や `devtools: true` を利用し、手動操作に近いブラウザ環境を再現。
- **通信制御**: `Network.emulateNetworkConditions` で通信速度を制限し、環境の揺らぎを抑制。
- **計測手法**:
    - `performance.timing` を用いたイベントタイミングの取得。
    - `request`/`response` イベントの監視とログ記録。
    - `RxJS` を活用したネットワーク通信の完了待機処理。

### 結論
- PuppeteerはDevTools相当の調査・解析が可能な強力なツール。
- 手動操作と近い環境設定を行うことで、信頼性の高いデータ収集が可能。
- 複雑な非同期処理には `async/await` の活用が不可欠。
