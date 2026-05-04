---
title: "S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介"
type: "topic"
tags:
  - "amazon-ec2"
  - "cloudformation"
  - "networking"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介.md"
summary: "S3 Express One Zone 用 VPC エンドポイント構築の要約"
---

# S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介

## 概要

S3 Express One Zone 用 VPC エンドポイント構築の要約

*発行: 2024-01-21 / [[amazon-ec2-cloudformation-s3-express-one-a725cf]]*

## 主要なトピック

- [[amazon-ec2]]
- [[cloudformation]]
- [[networking]]

## 詳細

- 本記事は、CloudFormation を使用して S3 Express One Zone 用の Gateway 型 VPC エンドポイントを構築する方法を解説しています。
- 要点
- **専用エンドポイントが必要**: 通常の S3 用 VPC エンドポイントとは別に、S3 Express One Zone 用（`com.amazonaws.[region].s3express`）のエンドポイントを作成する必要があります。
- **実装のポイント**: CloudFormation テンプレートにおいて、`ServiceName` プロパティを適切に指定することで、既存の VPC への追加や新規構築が可能です。
- **メリット**: VPC エンドポイント経由での通信により、EC2 と S3 Express One Zone 間の通信経路が最適化され、通信コストの削減が期待できます。
- **設定例**: 記事内では、3AZ 構成のネットワーク環境に S3 および S3 Express One Zone 用のエンドポイントを両方定義した CloudFormation テンプレートのサンプルが提供されています。

*発行: 2024-01-21 / [[amazon-ec2-cloudformation-s3-express-one-a725cf]]*

## 関連テーマ

- [[amazon-ec2]]
- [[cloudformation]]
- [[networking]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介.md`
- https://dev.classmethod.jp/articles/cloudformation-template-for-s3-express-one-zone-vpc-endpoint/
