---
title: "@spurreiter/wstun"
source: "https://www.npmjs.com/package/@spurreiter/wstun"
author:
published: 2026-03-29
created: 2026-05-01
description: "A set of tools to establish TCP tunnels (or TCP reverse tunnels) over WebSocket connections for circumventing the problem of directly connect to hosts behind a strict firewall or without public IP. It also supports WebSocket Secure (wss) connections.. Latest version: 2.0.5, last published: a month ago. Start using @spurreiter/wstun in your project by running `npm i @spurreiter/wstun`. There are no other projects in the npm registry using @spurreiter/wstun."
tags:
  - "clippings"
---
### 概要
`@spurreiter/wstun` は、ファイアウォール越しやグローバルIPを持たない環境での通信を可能にする、WebSocketベースのTCPトンネリング（前方および逆方向）ツールです。Node.js向けにESM対応・型定義付きで書き直されたライブラリです。

### 主な特徴
- **前方・逆方向トンネル**: WebSocketを利用したTCP通信の中継。
- **セキュリティ**: TLS/WSS（暗号化通信）のサポート。
- **CLI機能**: コマンドラインから即座にサーバーやクライアントとして起動可能。
- **拡張性**: 認証機能（JSONによる接続制限）や自動再接続オプションを備える。

### 主要な機能
- **前方トンネル**: クライアントがサーバーを介して特定のサービスに接続。
- **逆方向トンネル**: サーバーがクライアント側のローカルサービスにアクセス。
- **ロギング**: `debug-level` を利用した柔軟なログ管理。

### 導入方法
- **インストール**: `npm install @spurreiter/wstun`
- **実行例 (CLI)**:
  - サーバー起動: `wstun -s 4000`
  - クライアント起動: `wstun -t 9000 wss://host:4000`