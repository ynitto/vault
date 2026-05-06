---
title: "ALB と Lambda のリクエストサイズの最大値"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "serverless"
  - "yohei-a"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ALB と Lambda のリクエストサイズの最大値.md"
summary: "AWS LambdaとApplication Load Balancer（ALB）を連携させる際の、リクエストペイロード制限に関する技術情報のまとめです。"
---

# ALB と Lambda のリクエストサイズの最大値

## 概要

AWS LambdaとApplication Load Balancer（ALB）を連携させる際の、リクエストペイロード制限に関する技術情報のまとめです。

*発行: 2021-01-15 / [[aws-lambda-alb-lambda-https-179a86]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[serverless]]
- [[yohei-a]]

## 詳細

- AWS LambdaとApplication Load Balancer（ALB）を連携させる際の、リクエストペイロード制限に関する技術情報のまとめです。
- 要点
- **Lambdaのペイロード制限**
- 同期呼び出し: 最大 6MB
- 非同期呼び出し: 最大 256KB
- **ALB経由の制限**
- Lambdaをターゲットとする場合、リクエストボディは最大 **1MB** に制限されます。
- **トラブルシューティング**
- リクエストボディが1MBを超えると「HTTP 413: Payload too large」エラーが発生します。

*発行: 2021-01-15 / [[aws-lambda-alb-lambda-https-179a86]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[serverless]]
- [[yohei-a]]

## 出典

- `60_Resources/ALB と Lambda のリクエストサイズの最大値.md`
- https://yohei-a.hatenablog.jp/entry/20210115/1610705961
