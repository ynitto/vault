---
title: "え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "cloudwatch"
  - "observability"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾.md"
summary: "AWSの各サービスを利用する際に、意図せず高額なコストが発生してしまうリスクと、その対策方法を理論値ベースで解説した記事です。"
---

# え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾

## 概要

AWSの各サービスを利用する際に、意図せず高額なコストが発生してしまうリスクと、その対策方法を理論値ベースで解説した記事です。

*発行: 2020-02-28 / [[aws-lambda-aws-5-3-d83259]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[cloudwatch]]
- [[observability]]

## 詳細

- AWSの各サービスを利用する際に、意図せず高額なコストが発生してしまうリスクと、その対策方法を理論値ベースで解説した記事です。
- 注意点
- 提示金額は検証時点（2020年2月）の東京リージョンの理論値。
- サービスそのものが悪いわけではなく、設定や設計によるコスト管理の重要性を説くもの。
- コスト管理が必要な主要サービスと対策
- 1. AWS Lambda
- **リスク**: 無限ループ等による意図しない大量実行・同時実行。
- **対策**: `Invocations`メトリクスの監視、異常時のアラート設定、同時実行数の制限、Saving Plansの活用。
- 2. Amazon CloudWatch（Alarm）

*発行: 2020-02-28 / [[aws-lambda-aws-5-3-d83259]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[cloudwatch]]
- [[observability]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾.md`
- https://dev.classmethod.jp/articles/5-ways-to-spend-cost-on-aws-v3/
