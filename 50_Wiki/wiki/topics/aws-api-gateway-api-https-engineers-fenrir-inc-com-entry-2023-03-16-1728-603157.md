---
title: "サーバーレスなデータ収集APIを作るときの困りポイント"
type: "topic"
tags:
  - "aws"
  - "api-gateway"
  - "authentication"
  - "security"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/サーバーレスなデータ収集APIを作るときの困りポイント.md"
summary: "AWS API Gateway、Kinesis、S3を組み合わせたデータ収集APIの構築において、実務で発生しやすい課題とその解決策を解説した記事です。"
---

# サーバーレスなデータ収集APIを作るときの困りポイント

## 概要

AWS API Gateway、Kinesis、S3を組み合わせたデータ収集APIの構築において、実務で発生しやすい課題とその解決策を解説した記事です。

*発行: 2023-03-16 / [[aws-api-gateway-api-https-engineers-fenrir-inc-com-entry-2023-03-16-1728-603157]]*

## 主要なトピック

- [[aws]]
- [[api-gateway]]
- [[authentication]]
- [[security]]

## 詳細

- AWS API Gateway、Kinesis、S3を組み合わせたデータ収集APIの構築において、実務で発生しやすい課題とその解決策を解説した記事です。
- 要点まとめ
- **データの区切り問題**
- マッピングテンプレート内で改行変数を定義することで、S3出力時に改行区切りを付与し、パースを容易にする。
- **ファイル名の時刻重複**
- Kinesis Firehoseが出力するファイル名はシャードごとに作成されるため、時刻だけで一意性を判断せず、UUID等の識別子を考慮する。
- **API保護の選択肢**
- 用途に応じて以下の手法でセキュリティを強化する：
- **OpenAPI**: スキーマバリデーション

*発行: 2023-03-16 / [[aws-api-gateway-api-https-engineers-fenrir-inc-com-entry-2023-03-16-1728-603157]]*

## 関連テーマ

- [[aws]]
- [[api-gateway]]
- [[authentication]]
- [[security]]

## 出典

- `60_Resources/サーバーレスなデータ収集APIを作るときの困りポイント.md`
- https://engineers.fenrir-inc.com/entry/2023/03/16/172808
