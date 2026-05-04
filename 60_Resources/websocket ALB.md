---
title: "websocket ALB"
source: "https://zenn.dev/ymktmk/scraps/71c69a061a9acd"
author:
published: 2024/04/03にコメント追加
created: 2026-05-01
description: "tomokiさんのスクラップ"
tags:
  - "clippings"
---
### WebSocketとALBの運用における要点

本スクラップは、WebSocketをAWSのApplication Load Balancer (ALB) で運用する際の構成および注意点をまとめたものです。

*   **ヘルスチェックの実装**
    *   `/api/health` エンドポイントを作成し、ALBからの死活監視に応答できるようにする。
*   **ALBのWebSocketサポート**
    *   ALBはHTTP/1.1接続をWebSocketへアップグレードする機能をネイティブサポートしている。
*   **接続タイムアウトの設定**
    *   ALBの「Connection idle timeout」はデフォルトで60秒。必要に応じて調整が必要。
*   **セッション維持（Stickiness）**
    *   Sticky sessionの設定により、特定のターゲットへのセッションを維持できる。