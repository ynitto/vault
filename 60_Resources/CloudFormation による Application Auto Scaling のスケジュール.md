---
title: "CloudFormation による Application Auto Scaling のスケジュール"
source: "https://tech.quartetcom.co.jp/2022/07/28/ecs-scheduled-auto-scaling/"
author:
  - "[[真鍋 直泰]]"
published: Thu
created: 2026-05-01
description: "はじめに今回は小ネタです。Application Auto Scaling のスケジュールされたアクションの例 - Application Auto Scaling などでは aws-cli による Appliction Auco Scaling のスケジュール方法が示されていました。しかし、CloudForma..."
tags:
  - "clippings"
---
### 概要
CloudFormationを用いて、ECSサービスの「スケジュールされたオートスケーリング」を設定する方法について解説した技術メモです。

### 要点
- **目的**: 特定の日時（毎月1日3時～2日18時）にタスク数を固定し、それ以外の期間はCloudWatch Alarmに基づいた動的なスケーリングを行う。
- **CloudFormationの活用**: `AWS::ApplicationAutoScaling::ScalableTarget` リソースの `ScheduledActions` プロパティを使用して、スケーリングスケジュールを定義する。
- **Timezone指定の利便性**: EventBridgeとは異なり、`Timezone` プロパティでタイムゾーン（例: `Asia/Tokyo`）を指定可能。IANAのタイムゾーンIDを使用する必要がある。
- **設定確認**: スケジュール設定はAWSマネジメントコンソールからは確認できない場合があるため、`aws application-autoscaling describe-scheduled-actions` コマンドで確認する。