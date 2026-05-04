---
title: "AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "serverless"
  - "tfrcm"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める.md"
summary: "本記事は、2019年末に発表されたAWS Lambdaの非同期呼び出しに関する新機能（結果の出力先指定とリトライ設定）を検証したレポートです。"
---

# AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める

## 概要

本記事は、2019年末に発表されたAWS Lambdaの非同期呼び出しに関する新機能（結果の出力先指定とリトライ設定）を検証したレポートです。

*発行: 2020-01-21 / [[aws-lambda-aws-lambda-https-8a37a1]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[serverless]]
- [[tfrcm]]

## 詳細

- 本記事は、2019年末に発表されたAWS Lambdaの非同期呼び出しに関する新機能（結果の出力先指定とリトライ設定）を検証したレポートです。
- 主要なポイント
- **非同期呼び出しの機能強化**
- **Destinations (送信先設定):**
- 非同期処理の「成功時」および「失敗時」の実行結果を、SQS、SNS、Lambda、EventBridgeへ送信可能。
- 従来の手動実装やDLQよりも詳細な情報（入出力内容、エラーの詳細）を取得可能。
- **最大リトライ回数の制御:**
- これまで固定（最大2回）だったリトライ回数を0〜2回の間で設定可能に。
- 不要なリトライを回避することで、無駄な処理コストやエラーの重複を抑止できる。

*発行: 2020-01-21 / [[aws-lambda-aws-lambda-https-8a37a1]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[serverless]]
- [[tfrcm]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AWS Lambda関数を非同期で呼ぶ場合の動きを改めて確める.md`
- https://qiita.com/horit0123/items/295f8dc55d8c07e6512a
