---
title: "ECSタスクの異常終了をCloudFormationでメトリクスにして死活監視"
type: "topic"
tags:
  - "cloudformation"
  - "cloudwatch"
  - "observability"
  - "k-goto-id-go-to-k"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSタスクの異常終了をCloudFormationでメトリクスにして死活監視.md"
summary: "ECSタスクの異常終了を可視化し、アラート通知を行うための構成についての解説です。CloudWatch LogsのメトリクスフィルターとEventBrid…"
---

# ECSタスクの異常終了をCloudFormationでメトリクスにして死活監視

## 概要

ECSタスクの異常終了を可視化し、アラート通知を行うための構成についての解説です。CloudWatch LogsのメトリクスフィルターとEventBridgeを活用します。

*発行: 2022-02-03 / [[cloudformation-cloudwatch-ecs-cloudformation-https-cfee1c]]*

## 主要なトピック

- [[cloudformation]]
- [[cloudwatch]]
- [[observability]]
- [[k-goto-id-go-to-k]]

## 詳細

- ECSタスクの異常終了を可視化し、アラート通知を行うための構成についての解説です。CloudWatch LogsのメトリクスフィルターとEventBridgeを活用します。
- 要点
- **仕組み**: EventBridgeでECSタスクのイベントをCloudWatch Logsに転送し、メトリクスフィルターで異常終了を抽出してカスタムメトリクスを作成します。
- **主なメリット**:
- ダッシュボードで異常終了の履歴を可視化できる。
- メトリクスに基づいた柔軟なアラーム設定が可能。
- **実装の構成要素**:
- **EventBridge**: タスクのイベントをログへ転送。
- **メトリクスフィルター**: `stoppedReason`などを条件に異常終了のみを数値化。

*発行: 2022-02-03 / [[cloudformation-cloudwatch-ecs-cloudformation-https-cfee1c]]*

## 関連テーマ

- [[cloudformation]]
- [[cloudwatch]]
- [[observability]]
- [[k-goto-id-go-to-k]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSタスクの異常終了をCloudFormationでメトリクスにして死活監視.md`
- https://go-to-k.hatenablog.com/entry/2022/01/30/045205
