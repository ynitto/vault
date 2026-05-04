---
title: "起動タイプがEC2であるECSを高速化させるためのtips"
source: "https://qiita.com/yoshii0110/items/8a780510f312a2b7c78e"
author:
  - "[[yoshii0110]]"
published: 2022-06-21
created: 2026-04-30
description: "概要 今回は、AWSの起動タイプがEC2であるAmazon Elastic Container Service - ECSをより高速化させるためのtipsについて記事にしました。 例えば、タスクの起動を高速化したい・・・だったり、クラスタの自動スケーリングを高速化..."
tags:
  - "clippings"
---
### 記事の要約
本記事は、AWSのEC2起動タイプにおけるAmazon ECSのパフォーマンスを最適化し、タスクの起動やデプロイを高速化するための実践的な設定Tipsを解説しています。

### 高速化の要点

#### 1. タスク起動の高速化
* **コンテナイメージのキャッシュ**: `ECS_IMAGE_PULL_BEHAVIOR`を`once`または`prefer-cached`に設定し、リモートからのプル時間を削減。
* **サービス設計**: 大規模なサービスを細分化し、小規模なサービスを並行してプロビジョニングさせる。
* **ロードバランサー設定**: 
    * ヘルスチェックの閾値を緩和（`HealthCheckIntervalSeconds: 5`, `HealthyThresholdCount: 2`）。
    * コネクションドレイン時間を最適化（`deregistration_delay.timeout_seconds: 5`）。
* **SIGTERM応答性**: アプリケーションの終了処理時間に合わせて`ECS_CONTAINER_STOP_TIMEOUT`を調整。

#### 2. クラスター自動スケーリングの高速化
* **キャパシティプロバイダー**: `minimumScalingStepSize`を調整し、一度のスケールアウトで確保するインスタンス数を最適化。
* **ウォームアップ期間**: インスタンスのウォームアップ時間をデフォルト（300秒）より短縮し、スケーリングの応答性を向上。

#### 3. デプロイの高速化
* **デプロイ設定**: `minimumHealthyPercent`と`maximumPercent`を適切に調整（例: 50% / 200%）することで、タスク入れ替えの効率を上げる。
