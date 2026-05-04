---
title: "AWS Lambda：API GatewayとApplication Load Balancerの違い"
source: "https://qiita.com/unhurried/items/5a497ec81e4fefe22396"
author:
  - "[[ohtsuka1317]]"
published: 2019-08-07
created: 2026-05-01
description: "AWS Lambdaを使ってサーバーレスでWeb APIを作る場合、Lambdaの呼び出し元としてAPI Gateway (API GW) もしくはApplication Load Balancer (ALB) のどちらかを選択することになる。この選択基準となる両者の違いを..."
tags:
  - "clippings"
---
### 概要
AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (ALB)」の主な違いを比較・解説した記事です。

### 比較のポイント
- **API Gatewayの特性**
  - リクエスト検証、データマッピング、SDK生成などの豊富な独自機能がある。
  - HTTPS (443番ポート) のみに対応。
  - タイムアウトは最大29秒まで。
  - 実行回数ベースの課金（少〜中規模リクエストで有利）。

- **ALBの特性**
  - 任意のポートやプロトコル設定が可能。
  - タイムアウトはLambdaの最大制限（15分）まで対応可能。
  - 大規模なリクエスト処理ではコスト効率が良い。
  - リクエスト/レスポンスサイズは最大1MBに制限される。

- **技術的差異（Eventフォーマット）**
  - ヘッダー名やクエリストリングのデコード状態、マルチバリュー対応などに仕様の違いがあるため、Lambdaの実装時に注意が必要。