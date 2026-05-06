---
title: "Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード)"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "api-gateway"
  - "cloudfront"
  - "tmokmss"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md"
summary: "Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法…"
---

# Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード)

## 概要

Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法についての解説記事です。

*発行: 2022-12-13 / [[aws-lambda-next-js-lambda-api-e4f04b]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[cloudfront]]
- [[tmokmss]]

## 詳細

- Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法についての解説記事です。
- 要点
- **構成のメリット**:
- サーバーレスで運用コストを低減（リクエストがない時は料金ゼロ）。
- AWS Lambda Web Adapterを利用することで、コンテナベースのWebアプリを最小限の変更で移植可能。
- **主な設定手順**:
- `next.config.js`に`output: 'standalone'`を追加。
- `Dockerfile`にて`aws-lambda-adapter`をインストール。
- ベースイメージを`amazon/aws-lambda-nodejs`にすることで、Lambdaのイメージキャッシュ効率を高めコールドスタートを短縮。

*発行: 2022-12-13 / [[aws-lambda-next-js-lambda-api-e4f04b]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[api-gateway]]
- [[cloudfront]]
- [[tmokmss]]

## 出典

- `60_Resources/Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード).md`
- https://tmokmss.hatenablog.com/entry/20221213/1670891305
