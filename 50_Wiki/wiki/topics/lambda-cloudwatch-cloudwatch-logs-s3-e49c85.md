---
title: "CloudWatch Logs と S3 にかかる料金比較"
type: "topic"
tags:
  - "lambda"
  - "cloudwatch"
  - "serverless"
  - "emi"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/CloudWatch Logs と S3 にかかる料金比較.md"
summary: "CloudWatch LogsとS3の料金比較と、コスト最適化の考え方をまとめた記事です。"
---

# CloudWatch Logs と S3 にかかる料金比較

## 概要

CloudWatch LogsとS3の料金比較と、コスト最適化の考え方をまとめた記事です。

*発行: 2024-05-26 / [[lambda-cloudwatch-cloudwatch-logs-s3-e49c85]]*

## 主要なトピック

- [[lambda]]
- [[cloudwatch]]
- [[serverless]]
- [[emi]]

## 詳細

- CloudWatch LogsとS3の料金比較と、コスト最適化の考え方をまとめた記事です。
- 要点
- **料金の構造と違い**
- **CloudWatch Logs**: 書き込み（取り込み）料金が高価。保存料金は自動圧縮（15%程度）されるため、生データ量で比較するとS3と大きな差はない。
- **S3**: 書き込みはリクエスト数課金。保存料金は安価だが、大量の書き込みが発生する場合やアーキテクチャの変更が必要。
- **コスト削減の誤解**
- ログの保持期間を短くするだけでは大幅な削減は難しい。
- CloudWatch Logsを経由してS3へ流すと、取り込みコストが発生するため逆に高くなる可能性がある。
- **適材適所の選択**

*発行: 2024-05-26 / [[lambda-cloudwatch-cloudwatch-logs-s3-e49c85]]*

## 関連テーマ

- [[lambda]]
- [[cloudwatch]]
- [[serverless]]
- [[emi]]

## 出典

- `../60_Resources/CloudWatch Logs と S3 にかかる料金比較.md`
- https://dev.classmethod.jp/articles/comparison-of-fees-for-cloudwatch-logs-and-s3/
