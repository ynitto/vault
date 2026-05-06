---
title: "REST API と HTTP API のどちらかを選択する - Amazon API Gateway"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "api-gateway"
  - "authentication"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md"
summary: "Amazon API Gateway：REST API と HTTP API の比較要約"
---

# REST API と HTTP API のどちらかを選択する - Amazon API Gateway

## 概要

Amazon API Gateway：REST API と HTTP API の比較要約

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[authentication]]

## 詳細

- AWS の API Gateway で提供される「REST API」と「HTTP API」は、どちらも RESTful API ですが、設計思想と機能範囲が異なります。
- 1. 基本的な違い
- **REST API**: 豊富な機能が求められる複雑な構成向け。セキュリティや管理機能が充実している。
- **HTTP API**: 低価格かつ低レイテンシーが求められる、最小限の機能構成向け。
- 2. 主な機能比較の要点
- **セキュリティ・管理**: API キー、クライアントごとのレート制限、AWS WAF との統合、プライベート API は **REST API のみ**が対応。
- **認可**: 両者ともに IAM、Lambda 認可をサポート。**JWT 認証**は HTTP API が得意とし、**リソースポリシー**は REST API のみ対応。
- **開発・デプロイ**: REST API は手動デプロイやCanaryリリース、リクエスト検証が可能。HTTP API は自動デプロイが標準。
- **統合**: 基本的な Lambda、HTTP、AWS サービス統合は両者可能。**レスポンスストリーミング**や **Mock 統合**は REST API のみ。

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[authentication]]

## 出典

- `60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md`
- https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/http-api-vs-rest.html
