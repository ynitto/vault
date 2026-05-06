---
title: "API GatewayでKinesis Data Firehoseのプロキシを作成する"
type: "topic"
tags:
  - "api-gateway"
  - "serverless"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/API GatewayでKinesis Data Firehoseのプロキシを作成する.md"
summary: "本記事では、API Gatewayをプロキシとして利用し、受信したデータをKinesis Data Firehose経由でS3バケットへ自動的に保存する構…"
---

# API GatewayでKinesis Data Firehoseのプロキシを作成する

## 概要

本記事では、API Gatewayをプロキシとして利用し、受信したデータをKinesis Data Firehose経由でS3バケットへ自動的に保存する構築手順を紹介しています。

*発行: 2023-04-10 / [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]*

## 主要なトピック

- [[api-gateway]]
- [[serverless]]

## 詳細

- 本記事では、API Gatewayをプロキシとして利用し、受信したデータをKinesis Data Firehose経由でS3バケットへ自動的に保存する構築手順を紹介しています。
- 構築のポイント
- **目的**: センサーデータ等の定期的な収集・保存。
- **メリット**: リアルタイム性が不要な場合、Kinesis Data Streamsを使用するよりも低コストかつ簡単にS3連携が実現可能。
- **主要な設定内容**:
- **S3**: 送信先バケットの準備。
- **Firehose**: デフォルト設定で配信ストリームを作成。
- **IAM**: API GatewayがFirehoseへアクセスできるよう許可ポリシーを追加。
- **API Gateway**: `POST`メソッドを作成し、マッピングテンプレートを用いて入力データをFirehoseの`PutRecord`形式へ変換。

*発行: 2023-04-10 / [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]*

## 関連テーマ

- [[api-gateway]]
- [[serverless]]

## 出典

- `../60_Resources/API GatewayでKinesis Data Firehoseのプロキシを作成する.md`
- https://techblog.techfirm.co.jp/entry/create-kinesis-firehose-proxy-with-api-gateway
