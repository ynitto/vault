---
title: "ECS Cluster Auto Scalingについて調べたこと"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ec2"
  - "rch1223"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECS Cluster Auto Scalingについて調べたこと.md"
summary: "Amazon ECSにおける「Cluster Auto Scaling (CAS)」の仕組み、設定、および挙動に関する技術メモです。"
---

# ECS Cluster Auto Scalingについて調べたこと

## 概要

Amazon ECSにおける「Cluster Auto Scaling (CAS)」の仕組み、設定、および挙動に関する技術メモです。

*発行: 2020-05-25 / [[aws-amazon-ecs-ecs-cluster-auto-77fe05]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[rch1223]]

## 詳細

- Amazon ECSにおける「Cluster Auto Scaling (CAS)」の仕組み、設定、および挙動に関する技術メモです。
- 主な要点
- **CAS導入のメリット**
- ECSタスク数に合わせてASG（Auto Scaling Group）を自動スケールできる。
- ECSタスクとコンテナインスタンスの管理を統合可能。
- **主要な設定項目**
- **マネージドスケーリング**: ECSがASGのスケールを自動制御。
- **ターゲットキャパシティー**: インスタンス利用率の目標値（例: 80%指定なら20%を余剰として確保）。
- **マネージドターミネーション保護**: タスク終了までインスタンス停止を待機。

*発行: 2020-05-25 / [[aws-amazon-ecs-ecs-cluster-auto-77fe05]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[rch1223]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECS Cluster Auto Scalingについて調べたこと.md`
- https://qiita.com/rch1223/items/b9dbbfe7099f8697690c
