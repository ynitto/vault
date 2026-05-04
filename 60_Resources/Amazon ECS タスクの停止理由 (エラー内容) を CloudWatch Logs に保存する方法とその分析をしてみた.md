---
title: "Amazon ECS タスクの停止理由 (エラー内容) を CloudWatch Logs に保存する方法とその分析をしてみた"
source: "https://dev.classmethod.jp/articles/stop-ecs-task-reason-cloudwatch-logs/"
author:
  - "[[平井裕二]]"
published: 2026-05-20
created: 2026-05-01
description: "AWS FargateなどのECSタスクの停止理由を確認する場合、タスクが停止して1時間を過ぎると、コンソール上では確認できません。過去にさかのぼって確認できるよう、CloudWatch Logsに保存する方法について解説します。"
tags:
  - "clippings"
---
### 概要
AWS ECSタスクの停止理由（エラー内容）は、標準ではECSコンソール上で1時間しか確認できません。本記事では、EventBridgeとCloudFormationを活用して、タスクの停止イベントをCloudWatch Logsに永続的に保存・分析する方法を解説しています。

### 要点
- **課題の解決**：タスク停止時のイベント情報をCloudWatch Logsに自動転送することで、1時間経過後も過去の停止理由を確認可能にする。
- **実装方法**：
    - CloudFormationテンプレートを利用し、EventBridgeルールとCloudWatchロググループをデプロイ。
    - EventBridgeで「ECS Task State Change（STOPPED）」を検知してロググループへ保存。
- **カスタマイズ性**：
    - クラスターやタスク定義単位でのフィルタリングが可能。
    - 異常終了（exitCodeが0以外）のみを抽出するイベントパターン設定にも対応。
- **分析手法**：
    - CloudWatch Logs Insightsを使用して、特定サービスのログを検索し、停止理由やexitCodeを効率的に分析する方法を紹介。
