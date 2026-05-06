---
title: "ifritJP/kptunnel: Tunnel/Reverse Tunnel over WebSocket and TCP/IP."
type: "topic"
tags:
  - "authentication"
  - "networking"
  - "websocket"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md"
summary: "`kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続…"
---

# ifritJP/kptunnel: Tunnel/Reverse Tunnel over WebSocket and TCP/IP.

## 概要

`kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続が一時的に切断されても、TCPセッションを維持できる点が特徴です。

## 主要なトピック

- [[authentication]]
- [[networking]]
- [[websocket]]

## 詳細

- `kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続が一時的に切断されても、TCPセッションを維持できる点が特徴です。
- 主な特徴
- **接続の継続性:** ネットワーク切断時もTCPセッションを保持。
- **通信方式:** WebSocket（`ws` prefix）または直接TCP接続を選択可能。
- **セキュリティ:** クライアント認証および通信の暗号化に対応。
- **柔軟性:** プロキシ経由の接続（HTTPプロキシのみ）や、IPアドレスによるアクセス制限が可能。
- 基本的な使い方
- `$ kptunnel <モード> <サーバー> [転送設定] [オプション]`
- **モード:** `wsserver`, `r-wsserver`, `client`, `r-client` など（`r-`はリバーストンネル）。

## 関連テーマ

- [[authentication]]
- [[networking]]
- [[websocket]]

## 出典

- `60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md`
- https://github.com/ifritJP/kptunnel
