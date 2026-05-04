---
title: "CloudWatch LogsのログデータをKinesis Data Firehose経由でS3に出力する"
source: "https://dev.classmethod.jp/articles/cloudwatch-logs-to-s3-via-kinesis-data-firehose/"
author:
  - "[[坂巻一義]]"
published: 2020-05-10
created: 2026-04-30
description: "CloudWatch Logsのデータを、Kinesis Data Firehose経由でS3に出力する手順です。"
tags:
  - "clippings"
---
### 概要
Lambdaなどのコード実装を行わず、AWS CLIを用いてCloudWatch LogsのデータをKinesis Data Firehose経由でS3へ自動出力する構築手順を解説した記事です。

### 要点まとめ
- **目的**: CloudWatch LogsのログをS3へ安価かつ簡単にエクスポートする。
- **構成要素**:
  - **CloudWatch Logs**: ログの出力元。
  - **Kinesis Data Firehose**: ログの配信・保存先S3への転送を行う中継サービス。
  - **IAMロール**: 各サービス間で適切な権限（S3操作権限やFirehose引き受け権限など）を定義。
- **重要ポイント**:
  - CloudWatch LogsからFirehoseへの出力には「サブスクリプションフィルタ」の設定が不可欠。
  - サブスクリプションフィルタの設定はマネジメントコンソール非対応のため、AWS CLI（`put-subscription-filter`）の使用が必要。
  - 配信エラー発生時は、CloudWatch Logsの特定ロググループに詳細が出力されるよう設計することで監視が可能。
  - 構築作業の再現性を高めるためのCloudFormationテンプレートも提示。
