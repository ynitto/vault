---
title: "AWS初心者がCloudWatch Logs Insightsを使ってみた"
type: "topic"
tags:
  - "cloudwatch"
  - "observability"
  - "kesoji"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/AWS初心者がCloudWatch Logs Insightsを使ってみた.md"
summary: "CloudWatch Logs Insightsの要約"
---

# AWS初心者がCloudWatch Logs Insightsを使ってみた

## 概要

CloudWatch Logs Insightsの要約

*発行: 2020-10-08 / [[cloudwatch-observability-aws-cloudwatch-logs-c2a219]]*

## 主要なトピック

- [[cloudwatch]]
- [[observability]]
- [[kesoji]]

## 詳細

- AWSのCloudWatch Logs Insightsは、ログデータを効率的に検索・分析できる機能です。SQLライクな独自構文を使用し、スキャンしたデータ量に応じた従量課金制で利用可能です。
- 主要な機能とポイント
- **クエリの基本操作**
- `fields`: 取得するフィールド（カラム）を指定
- `filter`: 抽出条件の指定（例: `like` で文字列検索）
- `sort`: 並び替え（`asc`/`desc`）
- `limit`: 取得件数の制限
- `stats`: `count`, `avg`, `sum` などの集計関数
- `parse`: 正規表現等を用いてログから特定項目を抽出

*発行: 2020-10-08 / [[cloudwatch-observability-aws-cloudwatch-logs-c2a219]]*

## 関連テーマ

- [[cloudwatch]]
- [[observability]]
- [[kesoji]]

## 出典

- `60_Resources/AWS初心者がCloudWatch Logs Insightsを使ってみた.md`
- https://qiita.com/suuu/items/8387df88f134348f22c7
