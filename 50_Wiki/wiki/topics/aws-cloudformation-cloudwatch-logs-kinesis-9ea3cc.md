---
title: "CloudWatch LogsのログデータをKinesis Data Firehose経由でS3に出力する"
type: "topic"
tags:
  - "aws"
  - "cloudformation"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/CloudWatch LogsのログデータをKinesis Data Firehose経由でS3に出力する.md"
summary: "Lambdaなどのコード実装を行わず、AWS CLIを用いてCloudWatch LogsのデータをKinesis Data Firehose経由でS3へ…"
---

# CloudWatch LogsのログデータをKinesis Data Firehose経由でS3に出力する

## 概要

Lambdaなどのコード実装を行わず、AWS CLIを用いてCloudWatch LogsのデータをKinesis Data Firehose経由でS3へ自動出力する構築手順を解説した記事です。

*発行: 2020-05-10 / [[aws-cloudformation-cloudwatch-logs-kinesis-9ea3cc]]*

## 主要なトピック

- [[aws]]
- [[cloudformation]]
- [[cloudwatch]]

## 詳細

- Lambdaなどのコード実装を行わず、AWS CLIを用いてCloudWatch LogsのデータをKinesis Data Firehose経由でS3へ自動出力する構築手順を解説した記事です。
- 要点まとめ
- **目的**: CloudWatch LogsのログをS3へ安価かつ簡単にエクスポートする。
- **構成要素**:
- **CloudWatch Logs**: ログの出力元。
- **Kinesis Data Firehose**: ログの配信・保存先S3への転送を行う中継サービス。
- **IAMロール**: 各サービス間で適切な権限（S3操作権限やFirehose引き受け権限など）を定義。
- **重要ポイント**:
- CloudWatch LogsからFirehoseへの出力には「サブスクリプションフィルタ」の設定が不可欠。

*発行: 2020-05-10 / [[aws-cloudformation-cloudwatch-logs-kinesis-9ea3cc]]*

## 関連テーマ

- [[aws]]
- [[cloudformation]]
- [[cloudwatch]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/CloudWatch LogsのログデータをKinesis Data Firehose経由でS3に出力する.md`
- https://dev.classmethod.jp/articles/cloudwatch-logs-to-s3-via-kinesis-data-firehose/
