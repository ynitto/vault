---
title: "API Gateway のアクセス元をリソースポリシー機能を使用してCloudFrontのみに限定する方法"
source: "https://zatoima.github.io/aws-api-gateway-cloudfront-restrict-resource-policy/"
author:
  - "[[\"zatoima\"]]"
published: "2022-06-13T00:00:00Z"
created: 2026-05-01
description: "memo blog. Hugo on GitHub Pages"
tags:
  - "clippings"
---
### 要約
API Gatewayへの直接アクセスを遮断し、CloudFront経由のアクセスのみを許可するために、API GatewayのリソースポリシーとCloudFrontのカスタムヘッダーを組み合わせる手法の解説記事です。

### 重要ポイント
- **仕組みの概要**
  - CloudFrontからAPI Gatewayへのリクエストにカスタムヘッダーを付与。
  - API Gatewayのリソースポリシーにて、そのカスタムヘッダーがないリクエストを拒否（Deny）するように設定。

- **主な手順**
  1. **CloudFront設定**: オリジンリクエストに推測されにくいカスタムヘッダーを追加。
  2. **API Gateway設定**: リソースポリシーにて `StringNotEquals` 条件を用い、特定ヘッダーがない場合に `Deny` するポリシーを適用。
  3. **デプロイ**: 設定反映のため、API Gatewayの再デプロイを実施。

- **注意点**
  - カスタムヘッダー値は第三者に漏洩しないよう、十分に複雑な文字列にする必要があります。