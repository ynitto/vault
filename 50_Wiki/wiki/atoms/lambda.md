---
title: "AWS Lambda"
type: "product"
tags:
  - "aws"
  - "lambda"
  - "serverless"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ALB と Lambda のリクエストサイズの最大値.md"
  - "60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md"
  - "60_Resources/AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める.md"
  - "60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md"
  - "60_Resources/AWS側がしてきたECS  Fargate のスケーリング速度改善の話.md"
  - "60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md"
  - "60_Resources/Async Lambda Function Retries with Backoff and Jitter.md"
  - "60_Resources/CloudWatch Logs と S3 にかかる料金比較.md"
  - "60_Resources/MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）.md"
  - "60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md"
  - "60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md"
  - "60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md"
  - "60_Resources/え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾.md"
  - "60_Resources/クォータ.md"
  - "60_Resources/推奨アラーム.md"
summary: "AWS のイベント駆動サーバレス実行基盤。"
---

# AWS Lambda

## 概要















AWS Lambda はイベントに応じてコードを実行するマネージドなコンピュートサービスで、API・非同期処理・自動化の要になる。















## 詳細

- [[aws-lambda-alb-lambda-https-179a86]]: AWS LambdaとApplication Load Balancer（ALB）を連携させる際の、リクエストペイロード制限に関する技術情報のまとめです。
*発行: 2021-01-15 / [[aws-lambda-alb-lambda-https-179a86]]*
- [[aws-lambda-api-gateway-amazon-8c3dca]]: API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法についての解説記事です。
*発行: 2024-06-11 / [[aws-lambda-api-gateway-amazon-8c3dca]]*
- [[aws-lambda-aws-lambda-https-8a37a1]]: 本記事は、2019年末に発表されたAWS Lambdaの非同期呼び出しに関する新機能（結果の出力先指定とリトライ設定）を検証したレポートです。
*発行: 2020-01-21 / [[aws-lambda-aws-lambda-https-8a37a1]]*
- [[aws-lambda-aws-lambda-api-cafc43]]: AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (ALB)」の主な違いを比較…
*発行: 2019-08-07 / [[aws-lambda-aws-lambda-api-cafc43]]*
- [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]: 本記事は、2022年までにAWSが実施したAmazon ECSおよびAWS Fargateにおけるコンテナスケーリング速度の劇的な改善について解説しています。
*発行: 2022-12-12 / [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]*
- [[aws-lambda-amazon-api-gateway-1339da]]: Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この問題を Lambda オ…
*発行: 2021-12-06 / [[aws-lambda-amazon-api-gateway-1339da]]*
- [[aws-lambda-async-lambda-function-5b6e4a]]: AWS Lambdaの標準機能では不十分な非同期処理の再試行回数（最大2回）を補うため、SQSの可視性タイムアウトを利用して最大24時間の指数バックオフとジッター付き再試行を実現…
*発行: 2022-02-07 / [[aws-lambda-async-lambda-function-5b6e4a]]*
- [[lambda-cloudwatch-cloudwatch-logs-s3-e49c85]]: CloudWatch LogsとS3の料金比較と、コスト最適化の考え方をまとめた記事です。
*発行: 2024-05-26 / [[lambda-cloudwatch-cloudwatch-logs-s3-e49c85]]*
- [[aws-lambda-moto-lambda-docker-28ff00]]: Motoを使用して、Lambda関数から別のLambda関数をboto3経由で呼び出す処理をテストする方法を解説しています。Dockerを使用しない軽量なテスト構成に焦点を当てて…
*発行: 2025-02-05 / [[aws-lambda-moto-lambda-docker-28ff00]]*
- [[aws-lambda-next-js-lambda-api-e4f04b]]: Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法についての解説記事です。
*発行: 2022-12-13 / [[aws-lambda-next-js-lambda-api-e4f04b]]*
- [[aws-lambda-rest-api-http-47b62c]]: Amazon API Gateway：REST API と HTTP API の比較要約
- [[lambda-networking-vpc-lambda-invoke-ec6acf]]: VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技術解説記事です。
*発行: 2022-11-15 / [[lambda-networking-vpc-lambda-invoke-ec6acf]]*
- [[aws-lambda-aws-5-3-d83259]]: AWSの各サービスを利用する際に、意図せず高額なコストが発生してしまうリスクと、その対策方法を理論値ベースで解説した記事です。
*発行: 2020-02-28 / [[aws-lambda-aws-5-3-d83259]]*
- [[aws-lambda-https-docs-aws-amazon-com-ja-jp-amazoncloudfront-latest-devel-ab9d59]]: 本ドキュメントは、Amazon CloudFrontにおける各種制限事項（クォータ）の一覧です。多くの項目はService QuotasやAWSサポートを通じて引き上げが可能です。
- [[aws-lambda-https-docs-aws-amazon-com-ja-jp-amazoncloudwatch-latest-monit-243b74]]: 本書は、AWS の各サービスにおける「ベストプラクティスアラーム」の設定推奨事項をまとめた技術ガイドです。

## 関連

- [[aws-lambda-alb-lambda-https-179a86]]
- [[serverless]]
- [[api-gateway]]
- [[aws]]
- [[aws-lambda-api-gateway-amazon-8c3dca]]
- [[aws-lambda-aws-lambda-https-8a37a1]]
- [[aws-lambda-aws-lambda-api-cafc43]]
- [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]
- [[aws-lambda-amazon-api-gateway-1339da]]
- [[aws-lambda-async-lambda-function-5b6e4a]]

## 出典

- `60_Resources/ALB と Lambda のリクエストサイズの最大値.md`
- https://yohei-a.hatenablog.jp/entry/20210115/1610705961
- `60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md`
- https://tech.every.tv/entry/20240611
- `60_Resources/AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める.md`
- https://qiita.com/horit0123/items/295f8dc55d8c07e6512a
- `60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md`
- https://qiita.com/unhurried/items/5a497ec81e4fefe22396
- `60_Resources/AWS側がしてきたECS  Fargate のスケーリング速度改善の話.md`
- https://qiita.com/yoshii0110/items/cbbfe797845dfa7e181d
- `60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md`
- https://tech.aptpod.co.jp/entry/2021/12/06/070000
- `60_Resources/Async Lambda Function Retries with Backoff and Jitter.md`
- https://lucvandonkersgoed.com/2022/02/07/async-lambda-function-retries-with-backoff-and-jitter/
- `60_Resources/CloudWatch Logs と S3 にかかる料金比較.md`
- https://dev.classmethod.jp/articles/comparison-of-fees-for-cloudwatch-logs-and-s3/
- `60_Resources/MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）.md`
- https://zenn.dev/ncdc/articles/eaa3d113c27f28
- `60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md`
- https://tmokmss.hatenablog.com/entry/20221213/1670891305
- `60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md`
- https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/http-api-vs-rest.html
- `60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md`
- https://qiita.com/hirai-11/items/f16b326061956fb85c9c
- `60_Resources/え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾.md`
- https://dev.classmethod.jp/articles/5-ways-to-spend-cost-on-aws-v3/
- `60_Resources/クォータ.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html
- `60_Resources/推奨アラーム.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html
