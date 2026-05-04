---
title: "ECS service desire count get resets by Auto Scaling"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ec2"
  - "farp332-78622-gold-badges1515"
  - "brother-andy-13144-bronze"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECS service desire count get resets by Auto Scaling.md"
summary: "AWS ECS Fargateで自動スケーリングを設定している環境において、CLIコマンドでDesired Countを0にしても、自動スケーリング設定が…"
---

# ECS service desire count get resets by Auto Scaling

## 概要

AWS ECS Fargateで自動スケーリングを設定している環境において、CLIコマンドでDesired Countを0にしても、自動スケーリング設定がすぐに値を元に戻してしまい、タスクを完全に停止できないという問題。

*発行: 2020-09-21 / [[aws-amazon-ecs-ecs-service-desire-d145d6]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[farp332-78622-gold-badges1515]]
- [[brother-andy-13144-bronze]]

## 詳細

- AWS ECS Fargateで自動スケーリングを設定している環境において、CLIコマンドでDesired Countを0にしても、自動スケーリング設定がすぐに値を元に戻してしまい、タスクを完全に停止できないという問題。
- 解決のための重要なポイント
- **自動スケーリングの仕様**：自動スケーリングが有効な場合、ECSサービスの希望タスク数は自動スケーリングポリシーによって管理されるため、個別の`update-service`コマンドは上書きされます。
- **推奨される対応策**：
- **ポリシーの調整**：スケーリングターゲットの`MinCapacity`と`MaxCapacity`を0に設定し、`SuspendedState`でスケーリングアクションを一時停止することで、意図的にスケールインさせます。
- **構成の見直し**：自動スケーリング自体を利用しない構成に変更するか、タスク停止のスケジュールに合わせて自動スケーリング設定そのものを動的に更新（無効化）する必要があります。

*発行: 2020-09-21 / [[aws-amazon-ecs-ecs-service-desire-d145d6]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[farp332-78622-gold-badges1515]]
- [[brother-andy-13144-bronze]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECS service desire count get resets by Auto Scaling.md`
- https://stackoverflow.com/questions/63992903/ecs-service-desire-count-get-resets-by-auto-scaling
