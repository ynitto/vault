---
title: "起動タイプがEC2であるECSを高速化させるためのtips"
type: "topic"
tags:
  - "performance"
  - "yoshii0110"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/起動タイプがEC2であるECSを高速化させるためのtips.md"
summary: "本記事は、AWSのEC2起動タイプにおけるAmazon ECSのパフォーマンスを最適化し、タスクの起動やデプロイを高速化するための実践的な設定Tipsを解…"
---

# 起動タイプがEC2であるECSを高速化させるためのtips

## 概要

本記事は、AWSのEC2起動タイプにおけるAmazon ECSのパフォーマンスを最適化し、タスクの起動やデプロイを高速化するための実践的な設定Tipsを解説しています。

*発行: 2022-06-21 / [[performance-yoshii0110-ec2-ecs-tips-3e3b48]]*

## 主要なトピック

- [[performance]]
- [[yoshii0110]]

## 詳細

- 本記事は、AWSのEC2起動タイプにおけるAmazon ECSのパフォーマンスを最適化し、タスクの起動やデプロイを高速化するための実践的な設定Tipsを解説しています。
- 高速化の要点
- 1. タスク起動の高速化
- **コンテナイメージのキャッシュ**: `ECS_IMAGE_PULL_BEHAVIOR`を`once`または`prefer-cached`に設定し、リモートからのプル時間を削減。
- **サービス設計**: 大規模なサービスを細分化し、小規模なサービスを並行してプロビジョニングさせる。
- **ロードバランサー設定**:
- ヘルスチェックの閾値を緩和（`HealthCheckIntervalSeconds: 5`, `HealthyThresholdCount: 2`）。
- コネクションドレイン時間を最適化（`deregistration_delay.timeout_seconds: 5`）。
- **SIGTERM応答性**: アプリケーションの終了処理時間に合わせて`ECS_CONTAINER_STOP_TIMEOUT`を調整。

*発行: 2022-06-21 / [[performance-yoshii0110-ec2-ecs-tips-3e3b48]]*

## 関連テーマ

- [[performance]]
- [[yoshii0110]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/起動タイプがEC2であるECSを高速化させるためのtips.md`
- https://qiita.com/yoshii0110/items/8a780510f312a2b7c78e
