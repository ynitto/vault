---
title: "REST API と HTTP API のどちらかを選択する - Amazon API Gateway"
source: "https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/http-api-vs-rest.html"
author:
published:
created: 2026-05-01
description: "REST API と HTTP API の違いについて説明します。"
tags:
  - "clippings"
---
### Amazon API Gateway：REST API と HTTP API の比較要約

AWS の API Gateway で提供される「REST API」と「HTTP API」は、どちらも RESTful API ですが、設計思想と機能範囲が異なります。

#### 1. 基本的な違い
- **REST API**: 豊富な機能が求められる複雑な構成向け。セキュリティや管理機能が充実している。
- **HTTP API**: 低価格かつ低レイテンシーが求められる、最小限の機能構成向け。

#### 2. 主な機能比較の要点
- **セキュリティ・管理**: API キー、クライアントごとのレート制限、AWS WAF との統合、プライベート API は **REST API のみ**が対応。
- **認可**: 両者ともに IAM、Lambda 認可をサポート。**JWT 認証**は HTTP API が得意とし、**リソースポリシー**は REST API のみ対応。
- **開発・デプロイ**: REST API は手動デプロイやCanaryリリース、リクエスト検証が可能。HTTP API は自動デプロイが標準。
- **統合**: 基本的な Lambda、HTTP、AWS サービス統合は両者可能。**レスポンスストリーミング**や **Mock 統合**は REST API のみ。

#### 3. 選択基準
- **REST API を選ぶべきケース**: 強固な保護機能、きめ細かなアクセス制御（API キーなど）、高度なリクエスト変換が必要な場合。
- **HTTP API を選ぶべきケース**: シンプルな実装でコストを抑えたい場合、および高速なレスポンスが最優先される場合。