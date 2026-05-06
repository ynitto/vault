---
title: "Amazon ECS タスクの停止理由 (エラー内容) を CloudWatch Logs に保存する方法とその分析をしてみた"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "cloudformation"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../../60_Resources/Amazon ECS タスクの停止理由 (エラー内容) を CloudWatch Logs に保存する方法とその分析をしてみた.md"
summary: "AWS ECSタスクの停止理由（エラー内容）は、標準ではECSコンソール上で1時間しか確認できません。本記事では、EventBridgeとCloudFor…"
---

# Amazon ECS タスクの停止理由 (エラー内容) を CloudWatch Logs に保存する方法とその分析をしてみた

## 概要

AWS ECSタスクの停止理由（エラー内容）は、標準ではECSコンソール上で1時間しか確認できません。本記事では、EventBridgeとCloudFormationを活用して、タスクの停止イベントをCloudWatch Logsに永続的に保存・分析する方法を解説しています。

*発行: 2026-05-20 / [[aws-amazon-ecs-amazon-ecs-cloudwatch-c9c0fc]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[cloudformation]]
- [[cloudwatch]]

## 詳細

- AWS ECSタスクの停止理由（エラー内容）は、標準ではECSコンソール上で1時間しか確認できません。本記事では、EventBridgeとCloudFormationを活用して、タスクの停止イベントをCloudWatch Logsに永続的に保存・分析する方法を解説しています。
- 要点
- **課題の解決**：タスク停止時のイベント情報をCloudWatch Logsに自動転送することで、1時間経過後も過去の停止理由を確認可能にする。
- **実装方法**：
- CloudFormationテンプレートを利用し、EventBridgeルールとCloudWatchロググループをデプロイ。
- EventBridgeで「ECS Task State Change（STOPPED）」を検知してロググループへ保存。
- **カスタマイズ性**：
- クラスターやタスク定義単位でのフィルタリングが可能。
- 異常終了（exitCodeが0以外）のみを抽出するイベントパターン設定にも対応。

*発行: 2026-05-20 / [[aws-amazon-ecs-amazon-ecs-cloudwatch-c9c0fc]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[cloudformation]]
- [[cloudwatch]]

## 出典

- `../../60_Resources/Amazon ECS タスクの停止理由 (エラー内容) を CloudWatch Logs に保存する方法とその分析をしてみた.md`
- https://dev.classmethod.jp/articles/stop-ecs-task-reason-cloudwatch-logs/
