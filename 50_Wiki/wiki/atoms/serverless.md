---
title: "Serverless"
type: "concept"
tags:
  - "serverless"
  - "architecture"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ALB と Lambda のリクエストサイズの最大値.md"
  - "60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md"
  - "60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md"
  - "60_Resources/API GatewayでKinesis Data Firehoseのプロキシを作成する.md"
  - "60_Resources/AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める.md"
  - "60_Resources/AWS側がしてきたECS  Fargate のスケーリング速度改善の話.md"
  - "60_Resources/Async Lambda Function Retries with Backoff and Jitter.md"
  - "60_Resources/CloudWatch Logs と S3 にかかる料金比較.md"
  - "60_Resources/MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）.md"
  - "60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md"
  - "60_Resources/ついにAPI Gatewayの統合タイムアウトが29秒の壁を超えられるように！実際に延長リクエストしてみた.md"
summary: "サーバレス設計の要点を整理するページ。"
---

# Serverless

## 概要











Serverless は運用負荷を減らしつつ、イベント駆動で機能を構成するための設計スタイル。











## 詳細

- [[aws-lambda-alb-lambda-https-179a86]]: AWS LambdaとApplication Load Balancer（ALB）を連携させる際の、リクエストペイロード制限に関する技術情報のまとめです。
*発行: 2021-01-15 / [[aws-lambda-alb-lambda-https-179a86]]*
- [[aws-lambda-api-gateway-amazon-8c3dca]]: API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法についての解説記事です。
*発行: 2024-06-11 / [[aws-lambda-api-gateway-amazon-8c3dca]]*
- [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]: API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとCloudFrontのカスタムヘ…
*発行: 2022-06-13T00:00:00Z / [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]*
- [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]: 本記事では、API Gatewayをプロキシとして利用し、受信したデータをKinesis Data Firehose経由でS3バケットへ自動的に保存する構築手順を紹介しています。
*発行: 2023-04-10 / [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]*
- [[aws-lambda-aws-lambda-https-8a37a1]]: 本記事は、2019年末に発表されたAWS Lambdaの非同期呼び出しに関する新機能（結果の出力先指定とリトライ設定）を検証したレポートです。
*発行: 2020-01-21 / [[aws-lambda-aws-lambda-https-8a37a1]]*
- [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]: 本記事は、2022年までにAWSが実施したAmazon ECSおよびAWS Fargateにおけるコンテナスケーリング速度の劇的な改善について解説しています。
*発行: 2022-12-12 / [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]*
- [[aws-lambda-async-lambda-function-5b6e4a]]: AWS Lambdaの標準機能では不十分な非同期処理の再試行回数（最大2回）を補うため、SQSの可視性タイムアウトを利用して最大24時間の指数バックオフとジッター付き再試行を実現…
*発行: 2022-02-07 / [[aws-lambda-async-lambda-function-5b6e4a]]*
- [[lambda-cloudwatch-cloudwatch-logs-s3-e49c85]]: CloudWatch LogsとS3の料金比較と、コスト最適化の考え方をまとめた記事です。
*発行: 2024-05-26 / [[lambda-cloudwatch-cloudwatch-logs-s3-e49c85]]*
- [[aws-lambda-moto-lambda-docker-28ff00]]: Motoを使用して、Lambda関数から別のLambda関数をboto3経由で呼び出す処理をテストする方法を解説しています。Dockerを使用しない軽量なテスト構成に焦点を当てて…
*発行: 2025-02-05 / [[aws-lambda-moto-lambda-docker-28ff00]]*
- [[lambda-networking-vpc-lambda-invoke-ec6acf]]: VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技術解説記事です。
*発行: 2022-11-15 / [[lambda-networking-vpc-lambda-invoke-ec6acf]]*
- [[aws-api-gateway-api-gateway-29-011e61]]: API Gateway 統合タイムアウト延長の概要
  *発行: 2024-06-14 / [[aws-api-gateway-api-gateway-29-011e61]]*

## 関連

- [[aws-lambda-alb-lambda-https-179a86]]
- [[lambda]]
- [[api-gateway]]
- [[aws]]
- [[aws-lambda-api-gateway-amazon-8c3dca]]
- [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]
- [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]
- [[aws-lambda-aws-lambda-https-8a37a1]]
- [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]
- [[aws-lambda-async-lambda-function-5b6e4a]]

## 出典

- `60_Resources/ALB と Lambda のリクエストサイズの最大値.md`
- https://yohei-a.hatenablog.jp/entry/20210115/1610705961
- `60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md`
- https://tech.every.tv/entry/20240611
- `60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md`
- https://zatoima.github.io/aws-api-gateway-cloudfront-restrict-resource-policy/
- `60_Resources/API GatewayでKinesis Data Firehoseのプロキシを作成する.md`
- https://techblog.techfirm.co.jp/entry/create-kinesis-firehose-proxy-with-api-gateway
- `60_Resources/AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める.md`
- https://qiita.com/horit0123/items/295f8dc55d8c07e6512a
- `60_Resources/AWS側がしてきたECS  Fargate のスケーリング速度改善の話.md`
- https://qiita.com/yoshii0110/items/cbbfe797845dfa7e181d
- `60_Resources/Async Lambda Function Retries with Backoff and Jitter.md`
- https://lucvandonkersgoed.com/2022/02/07/async-lambda-function-retries-with-backoff-and-jitter/
- `60_Resources/CloudWatch Logs と S3 にかかる料金比較.md`
- https://dev.classmethod.jp/articles/comparison-of-fees-for-cloudwatch-logs-and-s3/
- `60_Resources/MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）.md`
- https://zenn.dev/ncdc/articles/eaa3d113c27f28
- `60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md`
- https://qiita.com/hirai-11/items/f16b326061956fb85c9c
- `60_Resources/ついにAPI Gatewayの統合タイムアウトが29秒の壁を超えられるように！実際に延長リクエストしてみた.md`
- https://qiita.com/shimagaji/items/4fa220ea0215a04704b6
