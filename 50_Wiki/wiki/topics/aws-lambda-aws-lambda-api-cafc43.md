---
title: "AWS Lambda：API GatewayとApplication Load Balancerの違い"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "api-gateway"
  - "networking"
  - "ohtsuka1317"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md"
summary: "AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (A…"
---

# AWS Lambda：API GatewayとApplication Load Balancerの違い

## 概要

AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (ALB)」の主な違いを比較・解説した記事です。

*発行: 2019-08-07 / [[aws-lambda-aws-lambda-api-cafc43]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[networking]]
- [[ohtsuka1317]]

## 詳細

- AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (ALB)」の主な違いを比較・解説した記事です。
- 比較のポイント
- **API Gatewayの特性**
- リクエスト検証、データマッピング、SDK生成などの豊富な独自機能がある。
- HTTPS (443番ポート) のみに対応。
- タイムアウトは最大29秒まで。
- 実行回数ベースの課金（少〜中規模リクエストで有利）。
- **ALBの特性**
- 任意のポートやプロトコル設定が可能。

*発行: 2019-08-07 / [[aws-lambda-aws-lambda-api-cafc43]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[networking]]
- [[ohtsuka1317]]

## 出典

- `60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md`
- https://qiita.com/unhurried/items/5a497ec81e4fefe22396
