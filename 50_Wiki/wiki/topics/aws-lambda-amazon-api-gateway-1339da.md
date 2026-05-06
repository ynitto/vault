---
title: "Amazon API Gateway での相互 TLS 認証をちゃんとやる"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "api-gateway"
  - "authentication"
  - "aptpod-tech-writer"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md"
summary: "Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この…"
---

# Amazon API Gateway での相互 TLS 認証をちゃんとやる

## 概要

Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この問題を Lambda オーソライザーを活用して解決し、失効済み証明書による不正アクセスを拒否する実装方法を解説しています。

*発行: 2021-12-06 / [[aws-lambda-amazon-api-gateway-1339da]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[authentication]]
- [[aptpod-tech-writer]]

## 詳細

- Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この問題を Lambda オーソライザーを活用して解決し、失効済み証明書による不正アクセスを拒否する実装方法を解説しています。
- 重要なポイント
- 課題
- Amazon API Gateway の標準機能では、mTLS の証明書失効リスト（CRL）や OCSP による検証が行われない。
- 一度発行された証明書は、有効期限内であれば失効させてもアクセスが遮断されないリスクがある。
- 解決策：Lambda オーソライザーの実装
- **仕組み**: Lambda オーソライザーへ渡される証明書情報を利用し、Lambda 関数内で `certvalidator` 等を用いて失効状態を検証する。
- **効率化**: トラストストアをハンドラ外で読み込み（グローバルスコープ）、Lambda のコールドスタート時にのみ S3 と通信することでレイテンシを抑える。
- **設定**:

*発行: 2021-12-06 / [[aws-lambda-amazon-api-gateway-1339da]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[authentication]]
- [[aptpod-tech-writer]]

## 出典

- `../60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md`
- https://tech.aptpod.co.jp/entry/2021/12/06/070000
