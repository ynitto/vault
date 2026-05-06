---
title: "信頼は相互に: Amazon CloudFront が mTLS をサポート"
type: "topic"
tags:
  - "aws"
  - "authentication"
  - "cloudfront"
  - "security"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート.md"
summary: "Amazon CloudFront が mTLS をサポート"
---

# 信頼は相互に: Amazon CloudFront が mTLS をサポート

## 概要

Amazon CloudFront が mTLS をサポート

*発行: 2025-12-04 / [[aws-authentication-amazon-cloudfront-mtls-2f6191]]*

## 主要なトピック

- [[aws]]
- [[authentication]]
- [[cloudfront]]
- [[security]]

## 詳細

- Amazon CloudFront は、エンドユーザーと CloudFront 間の相互 TLS 認証 (mTLS) をサポートしました。これにより、アプリケーションのセキュリティ強化とアクセス制御の最適化が可能になります。
- 主なメリット
- **ゼロトラストの実現**: クライアントとサーバー双方が証明書を検証し、認証を相互に行うことで信頼を確立。
- **多様なユースケース**: 金融取引（PCI DSS）、IoTデバイス認証、企業内アプリのアクセス制限、医療データ保護などに有効。
- **運用の効率化**: AWS Private CA や Trust Store と統合し、証明書のプロビジョニングから検証までを自動化。
- 実装と管理のポイント
- **柔軟なモード選択**:
- **Required**: すべての接続に有効な証明書を必須とする。
- **Optional**: mTLS と非 mTLS の混在を許可し、無効な証明書のみを拒否する。

*発行: 2025-12-04 / [[aws-authentication-amazon-cloudfront-mtls-2f6191]]*

## 関連テーマ

- [[aws]]
- [[authentication]]
- [[cloudfront]]
- [[security]]

## 出典

- `../60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート.md`
- https://aws.amazon.com/jp/blogs/news/trust-goes-both-ways-amazon-cloudfront-now-supports-viewer-mtls/
