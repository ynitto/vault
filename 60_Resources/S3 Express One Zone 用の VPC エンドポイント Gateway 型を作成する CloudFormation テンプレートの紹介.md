---
title: "S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介"
source: "https://dev.classmethod.jp/articles/cloudformation-template-for-s3-express-one-zone-vpc-endpoint/"
author:
  - "[[大村 保貴]]"
published: 2024-01-21
created: 2026-05-01
description:
tags:
  - "clippings"
---
### S3 Express One Zone 用 VPC エンドポイント構築の要約
本記事は、CloudFormation を使用して S3 Express One Zone 用の Gateway 型 VPC エンドポイントを構築する方法を解説しています。

### 要点
- **専用エンドポイントが必要**: 通常の S3 用 VPC エンドポイントとは別に、S3 Express One Zone 用（`com.amazonaws.[region].s3express`）のエンドポイントを作成する必要があります。
- **実装のポイント**: CloudFormation テンプレートにおいて、`ServiceName` プロパティを適切に指定することで、既存の VPC への追加や新規構築が可能です。
- **メリット**: VPC エンドポイント経由での通信により、EC2 と S3 Express One Zone 間の通信経路が最適化され、通信コストの削減が期待できます。
- **設定例**: 記事内では、3AZ 構成のネットワーク環境に S3 および S3 Express One Zone 用のエンドポイントを両方定義した CloudFormation テンプレートのサンプルが提供されています。