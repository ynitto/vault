---
title: "[アップデート] AWS LambdaがAmazon SQSをイベントソースとしたバッチ処理で部分応答をサポートしました"
source: "https://dev.classmethod.jp/articles/update-aws-lambda-partial-failures/"
author:
  - "[[武田隆志]]"
published: 2026-05-20
created: 2026-05-01
description: "Amazon SQSをイベントソースとしたLambda関数のバッチ処理において、一部の失敗したメッセージのIDを返すことで成功したメッセージは削除され失敗したメッセージはキューに残せるようになりました。"
tags:
  - "clippings"
---
### 概要
AWS LambdaのイベントソースとしてAmazon SQSを使用する際、バッチ処理中の「部分的な失敗（一部のメッセージのみ失敗）」を個別に処理できる新機能の紹介です。

### 要点
- **従来の課題**: バッチ処理で一部のメッセージが失敗しても、成功したものも含めてキュー全体が再試行対象になるか、個別に削除する実装が別途必要だった。
- **アップデート内容**: Lambdaが失敗したメッセージのIDのみを返却することで、失敗した分だけをキューに残し、成功分は正常に完了させることが可能になった。
- **設定のポイント**: 
    - Lambda関数のイベントソース設定で「バッチ項目の失敗を報告する（ReportBatchItemFailures）」を有効にする。
- **実装方法**: 
    - 関数側で `batchItemFailures` をキーとしたJSON形式で失敗したメッセージIDのリストを返却する。