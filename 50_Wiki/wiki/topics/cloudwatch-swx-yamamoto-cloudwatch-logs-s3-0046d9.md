---
title: "CloudWatch Logs を \"自動で\" S3 にエクスポートする方法。その 1 、Kinesis Data Firehose を使用する方法。 - サーバーワークスエンジニアブログ"
type: "topic"
tags:
  - "cloudwatch"
  - "swx-yamamoto"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/CloudWatch Logs を 自動で S3 にエクスポートする方法。その 1 、Kinesis Data Firehose を使用する方法。 - サーバーワークスエンジニアブログ.md"
summary: "CloudWatch LogsをS3へ自動エクスポートする方法（Kinesis Data Firehose編）"
---

# CloudWatch Logs を \"自動で\" S3 にエクスポートする方法。その 1 、Kinesis Data Firehose を使用する方法。 - サーバーワークスエンジニアブログ

## 概要

CloudWatch LogsをS3へ自動エクスポートする方法（Kinesis Data Firehose編）

*発行: 2023-12-14 / [[cloudwatch-swx-yamamoto-cloudwatch-logs-s3-0046d9]]*

## 主要なトピック

- [[cloudwatch]]
- [[swx-yamamoto]]

## 詳細

- 本記事は、CloudWatch LogsのログをKinesis Data Firehose経由で自動的にS3へ転送・保存する手法についての解説です。
- 重要なポイント
- **実現方法**: CloudWatch Logsの「サブスクリプションフィルター」を使用し、Kinesis Data Firehose経由でS3バケットへ配信する。
- **データ形式**: ログはgzip形式で圧縮されてS3に保存されます。
- **用途**: リアルタイム性が求められる分析や配信に適しています。
- **コスト面での注意**:
- Kinesis Data Firehoseの使用料金が発生するため、単純な「ストレージ料金の削減」には不向きです。
- 長期的な保管コスト削減が目的であれば、他の手法を検討する必要があります。
- **設定のヒント**:

*発行: 2023-12-14 / [[cloudwatch-swx-yamamoto-cloudwatch-logs-s3-0046d9]]*

## 関連テーマ

- [[cloudwatch]]
- [[swx-yamamoto]]

## 出典

- `60_Resources/CloudWatch Logs を 自動で S3 にエクスポートする方法。その 1 、Kinesis Data Firehose を使用する方法。 - サーバーワークスエンジニアブログ.md`
- https://blog.serverworks.co.jp/cloudwatch_logs-s3-kinesis_data_firehose
