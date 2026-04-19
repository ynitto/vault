---
title: "API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す"
source: "https://tech.every.tv/entry/20240611"
author:
  - "[[bnpb]]"
published: 2024-06-11
created: 2026-04-19
description: "この記事は every Tech Blog Advent Calendar 2024(夏) 11 日目の記事です。 エブリーで小売業界向き合いの開発を行っている @kosukeohmura といいます。 エブリーでは retail HUB という小売業界向けのサービスを展開しており、その開発を行う中でイベントログを収集する API を作る機会がありました。この記事ではその中でも表題の点にフォーカスして詳細をお伝えできればと思います。 イベントログを収集する API の概観 クライアントからのイベントログを API Gateway で作成した API で受け、Amazon Data Fireho…"
tags:
  - "clippings"
---
### 記事の要約
API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法についての解説記事です。

### 要点まとめ
- **解決した課題**
  - Lambdaを挟むと、コード管理、実行設定、ロール管理、コスト、ランタイム運用などの運用負荷が増加するため、これらを回避したかった。

- **採用した手法**
  - API Gatewayの「マッピングテンプレート（VTL）」を活用し、リクエストボディをFirehoseの`PutRecordBatch` APIが要求する形式（Base64エンコード済みデータを含む構造）に変換。

- **実装のポイント**
  - **メタデータ付加**: サーバー時刻、送信元IP、User-Agent、リクエストIDなどをVTLで付加。
  - **データ変換**: JSON配列をループ処理し、各要素をBase64変換して`PutRecordBatch`のJSON構造に整形。

- **検討事項と教訓**
  - **メリット**: Lambdaの運用コスト削減と処理のシンプル化。
  - **デメリット**: VTLのデバッグが難しく、複雑な変換には不向き。
  - **判断基準**: 変換処理がシンプルならマッピングテンプレート、複雑ならLambdaを検討すべき。