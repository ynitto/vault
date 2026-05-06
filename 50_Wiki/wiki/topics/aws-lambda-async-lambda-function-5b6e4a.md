---
title: "Async Lambda Function Retries with Backoff and Jitter"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "serverless"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Async Lambda Function Retries with Backoff and Jitter.md"
summary: "AWS Lambdaの標準機能では不十分な非同期処理の再試行回数（最大2回）を補うため、SQSの可視性タイムアウトを利用して最大24時間の指数バックオフと…"
---

# Async Lambda Function Retries with Backoff and Jitter

## 概要

AWS Lambdaの標準機能では不十分な非同期処理の再試行回数（最大2回）を補うため、SQSの可視性タイムアウトを利用して最大24時間の指数バックオフとジッター付き再試行を実現する手法を解説した記事です。

*発行: 2022-02-07 / [[aws-lambda-async-lambda-function-5b6e4a]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[serverless]]

## 詳細

- AWS Lambdaの標準機能では不十分な非同期処理の再試行回数（最大2回）を補うため、SQSの可視性タイムアウトを利用して最大24時間の指数バックオフとジッター付き再試行を実現する手法を解説した記事です。
- 要点
- **背景と課題**
- Lambdaの標準的な非同期再試行は最大2回までであり、外部システムの長時間停止に対応できない。
- 指数バックオフとジッターを組み合わせることで、システムの負荷を分散しつつ成功率を高める必要がある。
- **解決策の仕組み**
- **SQSの活用**: 失敗したメッセージをSQSキューに送り、再試行ハンドラーを通じて可視性タイムアウト（最大12時間）を調整しながら再試行を繰り返す。
- **再試行エンベロープ**: 元のデータに試行回数などのメタデータを付与し、ハンドラーが正しいバックオフ時間を計算できるようにする。
- **主要機能**

*発行: 2022-02-07 / [[aws-lambda-async-lambda-function-5b6e4a]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[serverless]]

## 出典

- `60_Resources/Async Lambda Function Retries with Backoff and Jitter.md`
- https://lucvandonkersgoed.com/2022/02/07/async-lambda-function-retries-with-backoff-and-jitter/
