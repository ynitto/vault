---
title: "Download readable image from AWS s3 using an API route in Nextjs"
type: "topic"
tags:
  - "aws"
  - "ahmed-elsayes-13122-silver"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Download readable image from AWS s3 using an API route in Nextjs.md"
summary: "Next.jsのAPIルートでAWS S3から画像ファイルをダウンロードする方法"
---

# Download readable image from AWS s3 using an API route in Nextjs

## 概要

Next.jsのAPIルートでAWS S3から画像ファイルをダウンロードする方法

*発行: 2022-03-18 / [[aws-ahmed-elsayes-13122-silver-download-readable-image-b42591]]*

## 主要なトピック

- [[aws]]
- [[ahmed-elsayes-13122-silver]]

## 詳細

- Next.jsのAPIルートを通じてS3上のファイルをダウンロードする際、画像が読み込めないという問題に対する解決策です。
- 原因
- `downloadedObject.Body?.toString('base64')` を使用して変換していたため、バイナリデータが正しく処理されていませんでした。
- 解決策
- **ストリーム処理を利用する**: `s3.getObject().createReadStream()` を使い、パイプラインでレスポンスに直接流し込みます。
- 実装コードの要点
- `createReadStream()` を使用してオブジェクトをストリームとして取得。
- `Content-Type` ヘッダーをファイル拡張子（image/png, image/jpeg等）に合わせて適切に設定。
- `res.setHeader('Content-Disposition', ...)` でダウンロード形式を指定。

*発行: 2022-03-18 / [[aws-ahmed-elsayes-13122-silver-download-readable-image-b42591]]*

## 関連テーマ

- [[aws]]
- [[ahmed-elsayes-13122-silver]]

## 出典

- `60_Resources/Download readable image from AWS s3 using an API route in Nextjs.md`
- https://stackoverflow.com/questions/71523267/download-readable-image-from-aws-s3-using-an-api-route-in-nextjs
