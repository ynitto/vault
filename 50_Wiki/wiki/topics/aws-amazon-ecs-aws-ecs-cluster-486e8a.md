---
title: "AWS ECS Cluster Auto ScalingがGAになったのでやってみた #reinvent"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ec2"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/AWS ECS Cluster Auto ScalingがGAになったのでやってみた reinvent.md"
summary: "AWS ECS Cluster Auto Scaling の概要"
---

# AWS ECS Cluster Auto ScalingがGAになったのでやってみた #reinvent

## 概要

AWS ECS Cluster Auto Scaling の概要

*発行: 2026-05-20 / [[aws-amazon-ecs-aws-ecs-cluster-486e8a]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]

## 詳細

- ECSクラスターのオートスケーリング機能が一般公開されました。キャパシティプロバイダーを活用することで、ワークロードに応じた柔軟かつ迅速なスケーリングが可能になります。
- 主な新機能
- **Managed scaling (スケーリング管理)**
- 「Capacity Provider Reservation」メトリックを用いた最適化により、迅速なスケールアウトを実現。
- **Managed instance termination protection (インスタンス終了保護)**
- スケールイン時に実行中のコンテナを保護し、中断を最小限に抑えます。
- 運用のメリット
- **ゼロからのスケール**：予備容量の予約設定により、新しいインスタンスの起動を待たずにコンテナを実行可能。
- **可用性の向上**：スケールイン時の意図しないコンテナ終了を防ぎ、運用の信頼性を高めます。

*発行: 2026-05-20 / [[aws-amazon-ecs-aws-ecs-cluster-486e8a]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]

## 出典

- `60_Resources/AWS ECS Cluster Auto ScalingがGAになったのでやってみた reinvent.md`
- https://dev.classmethod.jp/articles/aws-ecs-cluster-auto-scaling/
