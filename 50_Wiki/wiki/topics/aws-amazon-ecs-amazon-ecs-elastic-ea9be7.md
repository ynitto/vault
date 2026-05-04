---
title: "Amazon ECS コンテナインスタンス状態変更イベント - Amazon Elastic Container Service"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ec2"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon ECS コンテナインスタンス状態変更イベント - Amazon Elastic Container Service.md"
summary: "Amazon ECS コンテナインスタンス状態変更イベントの概要"
---

# Amazon ECS コンテナインスタンス状態変更イベント - Amazon Elastic Container Service

## 概要

Amazon ECS コンテナインスタンス状態変更イベントの概要

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[performance]]

## 詳細

- このドキュメントでは、Amazon ECS コンテナインスタンスの状態が変化した際に発行されるイベントの詳細と、その発生トリガーについて解説しています。
- イベント発生の主な要因
- 以下の操作や状態の変化によりイベントが生成されます。
- **タスクの実行・停止:** StartTask, RunTask, StopTask の実行や、サービススケジューラによるタスク管理。
- **コンテナエージェントによる報告:** タスクの状態変化（RUNNING から STOPPED への移行など）の通知。
- **インスタンスのライフサイクル:** コンテナインスタンスの登録・登録解除や、EC2 インスタンスの停止。
- **エージェントのステータス変化:** 初回登録時や、バックエンドとの接続・切断。
- **構成の更新:** コンテナエージェントのバージョンアップに伴う情報変更。
- 注意点

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[performance]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon ECS コンテナインスタンス状態変更イベント - Amazon Elastic Container Service.md`
- https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs_container_instance_events.html
