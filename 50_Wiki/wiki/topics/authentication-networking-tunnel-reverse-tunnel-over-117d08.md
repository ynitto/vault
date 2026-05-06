---
title: "Tunnel/Reverse Tunnel over websocket を作った"
type: "topic"
tags:
  - "authentication"
  - "networking"
  - "performance"
  - "websocket"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/TunnelReverse Tunnel over websocket を作った.md"
summary: "「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題…"
---

# Tunnel/Reverse Tunnel over websocket を作った

## 概要

「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題を解決するため、Go言語で独自開発されました。

*発行: 2020-05-29 / [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]*

## 主要なトピック

- [[authentication]]
- [[networking]]
- [[performance]]
- [[websocket]]

## 詳細

- 「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題を解決するため、Go言語で独自開発されました。
- 主な特徴
- **トンネル機能**: WebSocketを利用してポート制限をバイパスし、TCPセッションを転送。
- **堅牢性**: 強制切断を検知した際、自動再接続と未到達パケットの再送を行い、セッションを維持。
- **カスタマイズ性**: 「dispatcher」機能により、複数のクライアントを効率的に管理・振り分け可能。
- **セキュリティ**: クライアント認証（Challenge/Response）および通信経路の暗号化（AES256）をサポート。
- **高効率**: パケット結合送信やリングバッファによるメモリ効率化を実装。
- 利用ケース
- ポート制限された環境間でのセキュアなリモートアクセス。

*発行: 2020-05-29 / [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]*

## 関連テーマ

- [[authentication]]
- [[networking]]
- [[performance]]
- [[websocket]]

## 出典

- `../60_Resources/TunnelReverse Tunnel over websocket を作った.md`
- https://ifritjp../.github.io/blog2/public/posts/2020/2020-05-29-tunnel/
