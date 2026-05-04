---
title: "ウン十万接続のECSサービスを平和にアップデートしたい"
type: "topic"
tags:
  - "networking"
  - "websocket"
  - "mxg"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ウン十万接続のECSサービスを平和にアップデートしたい.md"
summary: "ECS上で長時間接続（WebSocket）を保持する「streamサーバ」をデプロイする際、AWSのデフォルトの停止処理では予期せぬ切断が発生していました…"
---

# ウン十万接続のECSサービスを平和にアップデートしたい

## 概要

ECS上で長時間接続（WebSocket）を保持する「streamサーバ」をデプロイする際、AWSのデフォルトの停止処理では予期せぬ切断が発生していました。これを回避するため、ALBのターゲットグループの状態をアプリ側でポーリングし、適切なタイミングで独自にグレースフルシャットダウンを行うことで、平和なデプロイを実現した事例です。

*発行: 2023-07-19 / [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]*

## 主要なトピック

- [[networking]]
- [[websocket]]
- [[mxg]]

## 詳細

- ECS上で長時間接続（WebSocket）を保持する「streamサーバ」をデプロイする際、AWSのデフォルトの停止処理では予期せぬ切断が発生していました。これを回避するため、ALBのターゲットグループの状態をアプリ側でポーリングし、適切なタイミングで独自にグレースフルシャットダウンを行うことで、平和なデプロイを実現した事例です。
- 要点
- **課題**: ECSのデプロイ時、SIGTERM受信後にALBが一定時間（約8秒）で強制的に接続を切断してしまうため、WebSocket接続がバッサリ切られ、クライアントが一斉に再接続してくる負荷が発生していた。
- **原因**: ALBはECSのStopTimeout（最大120秒）を関知せず、独自にコネクションを終了させる仕様である。
- **解決策**:
- アプリケーションコード内で`DescribeTargetHealth`を定期的にポーリングする。
- ターゲット状態が「draining」になったことを検知する。
- 設定した猶予期間内に、自発的にWebSocket接続を段階的に切断する実装に変更した。
- **成果**: 接続の切断が急激なスパイクにならず、グラフ上で緩やかに推移するようになり、デプロイ時のサービス負荷を抑えることに成功した。

*発行: 2023-07-19 / [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]*

## 関連テーマ

- [[networking]]
- [[websocket]]
- [[mxg]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ウン十万接続のECSサービスを平和にアップデートしたい.md`
- https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown
