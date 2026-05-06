---
title: "API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "api-gateway"
  - "serverless"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md"
summary: "API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法に…"
---

# API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す

## 概要

API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法についての解説記事です。

*発行: 2024-06-11 / [[aws-lambda-api-gateway-amazon-8c3dca]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[serverless]]

## 詳細

- API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法についての解説記事です。
- 要点まとめ
- **解決した課題**
- Lambdaを挟むと、コード管理、実行設定、ロール管理、コスト、ランタイム運用などの運用負荷が増加するため、これらを回避したかった。
- **採用した手法**
- API Gatewayの「マッピングテンプレート（VTL）」を活用し、リクエストボディをFirehoseの`PutRecordBatch` APIが要求する形式（Base64エンコード済みデータを含む構造）に変換。
- **実装のポイント**
- **メタデータ付加**: サーバー時刻、送信元IP、User-Agent、リクエストIDなどをVTLで付加。
- **データ変換**: JSON配列をループ処理し、各要素をBase64変換して`PutRecordBatch`のJSON構造に整形。

*発行: 2024-06-11 / [[aws-lambda-api-gateway-amazon-8c3dca]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[serverless]]

## 出典

- `60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md`
- https://tech.every.tv/entry/20240611
