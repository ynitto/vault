---
title: "Next.jsをLambda + API Gatewayでサーバーレス化する (standaloneモード)"
source: "https://tmokmss.hatenablog.com/entry/20221213/1670891305"
author:
  - "[[tmokmss]]"
published: 2022-12-13
created: 2026-05-01
description: "これは AWS LambdaとServerless Advent Calendar 2022 の記事です。 Next.jsをホスティングする手段の一つとして、Standaloneモードで動かす方法があります。 コンテナ1個で動かせるため非常にお手軽な選択肢で、GCPのCloud RunやAWSのApp Runnerなどで動かす例を見ることも多いです。 この記事では、AWS Lambda + API Gatewayのサーバーレス鉄板構成でNext.js standaloneモードを公開する方法を紹介します。巷ではあまり見かけない構成だったので、新しい選択肢となることに期待したいです。この構成は趣…"
tags:
  - "clippings"
---
### 要約
Next.jsのStandaloneモードを活用し、AWS Lambda + API Gatewayというサーバーレス構成でアプリケーションを公開する方法についての解説記事です。

### 要点
- **構成のメリット**:
  - サーバーレスで運用コストを低減（リクエストがない時は料金ゼロ）。
  - AWS Lambda Web Adapterを利用することで、コンテナベースのWebアプリを最小限の変更で移植可能。
- **主な設定手順**:
  - `next.config.js`に`output: 'standalone'`を追加。
  - `Dockerfile`にて`aws-lambda-adapter`をインストール。
  - ベースイメージを`amazon/aws-lambda-nodejs`にすることで、Lambdaのイメージキャッシュ効率を高めコールドスタートを短縮。
- **運用上の注意点**:
  - Lambdaのファイルシステム制限対策として、`.next`ディレクトリを`/tmp`へシンボリックリンクさせる必要がある。
  - 性能向上のため、CloudFrontを前段に配置しキャッシュを活用することを推奨。