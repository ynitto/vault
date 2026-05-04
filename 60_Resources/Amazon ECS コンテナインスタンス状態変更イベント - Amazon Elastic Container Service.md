---
title: "Amazon ECS コンテナインスタンス状態変更イベント - Amazon Elastic Container Service"
source: "https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs_container_instance_events.html"
author:
published:
created: 2026-05-01
description: "Amazon ECS コンテナインスタンス状態変更イベントについて説明します。"
tags:
  - "clippings"
---
### Amazon ECS コンテナインスタンス状態変更イベントの概要
このドキュメントでは、Amazon ECS コンテナインスタンスの状態が変化した際に発行されるイベントの詳細と、その発生トリガーについて解説しています。

### イベント発生の主な要因
以下の操作や状態の変化によりイベントが生成されます。
* **タスクの実行・停止:** StartTask, RunTask, StopTask の実行や、サービススケジューラによるタスク管理。
* **コンテナエージェントによる報告:** タスクの状態変化（RUNNING から STOPPED への移行など）の通知。
* **インスタンスのライフサイクル:** コンテナインスタンスの登録・登録解除や、EC2 インスタンスの停止。
* **エージェントのステータス変化:** 初回登録時や、バックエンドとの接続・切断。
* **構成の更新:** コンテナエージェントのバージョンアップに伴う情報変更。

### 注意点
* **エージェントの切断:** 1時間に数回発生する接続・切断イベントは通常の動作であり、問題ではありません。

### イベント構造
* イベントは `detail` セクションに `ContainerInstance` オブジェクトの情報を含み、CPU・メモリなどのリソース使用状況や属性情報が含まれます。
