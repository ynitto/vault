---
title: "Redis Streams adapter"
source: "https://socket.io/docs/v4/redis-streams-adapter/"
author:
published: 2026-03-03
created: 2026-05-01
description: "How it works"
tags:
  - "clippings"
---
### Socket.IO Redis Streams Adapter の概要
Redis Streamを活用し、Socket.IOサーバー間でパケットを転送するためのアダプターです。従来のPub/Sub方式と比較して、Redisサーバーとの一時的な切断に対してもパケットを損失することなく復旧できるのが最大の利点です。

### 主な特徴
- **耐障害性**: Redisとの切断時にもストリームを再開し、データ損失を防ぐ。
- **互換性**: Valkeyにも対応。
- **機能サポート**: ソケット管理、サーバー間通信、ブロードキャスト時のACK、接続状態のリカバリーに対応。

### 導入のポイント
- **インストール**: `npm install @socket.io/redis-streams-adapter redis` で実行。
- **設定**: `redis` パッケージや `ioredis` を使用してサーバーにアダプターを紐付けます。
- **注意点**: 複数サーバー構成では、**Sticky Sessions（スティッキーセッション）の設定が必須**です。未設定の場合、HTTP 400エラーが発生します。

### 主要なオプション
- `streamName`: Redisストリーム名（デフォルト: `socket.io`）
- `maxLen`: ストリームの最大長（デフォルト: `10,000`）
- `streamCount`: 水平スケーリングのためのストリーム数
