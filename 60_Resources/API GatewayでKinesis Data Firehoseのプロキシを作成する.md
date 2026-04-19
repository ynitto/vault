---
original_source: 00_Inbox/Clippings/API GatewayでKinesis Data Firehoseのプロキシを作成する.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, aws, 2026-04]
---

---
title: "API GatewayでKinesis Data Firehoseのプロキシを作成する"
source: "https://techblog.techfirm.co.jp/entry/create-kinesis-firehose-proxy-with-api-gateway"
author:
  - "[[tfi_takashi_sato]]"
published: 2023-04-10
created: 2026-04-19
description: "はじめに 以前、Kinesis Data Streamsと連携させるブログを書きましたが、今回はKinesis Data Firehoseでプロキシを作成、S3にデータ保管するパターンを記載します。 API GatewayでKinesis Data Streamsのプロキシを作成する - Techfirm Cloud Architect Blog 同じユースケース（センサーデータなど定期的なデータ収集、最終的には集計・分析する）でも、リアルタイム性がそこまで必要でなければ、こちらのパターンの方がさらに簡単にやりたいことが実現できると思います。 構築 S3の準備 Kinesis Data Fir…"
tags:
  - "clippings"
---
### 内容の要約
本記事では、API Gatewayをプロキシとして利用し、受信したデータをKinesis Data Firehose経由でS3バケットへ自動的に保存する構築手順を紹介しています。

### 構築のポイント
- **目的**: センサーデータ等の定期的な収集・保存。
- **メリット**: リアルタイム性が不要な場合、Kinesis Data Streamsを使用するよりも低コストかつ簡単にS3連携が実現可能。
- **主要な設定内容**:
  - **S3**: 送信先バケットの準備。
  - **Firehose**: デフォルト設定で配信ストリームを作成。
  - **IAM**: API GatewayがFirehoseへアクセスできるよう許可ポリシーを追加。
  - **API Gateway**: `POST`メソッドを作成し、マッピングテンプレートを用いて入力データをFirehoseの`PutRecord`形式へ変換。
- **確認方法**: テストリクエストを送信後、S3バケット内に該当オブジェクトが生成されていることを確認する。