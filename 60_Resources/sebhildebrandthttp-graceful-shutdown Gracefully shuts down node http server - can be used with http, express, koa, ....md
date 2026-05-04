---
title: "sebhildebrandt/http-graceful-shutdown: Gracefully shuts down node http server - can be used with http, express, koa, ..."
source: "https://github.com/sebhildebrandt/http-graceful-shutdown/tree/master"
author:
published:
created: 2026-05-01
description: "Gracefully shuts down node http server - can be used with http, express, koa, ... - sebhildebrandt/http-graceful-shutdown"
tags:
  - "clippings"
---
### 概要
`http-graceful-shutdown` は、Node.jsのHTTPサーバーを安全に終了させるためのライブラリです。接続中のクライアントに影響を与えず、リクエスト処理の完了を待ってからサーバーを停止させる「グレースフル・シャットダウン（正常終了）」を実現します。

### 主な特徴
- **互換性:** Express, Koa, Fastify, ネイティブHTTP/HTTPSサーバー等に対応。
- **安全な終了:** 既存の接続を追跡し、シャットダウン信号（SIGINT, SIGTERM等）受信後に新規接続を拒否します。
- **柔軟な制御:**
    - **preShutdown:** 接続が残っている状態での前処理。
    - **onShutdown:** データベース接続のクローズなど、終了時の非同期処理。
    - **finally:** 終了直前に実行する同期処理。
- **構成可能:** タイムアウト設定、シグナル定義、プロセス終了の強制有無（forceExit）を自由に設定可能。

### 利用シーン
- サーバー再起動やデプロイ時に、リクエストが途切れるのを防ぎたい場合。
- データベース等のリソースをクリーンに解放してからプロセスを終了させたい場合。

### クイックスタート
```javascript
const gracefulShutdown = require('http-graceful-shutdown');
const server = app.listen(3000);

// 基本的な有効化
gracefulShutdown(server);
```
