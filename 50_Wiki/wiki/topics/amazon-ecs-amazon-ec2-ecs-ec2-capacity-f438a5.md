---
title: "ECS on EC2におけるスケーリングの辛みを「Capacity Provider」で解決する"
type: "topic"
tags:
  - "amazon-ecs"
  - "amazon-ec2"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ECS on EC2におけるスケーリングの辛みを「Capacity Provider」で解決する.md"
summary: "ECS on EC2において、これまで手動設定が必要だったEC2のスケーリングを、ECSの「Capacity Provider」および「Cluster A…"
---

# ECS on EC2におけるスケーリングの辛みを「Capacity Provider」で解決する

## 概要

ECS on EC2において、これまで手動設定が必要だったEC2のスケーリングを、ECSの「Capacity Provider」および「Cluster Auto Scaling (CAS)」を利用することで自動化・効率化する手法の検証記事。

*発行: 2020-03-31 / [[amazon-ecs-amazon-ec2-ecs-ec2-capacity-f438a5]]*

## 主要なトピック

- [[amazon-ecs]]
- [[amazon-ec2]]

## 詳細

- ECS on EC2において、これまで手動設定が必要だったEC2のスケーリングを、ECSの「Capacity Provider」および「Cluster Auto Scaling (CAS)」を利用することで自動化・効率化する手法の検証記事。
- 要点まとめ
- **ECS on EC2の課題**
- タスクとEC2の両方のスケーリングを管理する必要があり、運用難易度が高かった。
- **解決策：Capacity ProviderとCAS**
- タスクのスケーリングのみ意識すれば、連動してEC2も自動で増減する。
- AutoScalingGroupの「希望するキャパシティ」が自動調整される。
- **検証結果**
- **スケールアウト**: EC2の追加を含め約3分で完了。

*発行: 2020-03-31 / [[amazon-ecs-amazon-ec2-ecs-ec2-capacity-f438a5]]*

## 関連テーマ

- [[amazon-ecs]]
- [[amazon-ec2]]

## 出典

- `60_Resources/ECS on EC2におけるスケーリングの辛みを「Capacity Provider」で解決する.md`
- https://dev.classmethod.jp/articles/ecs_on_ec2_capacity_provider/
