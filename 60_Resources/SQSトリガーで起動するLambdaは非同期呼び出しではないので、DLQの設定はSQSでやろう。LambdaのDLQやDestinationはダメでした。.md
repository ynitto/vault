---
title: "SQSトリガーで起動するLambdaは非同期呼び出しではないので、DLQの設定はSQSでやろう。LambdaのDLQやDestinationはダメでした。"
source: "https://dev.classmethod.jp/articles/sqs-trigger-lambda-dlq-setting/"
author:
  - "[[藤井元貴]]"
published: 2021-06-29
created: 2026-05-01
description: "SQSトリガーで動作するLambdaは、非同期呼び出しではありません。DLQを使いたい場合は、SQSのDLQを使いましょう。"
tags:
  - "clippings"
---
### 記事の要約
SQSトリガーで起動するLambda関数では、Lambda側で設定する「デッドレターキュー(DLQ)」や「Destination」が機能しないという仕様上の注意点と、その正しい実装方法（SQS側でのDLQ設定）を解説しています。

### 要点まとめ
- **結論**: SQSトリガーのLambdaは「非同期呼び出し」ではないため、LambdaのDLQ設定は無視される。
- **課題**: エラー発生時にLambdaの再試行設定やDLQが機能せず、SQS内にメッセージが残り続ける。
- **解決策**: SQS側の`RedrivePolicy`を使用して、SQSレベルでDLQを設定する必要がある。
- **実装のヒント**: 
    - AWS SAMを利用する場合、`AWS::SQS::Queue`リソースのプロパティとして`RedrivePolicy`を定義する。
    - 処理に失敗したメッセージはSQSのDLQへ移動し、そこから別処理（別のLambdaなど）へ連携することが可能。