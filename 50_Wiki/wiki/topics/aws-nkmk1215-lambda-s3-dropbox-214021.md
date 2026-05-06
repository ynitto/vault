---
title: "LambdaでS3にある画像をDropbox Businessにアップロードする"
type: "topic"
tags:
  - "aws"
  - "nkmk1215"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/LambdaでS3にある画像をDropbox Businessにアップロードする.md"
summary: "AWS Lambdaを利用し、S3上の画像をDropbox Businessの共有フォルダへアップロードするための実装手順に関する個人用メモです。"
---

# LambdaでS3にある画像をDropbox Businessにアップロードする

## 概要

AWS Lambdaを利用し、S3上の画像をDropbox Businessの共有フォルダへアップロードするための実装手順に関する個人用メモです。

*発行: 2021-09-20 / [[aws-nkmk1215-lambda-s3-dropbox-214021]]*

## 主要なトピック

- [[aws]]
- [[nkmk1215]]

## 詳細

- AWS Lambdaを利用し、S3上の画像をDropbox Businessの共有フォルダへアップロードするための実装手順に関する個人用メモです。
- 要点まとめ
- **事前準備**
- Dropbox Business APIの知識とアクセストークンの準備が必要。
- アプリ設定は「Full Dropbox」で作成する。
- **Root Namespace IDの取得**
- `get_current_account` APIを実行し、チームスペースのルートフォルダIDを特定する。
- **ソースコードの修正**
- Lambda関数のHTTPヘッダーに`Dropbox-API-Path-Root`を追加する。

*発行: 2021-09-20 / [[aws-nkmk1215-lambda-s3-dropbox-214021]]*

## 関連テーマ

- [[aws]]
- [[nkmk1215]]

## 出典

- `60_Resources/LambdaでS3にある画像をDropbox Businessにアップロードする.md`
- https://qiita.com/nkmk1215/items/95e2d97e5bb89a8b904a
