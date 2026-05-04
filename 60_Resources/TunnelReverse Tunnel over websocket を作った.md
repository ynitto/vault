---
title: "Tunnel/Reverse Tunnel over websocket を作った"
source: "https://ifritjp.github.io/blog2/public/posts/2020/2020-05-29-tunnel/"
author:
published: 2020-05-29
created: 2026-05-01
description: "とある理由から 「Tunnel/Reverse Tunnel over websocket」 が必要になったので作ってみた。 「Tunnel/Reverse Tunnel over websocket」 が何かというと、 「websocket を tunnel にして別の TCP 通信を通すもの」だ。 「Tunnel/Reverse Tunnel over websocket」 とは 「Tunnel/Reverse Tunnel over websocket」を少し具体的にいうと、 次のような構成で通信を可能にするモノだ。 frame"
tags:
  - "clippings"
---
### 概要
「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題を解決するため、Go言語で独自開発されました。

### 主な特徴
- **トンネル機能**: WebSocketを利用してポート制限をバイパスし、TCPセッションを転送。
- **堅牢性**: 強制切断を検知した際、自動再接続と未到達パケットの再送を行い、セッションを維持。
- **カスタマイズ性**: 「dispatcher」機能により、複数のクライアントを効率的に管理・振り分け可能。
- **セキュリティ**: クライアント認証（Challenge/Response）および通信経路の暗号化（AES256）をサポート。
- **高効率**: パケット結合送信やリングバッファによるメモリ効率化を実装。

### 利用ケース
- ポート制限された環境間でのセキュアなリモートアクセス。
- 頻繁に切断される不安定なネットワーク環境での通信維持。

### 技術スタック
- **開発言語**: Go (1.14.2)
- **カスタマイズ**: LuneScript (dispatcherの制御用)