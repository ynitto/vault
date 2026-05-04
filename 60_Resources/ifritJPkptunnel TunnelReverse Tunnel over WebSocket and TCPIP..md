---
title: "ifritJP/kptunnel: Tunnel/Reverse Tunnel over WebSocket and TCP/IP."
source: "https://github.com/ifritJP/kptunnel"
author:
published:
created: 2026-05-01
description: "Tunnel/Reverse Tunnel over WebSocket and TCP/IP. Contribute to ifritJP/kptunnel development by creating an account on GitHub."
tags:
  - "clippings"
---
### 概要
`kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続が一時的に切断されても、TCPセッションを維持できる点が特徴です。

### 主な特徴
- **接続の継続性:** ネットワーク切断時もTCPセッションを保持。
- **通信方式:** WebSocket（`ws` prefix）または直接TCP接続を選択可能。
- **セキュリティ:** クライアント認証および通信の暗号化に対応。
- **柔軟性:** プロキシ経由の接続（HTTPプロキシのみ）や、IPアドレスによるアクセス制限が可能。

### 基本的な使い方
`$ kptunnel <モード> <サーバー> [転送設定] [オプション]`

- **モード:** `wsserver`, `r-wsserver`, `client`, `r-client` など（`r-`はリバーストンネル）。
- **サーバー:** リスニングポートや接続先（例: `localhost:1234`）。
- **転送設定:** `[r|t], [ホスト]:ポート, 転送先ホスト:転送先ポート`。

### 主要オプション
- `-pass`: クライアント認証用パスワード。
- `-encPass`: 通信暗号化用パスワード。
- `-proxy`: HTTPプロキシ経由の接続（クライアント側）。
- `-ip`: 接続を許可するIP範囲の制限。

### 注意点
- **実験的機能:** TCPによる直接接続は現在実験的な機能です。
- **言語:** Go言語で開発されており、ネットワーク負荷の少ない環境でも安定したパフォーマンスを発揮します。