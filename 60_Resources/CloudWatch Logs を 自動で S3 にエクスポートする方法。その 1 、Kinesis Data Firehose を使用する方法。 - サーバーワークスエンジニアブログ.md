---
title: "CloudWatch Logs を \"自動で\" S3 にエクスポートする方法。その 1 、Kinesis Data Firehose を使用する方法。 - サーバーワークスエンジニアブログ"
source: "https://blog.serverworks.co.jp/cloudwatch_logs-s3-kinesis_data_firehose"
author:
  - "[[swx-yamamoto]]"
  - "[[(記事一覧)]]"
published: 2023-12-14
created: 2026-04-30
description: "こんにちは😺 技術課の山本です。 1. Kinesis Data Firehose を使用する方法 Kinesis Data Firehose のストリームを作成 CloudWatch Logs に付与する IAM ロールの作成 CloudWatch Logs のサブスクリプションフィルターを作成 確認 料金面 まとめ 余談 前回、AWS マネジメントコンソールを使って、CloudWatch Logs を手動で S3 にエクスポートするブログを書きました。 CloudWatch Logs を AWS マネジメントコンソールから手動で S3 バケットにエクスポートする - サーバーワークスエンジ…"
tags:
  - "clippings"
---
### CloudWatch LogsをS3へ自動エクスポートする方法（Kinesis Data Firehose編）

本記事は、CloudWatch LogsのログをKinesis Data Firehose経由で自動的にS3へ転送・保存する手法についての解説です。

#### 重要なポイント
*   **実現方法**: CloudWatch Logsの「サブスクリプションフィルター」を使用し、Kinesis Data Firehose経由でS3バケットへ配信する。
*   **データ形式**: ログはgzip形式で圧縮されてS3に保存されます。
*   **用途**: リアルタイム性が求められる分析や配信に適しています。
*   **コスト面での注意**: 
    *   Kinesis Data Firehoseの使用料金が発生するため、単純な「ストレージ料金の削減」には不向きです。
    *   長期的な保管コスト削減が目的であれば、他の手法を検討する必要があります。
*   **設定のヒント**: 
    *   配信ストリーム作成時にIAMロールを適切に設定する必要があります。
    *   サブスクリプションフィルター経由のログは複数行が1行にまとまるため、視認性には注意が必要です。
