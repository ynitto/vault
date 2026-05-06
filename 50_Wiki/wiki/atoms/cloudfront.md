---
title: "Amazon CloudFront"
type: "product"
tags:
  - "aws"
  - "cloudfront"
  - "cdn"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md"
  - "../60_Resources/AWSCloudFrontTrustStore CaCertificatesBundleS3Location - AWS CloudFormation.md"
  - "../60_Resources/Amazon CloudFront KeyValueStoreを活用した記事のリリース制御.md"
  - "../60_Resources/CloudFrontを経由しないALBへのアクセスを制限する.md"
  - "../../60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md"
  - "../60_Resources/describe-key-value-store — AWS CLI 2.34.32 Command Reference.md"
  - "../60_Resources/クォータ.md"
  - "../60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート.md"
  - "../60_Resources/小ネタ S3に保存されているログファイルをAWS CLIでまとめてコピーする.md"
summary: "CDN とエッジ制御を担う AWS サービス。"
---

# Amazon CloudFront

## 概要









Amazon CloudFront はコンテンツ配信だけでなく、エッジ認証やキャッシュ制御、KeyValueStore 連携などの設計点を持つ。









## 詳細

- [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]: API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとCloudFrontのカスタムヘ…
*発行: 2022-06-13T00:00:00Z / [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]*
- [[aws-cloudformation-aws-cloudfront-truststore-e46572]]: 本ドキュメントは、AWS CloudFormation における `AWS::CloudFront::TrustStore` のプロパティである `CaCertificatesB…
- [[aws-cloudfront-amazon-cloudfront-keyvaluestore-a212cb]]: 与えられた情報を整理・抽出し、視認性の高い形式で整理します。
*発行: 2023-12-22 / [[aws-cloudfront-amazon-cloudfront-keyvaluestore-a212cb]]*
- [[aws-cloudfront-cloudfront-alb-https-bd45fd]]: CloudFrontとALBを用いた構成において、ALBへ直接アクセスされるセキュリティリスクを防ぐための2つの手法を解説しています。
*発行: 2022-09-22 / [[aws-cloudfront-cloudfront-alb-https-bd45fd]]*
- [[aws-lambda-next-js-lambda-api-e4f04b]]: Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法についての解説記事です。
*発行: 2022-12-13 / [[aws-lambda-next-js-lambda-api-e4f04b]]*
- [[aws-cloudfront-describe-key-value-store-aws-cli-8cbbd0]]: AWS CLI: describe-key-value-store
- [[aws-lambda-https-docs-aws-amazon-com-ja-jp-amazoncloudfront-latest-devel-ab9d59]]: 本ドキュメントは、Amazon CloudFrontにおける各種制限事項（クォータ）の一覧です。多くの項目はService QuotasやAWSサポートを通じて引き上げが可能です。
- [[aws-authentication-amazon-cloudfront-mtls-2f6191]]: Amazon CloudFront が mTLS をサポート
*発行: 2025-12-04 / [[aws-authentication-amazon-cloudfront-mtls-2f6191]]*
- [[aws-cloudfront-s3-aws-cli-7a1230]]: AWS CLIを使用して、S3上の大量のログファイルから特定の日付・条件のファイルをローカルへ効率的にコピーする方法の解説。
  *発行: 2016-09-24 / [[aws-cloudfront-s3-aws-cli-7a1230]]*

## 関連

- [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]
- [[aws]]
- [[networking]]
- [[aws-cloudformation-aws-cloudfront-truststore-e46572]]
- [[aws-cloudfront-amazon-cloudfront-keyvaluestore-a212cb]]
- [[aws-cloudfront-cloudfront-alb-https-bd45fd]]
- [[aws-lambda-next-js-lambda-api-e4f04b]]
- [[aws-cloudfront-describe-key-value-store-aws-cli-8cbbd0]]
- [[aws-lambda-https-docs-aws-amazon-com-ja-jp-amazoncloudfront-latest-devel-ab9d59]]
- [[aws-authentication-amazon-cloudfront-mtls-2f6191]]

## 出典

- `../60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md`
- https://zatoima../.github.io/aws-api-gateway-cloudfront-restrict-resource-policy/
- `../60_Resources/AWSCloudFrontTrustStore CaCertificatesBundleS3Location - AWS CloudFormation.md`
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-truststore-cacertificatesbundles3location.html
- `../60_Resources/Amazon CloudFront KeyValueStoreを活用した記事のリリース制御.md`
- https://blog.usize-tech.com/cloudfront-keyvaluestore/
- `../60_Resources/CloudFrontを経由しないALBへのアクセスを制限する.md`
- https://tech.revcomm.co.jp/cf-alb-access-restriction
- `../../60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md`
- https://tmokmss.hatenablog.com/entry/20221213/1670891305
- `../60_Resources/describe-key-value-store — AWS CLI 2.34.32 Command Reference.md`
- https://docs.aws.amazon.com/cli/latest/reference/cloudfront-keyvaluestore/describe-key-value-store.html
- `../60_Resources/クォータ.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html
- `../60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート.md`
- https://aws.amazon.com/jp/blogs/news/trust-goes-both-ways-amazon-cloudfront-now-supports-viewer-mtls/
- `../60_Resources/小ネタ S3に保存されているログファイルをAWS CLIでまとめてコピーする.md`
- https://dev.classmethod.jp/articles/s3-logfile-copy-by-awscli/
