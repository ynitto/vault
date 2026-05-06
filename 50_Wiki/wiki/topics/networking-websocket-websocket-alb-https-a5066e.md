---
title: "websocket ALB"
type: "topic"
tags:
  - "networking"
  - "websocket"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/websocket ALB.md"
summary: "本スクラップは、WebSocketをAWSのApplication Load Balancer (ALB) で運用する際の構成および注意点をまとめたもので…"
---

# websocket ALB

## 概要

本スクラップは、WebSocketをAWSのApplication Load Balancer (ALB) で運用する際の構成および注意点をまとめたものです。

*発行: 2024/04/03にコメント追加 / [[networking-websocket-websocket-alb-https-a5066e]]*

## 主要なトピック

- [[networking]]
- [[websocket]]

## 詳細

- 本スクラップは、WebSocketをAWSのApplication Load Balancer (ALB) で運用する際の構成および注意点をまとめたものです。
- **ヘルスチェックの実装**
- `/api/health` エンドポイントを作成し、ALBからの死活監視に応答できるようにする。
- **ALBのWebSocketサポート**
- ALBはHTTP/1.1接続をWebSocketへアップグレードする機能をネイティブサポートしている。
- **接続タイムアウトの設定**
- ALBの「Connection idle timeout」はデフォルトで60秒。必要に応じて調整が必要。
- **セッション維持（Stickiness）**
- Sticky sessionの設定により、特定のターゲットへのセッションを維持できる。

*発行: 2024/04/03にコメント追加 / [[networking-websocket-websocket-alb-https-a5066e]]*

## 関連テーマ

- [[networking]]
- [[websocket]]

## 出典

- `../60_Resources/websocket ALB.md`
- https://zenn.dev/ymktmk/scraps/71c69a061a9acd
