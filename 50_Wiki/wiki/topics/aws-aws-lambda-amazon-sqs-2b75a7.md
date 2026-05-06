---
title: "[アップデート] AWS LambdaがAmazon SQSをイベントソースとしたバッチ処理で部分応答をサポートしました"
type: "topic"
tags:
  - "aws"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/アップデート AWS LambdaがAmazon SQSをイベントソースとしたバッチ処理で部分応答をサポートしました.md"
summary: "AWS LambdaのイベントソースとしてAmazon SQSを使用する際、バッチ処理中の「部分的な失敗（一部のメッセージのみ失敗）」を個別に処理できる新…"
---

# [アップデート] AWS LambdaがAmazon SQSをイベントソースとしたバッチ処理で部分応答をサポートしました

## 概要

AWS LambdaのイベントソースとしてAmazon SQSを使用する際、バッチ処理中の「部分的な失敗（一部のメッセージのみ失敗）」を個別に処理できる新機能の紹介です。

*発行: 2026-05-20 / [[aws-aws-lambda-amazon-sqs-2b75a7]]*

## 主要なトピック

- [[aws]]

## 詳細

- AWS LambdaのイベントソースとしてAmazon SQSを使用する際、バッチ処理中の「部分的な失敗（一部のメッセージのみ失敗）」を個別に処理できる新機能の紹介です。
- 要点
- **従来の課題**: バッチ処理で一部のメッセージが失敗しても、成功したものも含めてキュー全体が再試行対象になるか、個別に削除する実装が別途必要だった。
- **アップデート内容**: Lambdaが失敗したメッセージのIDのみを返却することで、失敗した分だけをキューに残し、成功分は正常に完了させることが可能になった。
- **設定のポイント**:
- Lambda関数のイベントソース設定で「バッチ項目の失敗を報告する（ReportBatchItemFailures）」を有効にする。
- **実装方法**:
- 関数側で `batchItemFailures` をキーとしたJSON形式で失敗したメッセージIDのリストを返却する。

*発行: 2026-05-20 / [[aws-aws-lambda-amazon-sqs-2b75a7]]*

## 関連テーマ

- [[aws]]

## 出典

- `../60_Resources/アップデート AWS LambdaがAmazon SQSをイベントソースとしたバッチ処理で部分応答をサポートしました.md`
- https://dev.classmethod.jp/articles/update-aws-lambda-partial-failures/
