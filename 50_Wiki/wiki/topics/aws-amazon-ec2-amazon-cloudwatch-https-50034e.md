---
title: "Amazon CloudWatch でのアラームの使用"
type: "topic"
tags:
  - "aws"
  - "amazon-ec2"
  - "cloudwatch"
  - "observability"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Amazon CloudWatch でのアラームの使用.md"
summary: "Amazon CloudWatch アラームの概要"
---

# Amazon CloudWatch でのアラームの使用

## 概要

Amazon CloudWatch アラームの概要

## 主要なトピック

- [[aws]]
- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]

## 詳細

- CloudWatch アラームは、メトリクスを監視し、しきい値超過時に通知送信やリソースの自動操作を行う機能です。
- 主なアラームの種類
- **メトリクスアラーム**: 単一または複数のメトリクス（数式を含む）を監視。
- **PromQL アラーム**: Prometheus クエリ言語を使用してメトリクスを監視。
- **複合アラーム**: 他のアラーム状態を組み合わせ、アラームノイズを低減。
- 特徴と運用のポイント
- **柔軟なアクション**: 通知（SNS）、EC2/Auto Scaling 操作、調査（Investigations）の開始などが可能。
- **タグ付け対応**: Metrics Insights クエリを使用し、リソースタグに基づいた動的な監視が可能。
- **状態管理**: INSUFFICIENT_DATA（データ不足）、ALARM（アラーム状態）、OKの3状態で管理。

## 関連テーマ

- [[aws]]
- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]

## 出典

- `60_Resources/Amazon CloudWatch でのアラームの使用.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html
