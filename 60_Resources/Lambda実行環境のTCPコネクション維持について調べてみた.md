---
title: "Lambda実行環境のTCPコネクション維持について調べてみた"
source: "https://dev.classmethod.jp/articles/lambda-tcp-keepalive/"
author:
  - "[[岩田智哉]]"
published: 2026-05-20
created: 2026-05-01
description: "tcpdumpでパケットキャプチャしながらLambda実行環境のTCPコネクション維持について思いを馳せてみました"
tags:
  - "clippings"
---
### Lambda実行環境におけるTCPコネクション維持の検証

Lambdaの実行環境が「フリーズ」している間、初期化処理で確立したDB接続が維持される仕組みについて、パケットキャプチャを用いて検証した結果の要約です。

#### 検証のポイント
- **TCPコネクションの維持:** Lambdaがフリーズ中であっても、AWS側のインフラがTCP KeepAliveパケットを適切に処理・応答している。
- **コネクションの終了:** Lambdaの実行環境が破棄されるタイミングで、適切にFIN/ACKを送信してコネクションがクローズされる。
- **双方向の応答性:** DB側からKeepAliveを送信した場合でも、Lambda側は正常にACKを返すことが確認された。

#### 結論
- Lambdaの初期化処理で確立した外部コネクションは、Lambdaの実行基盤（Worker/MicroVM）によって適切に管理・維持される。
- ユーザー側で特別なハンドリングを意識せずとも、プラットフォーム側が良い感じに接続を維持してくれる。