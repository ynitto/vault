---
title: "Question regarding rampusers and constantusers"
source: "https://community.gatling.io/t/question-regarding-rampusers-and-constantusers/7486/3"
author:
  - "[[saxenaj]]"
published: 2023-01-04
created: 2026-04-30
description: "I am new to Gatling as well as performance testing and got confused about the rampUsersPerSec and contantUsersPerSec. Can someone pls valida"
tags:
  - "clippings"
---
### Gatlingのユーザー注入プロファイルに関する要約

Gatlingコミュニティにおける、`constantUsersPerSec`と`rampUsersPerSec`の挙動に関する質問とその回答のまとめです。

#### 主要なポイント
- **ユーザー数とリクエスト数の混同に注意**
  - これらの設定は「秒間あたりのリクエスト数」ではなく「**秒間あたりのユーザー開始数**」を定義します。
  - シナリオが1つのリクエストのみで構成されている場合を除き、ユーザー数とリクエスト数は一致しません。

- **設定の解説**
  - `constantUsersPerSec(10).during(20)`: 20秒間、毎秒10ユーザーを生成（合計200ユーザー）。
  - `rampUsersPerSec(5).to(10).during(20)`: 20秒かけて毎秒5ユーザーから10ユーザーまで線形に加速（合計150ユーザー）。

- **テストの目的（用語の訂正）**
  - 長時間の高負荷テスト（リソースリーク確認）は「ソークテスト（Soak Test）」ですが、段階的に負荷を上げるテストは「キャパシティテスト」と呼ぶのが適切です。

- **アドバイス**
  - 実際の負荷挙動を把握するには、単純なシミュレーションを実行し、生成されたレポートを確認することが推奨されます。
