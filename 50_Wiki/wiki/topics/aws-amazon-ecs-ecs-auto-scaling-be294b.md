---
title: "ECSにおけるAuto Scaling Policyの「ターゲットスケーリング」と「ステップスケーリング」について"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ec2"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ECSにおけるAuto Scaling Policyの「ターゲットスケーリング」と「ステップスケーリング」について.md"
summary: "ECS Auto Scaling：ターゲット追跡 vs ステップスケーリング"
---

# ECSにおけるAuto Scaling Policyの「ターゲットスケーリング」と「ステップスケーリング」について

## 概要

ECS Auto Scaling：ターゲット追跡 vs ステップスケーリング

*発行: 2021-12-06 / [[aws-amazon-ecs-ecs-auto-scaling-be294b]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[cloudwatch]]

## 詳細

- 本記事は、AWS ECSにおける2つの主要なオートスケーリング方式の違いと使い分けを解説しています。
- 主な違い
- **ターゲット追跡スケーリング**
- 指定したメトリクス値（例：CPU 60%）を維持するように自動調整。
- 管理が容易で、通常の運用にはこちらを推奨。
- **ステップスケーリング**
- 閾値に応じて段階的にタスク数を増減させる。
- CloudWatch Alarmを自前で定義するため、より細かな調整が可能。
- 使い分けのポイント

*発行: 2021-12-06 / [[aws-amazon-ecs-ecs-auto-scaling-be294b]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[cloudwatch]]

## 出典

- `60_Resources/ECSにおけるAuto Scaling Policyの「ターゲットスケーリング」と「ステップスケーリング」について.md`
- https://zenn.dev/techno_koki/articles/082e7bbe1a3605
