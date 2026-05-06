---
title: "vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた"
type: "topic"
tags:
  - "lambda"
  - "networking"
  - "serverless"
  - "hirai-11"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md"
summary: "VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技…"
---

# vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた

## 概要

VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技術解説記事です。

*発行: 2022-11-15 / [[lambda-networking-vpc-lambda-invoke-ec6acf]]*

## 主要なトピック

- [[lambda]]
- [[networking]]
- [[serverless]]
- [[hirai-11]]

## 詳細

- VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技術解説記事です。
- 検証の要点
- **結論**: VPC内のLambda（パブリック/プライベート問わず）は、標準設定ではインターネット経由でAWS APIを呼び出せないため、Lambda同士の直接的なinvokeに失敗する。
- **解決策**: VPCエンドポイント（Interface型）を設置することで、VPC内からAWSサービスへのアクセスが可能となり、Lambdaの呼び出しが成功する。
- **構成要素**:
- 呼び出し元と呼び出し先のLambda関数を作成
- 適切なIAMロール（`AWSLambdaVPCAccessExecutionRole`等）の付与
- VPCエンドポイントの適切なセキュリティグループ設定
- 検証結果のまとめ

*発行: 2022-11-15 / [[lambda-networking-vpc-lambda-invoke-ec6acf]]*

## 関連テーマ

- [[lambda]]
- [[networking]]
- [[serverless]]
- [[hirai-11]]

## 出典

- `60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md`
- https://qiita.com/hirai-11/items/f16b326061956fb85c9c
