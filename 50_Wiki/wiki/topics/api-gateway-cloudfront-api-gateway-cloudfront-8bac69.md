---
title: "API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法"
type: "topic"
tags:
  - "api-gateway"
  - "cloudfront"
  - "serverless"
  - "zatoima"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md"
summary: "API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとClou…"
---

# API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法

## 概要

API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとCloudFrontのカスタムヘッダーを組み合わせる手法の解説記事です。

*発行: 2022-06-13T00:00:00Z / [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]*

## 主要なトピック

- [[api-gateway]]
- [[cloudfront]]
- [[serverless]]
- [[zatoima]]

## 詳細

- API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとCloudFrontのカスタムヘッダーを組み合わせる手法の解説記事です。
- 重要ポイント
- **仕組みの概要**
- CloudFrontからAPI Gatewayへのリクエストにカスタムヘッダーを付与。
- API Gatewayのリソースポリシーにて、そのカスタムヘッダーがないリクエストを拒否（Deny）するように設定。
- **主な手順**
- 1. **CloudFront設定**: オリジンリクエストに推測されにくいカスタムヘッダーを追加。
- 2. **API Gateway設定**: リソースポリシーにて `StringNotEquals` 条件を用い、特定ヘッダーがない場合に `Deny` するポリシーを適用。
- 3. **デプロイ**: 設定反映のため、API Gatewayの再デプロイを実施。

*発行: 2022-06-13T00:00:00Z / [[api-gateway-cloudfront-api-gateway-cloudfront-8bac69]]*

## 関連テーマ

- [[api-gateway]]
- [[cloudfront]]
- [[serverless]]
- [[zatoima]]

## 出典

- `60_Resources/API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法.md`
- https://zatoima.github.io/aws-api-gateway-cloudfront-restrict-resource-policy/
