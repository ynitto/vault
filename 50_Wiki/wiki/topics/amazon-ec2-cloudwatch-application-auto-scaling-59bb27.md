---
title: "Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling"
type: "topic"
tags:
  - "amazon-ec2"
  - "cloudwatch"
  - "observability"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling.md"
summary: "Application Auto Scaling: ステップスケーリングの概要"
---

# Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling

## 概要

Application Auto Scaling: ステップスケーリングの概要

## 主要なトピック

- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]

## 詳細

- ステップスケーリングは、CloudWatch アラームの違反状況に応じて、段階的に容量を増減させるスケーリングポリシーです。
- 主な仕組みとポイント
- **段階的な調整**: アラーム違反の程度に応じて、異なるスケーリング量（ステップ調整値）を定義可能。
- **調整タイプ**: 以下の3種類から選択可能。
- `ChangeInCapacity`: 現在の容量を絶対値で増減。
- `ExactCapacity`: 容量を指定の数値に直接変更。
- `PercentChangeInCapacity`: 現在の容量に対する割合（%）で増減。
- **クールダウン期間**: 連続するスケーリングアクティビティの間隔を制御し、急激な変動や「フラッピング（過剰な増減の繰り返し）」を防止。
- **考慮事項**:

## 関連テーマ

- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling.md`
- https://docs.aws.amazon.com/ja_jp/autoscaling/application/userguide/step-scaling-policy-overview.html
