---
title: "[小ネタ]ECSタスクの異常終了を検知するEventBridgeイベントパターン"
type: "topic"
tags:
  - "amazon-ecs"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/小ネタECSタスクの異常終了を検知するEventBridgeイベントパターン.md"
summary: "ECSタスクの異常終了をAmazon EventBridgeで効率的に検知・通知するための設定手法の解説です。"
---

# [小ネタ]ECSタスクの異常終了を検知するEventBridgeイベントパターン

## 概要

ECSタスクの異常終了をAmazon EventBridgeで効率的に検知・通知するための設定手法の解説です。

*発行: 2020-12-31 / [[amazon-ecs-ecs-eventbridge-https-dev-classmethod-jp-articles-ecs-state-c-e788f7]]*

## 主要なトピック

- [[amazon-ecs]]

## 詳細

- ECSタスクの異常終了をAmazon EventBridgeで効率的に検知・通知するための設定手法の解説です。
- 要点
- **イベントの特定**: `ECS Task State Change` イベントを利用し、特定のステータス変化をキャッチする。
- **フィルタリングの重要性**: 不要な通知を避けるため、イベントパターンで条件を絞り込む。
- **推奨されるフィルタリング条件**:
- `lastStatus`: `STOPPED` であること。
- `exitCode`: `0` 以外（正常終了を除外）。
- `stoppedReason`: ローリングアップデート時の「Scaling activity...」を除外。
- **柔軟な設定**: `clusterArn` を指定して特定クラスタのみ監視することも、指定せずにリージョン全体を対象とすることも可能。

*発行: 2020-12-31 / [[amazon-ecs-ecs-eventbridge-https-dev-classmethod-jp-articles-ecs-state-c-e788f7]]*

## 関連テーマ

- [[amazon-ecs]]

## 出典

- `60_Resources/小ネタECSタスクの異常終了を検知するEventBridgeイベントパターン.md`
- https://dev.classmethod.jp/articles/ecs-state-change/
