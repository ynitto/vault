---
title: "Amazon API Gateway"
type: "product"
tags:
  - "aws"
  - "api"
  - "serverless"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md"
  - "60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md"
  - "60_Resources/API GatewayでKinesis Data Firehoseのプロキシを作成する.md"
  - "60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md"
  - "60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md"
  - "60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md"
  - "60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md"
  - "60_Resources/ついにAPI Gatewayの統合タイムアウトが29秒の壁を超えられるように！実際に延長リクエストしてみた.md"
  - "60_Resources/サーバーレスなデータ収集APIを作るときの困りポイント.md"
  - "60_Resources/推奨アラーム.md"
summary: "API 公開や統合を担う AWS のゲートウェイサービス。"
---

# Amazon API Gateway

## 概要










Amazon API Gateway は HTTP API や統合処理の入口になり、認証・制御・周辺 AWS サービス接続を担う。










## 詳細

- [[aws-lambda-api-gateway-amazon-8c3dca]]: API GatewayからLambdaを使用せずに、直接Amazon Data Firehoseへイベントログを転送し、S3へ保存する構成を実現する方法についての解説記事です。
*発行: 2024-06-11 / [[aws-lambda-api-gateway-amazon-8c3dca]]*
- [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]: API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとCloudFrontのカスタムヘ…
*発行: 2022-06-13T00:00:00Z / [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]*
- [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]: 本記事では、API Gatewayをプロキシとして利用し、受信したデータをKinesis Data Firehose経由でS3バケットへ自動的に保存する構築手順を紹介しています。
*発行: 2023-04-10 / [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]*
- [[aws-lambda-aws-lambda-api-cafc43]]: AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (ALB)」の主な違いを比較…
*発行: 2019-08-07 / [[aws-lambda-aws-lambda-api-cafc43]]*
- [[aws-lambda-amazon-api-gateway-1339da]]: Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この問題を Lambda オ…
*発行: 2021-12-06 / [[aws-lambda-amazon-api-gateway-1339da]]*
- [[aws-lambda-next-js-lambda-api-e4f04b]]: Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法についての解説記事です。
*発行: 2022-12-13 / [[aws-lambda-next-js-lambda-api-e4f04b]]*
- [[aws-lambda-rest-api-http-47b62c]]: Amazon API Gateway：REST API と HTTP API の比較要約
- [[aws-api-gateway-api-gateway-29-011e61]]: API Gateway 統合タイムアウト延長の概要
*発行: 2024-06-14 / [[aws-api-gateway-api-gateway-29-011e61]]*
- [[aws-api-gateway-api-https-engineers-fenrir-inc-com-entry-2023-03-16-1728-603157]]: AWS API Gateway、Kinesis、S3を組み合わせたデータ収集APIの構築において、実務で発生しやすい課題とその解決策を解説した記事です。
*発行: 2023-03-16 / [[aws-api-gateway-api-https-engineers-fenrir-inc-com-entry-2023-03-16-1728-603157]]*
- [[aws-lambda-https-docs-aws-amazon-com-ja-jp-amazoncloudwatch-latest-monit-243b74]]: 本書は、AWS の各サービスにおける「ベストプラクティスアラーム」の設定推奨事項をまとめた技術ガイドです。

## 関連

- [[aws-lambda-api-gateway-amazon-8c3dca]]
- [[lambda]]
- [[serverless]]
- [[authentication]]
- [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]
- [[api-gateway-serverless-api-gateway-kinesis-55f6a8]]
- [[aws-lambda-aws-lambda-api-cafc43]]
- [[aws-lambda-amazon-api-gateway-1339da]]
- [[aws-lambda-next-js-lambda-api-e4f04b]]
- [[aws-lambda-rest-api-http-47b62c]]

## 出典

- `60_Resources/API Gateway から Amazon Data Firehose へ Lambda を使わずにデータを流す.md`
- https://tech.every.tv/entry/20240611
- `60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md`
- https://zatoima.github.io/aws-api-gateway-cloudfront-restrict-resource-policy/
- `60_Resources/API GatewayでKinesis Data Firehoseのプロキシを作成する.md`
- https://techblog.techfirm.co.jp/entry/create-kinesis-firehose-proxy-with-api-gateway
- `60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md`
- https://qiita.com/unhurried/items/5a497ec81e4fefe22396
- `60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md`
- https://tech.aptpod.co.jp/entry/2021/12/06/070000
- `60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md`
- https://tmokmss.hatenablog.com/entry/20221213/1670891305
- `60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md`
- https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/http-api-vs-rest.html
- `60_Resources/ついにAPI Gatewayの統合タイムアウトが29秒の壁を超えられるように！実際に延長リクエストしてみた.md`
- https://qiita.com/shimagaji/items/4fa220ea0215a04704b6
- `60_Resources/サーバーレスなデータ収集APIを作るときの困りポイント.md`
- https://engineers.fenrir-inc.com/entry/2023/03/16/172808
- `60_Resources/推奨アラーム.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html
