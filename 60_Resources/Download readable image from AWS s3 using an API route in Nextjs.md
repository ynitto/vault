---
title: "Download readable image from AWS s3 using an API route in Nextjs"
source: "https://stackoverflow.com/questions/71523267/download-readable-image-from-aws-s3-using-an-api-route-in-nextjs"
author:
  - "[[Ahmed Elsayes 13122 silver badges99 bronze badges]]"
published: 2022-03-18
created: 2026-05-01
description: "I am using Nextjs to build my app. I am using AWS s3 to store my static files (images and PDFs,..)I want user of my application to be able to download the file. I used the answer mentioned here to"
tags:
  - "clippings"
---
### Next.jsのAPIルートでAWS S3から画像ファイルをダウンロードする方法

Next.jsのAPIルートを通じてS3上のファイルをダウンロードする際、画像が読み込めないという問題に対する解決策です。

#### 原因
- `downloadedObject.Body?.toString('base64')` を使用して変換していたため、バイナリデータが正しく処理されていませんでした。

#### 解決策
- **ストリーム処理を利用する**: `s3.getObject().createReadStream()` を使い、パイプラインでレスポンスに直接流し込みます。

#### 実装コードの要点
- `createReadStream()` を使用してオブジェクトをストリームとして取得。
- `Content-Type` ヘッダーをファイル拡張子（image/png, image/jpeg等）に合わせて適切に設定。
- `res.setHeader('Content-Disposition', ...)` でダウンロード形式を指定。
- `readableObject.pipe(res)` でストリームをレスポンスに連結。
