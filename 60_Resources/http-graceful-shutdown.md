---
title: "http-graceful-shutdown"
source: "https://www.npmjs.com/package/http-graceful-shutdown"
author:
published: 2026-03-10
created: 2026-05-01
description: "gracefully shuts downs http server. Latest version: 3.1.16, last published: 2 months ago. Start using http-graceful-shutdown in your project by running `npm i http-graceful-shutdown`. There are 67 other projects in the npm registry using http-graceful-shutdown."
tags:
  - "clippings"
---
### 概要
`http-graceful-shutdown`は、Node.jsのHTTPサーバーを安全に停止（グレースフルシャットダウン）させるための軽量ライブラリです。接続中のクライアントを維持しつつ、新しい接続をブロックして順次クリーンアップを実行します。

### 主な特徴
- **接続管理**: 全接続を追跡し、アクティブなリクエスト完了を待機。
- **柔軟な停止**: SIGINTやSIGTERMなどのシステム信号をトリガーに自動停止。
- **拡張性**: 独自のクリーンアップ関数（DB切断など）を前処理・後処理に組み込み可能。
- **高い互換性**: Express, Koa, Fastify, ネイティブHTTP/HTTP2に対応。

### 設定可能なオプション
- **timeout**: 強制終了までの待機時間（デフォルト30秒）。
- **signals**: 終了をトリガーするシグナル定義。
- **preShutdown/onShutdown**: シャットダウン前後の非同期カスタム処理。
- **forceExit**: プロセスを強制終了するか、イベントループの終了を待つかを選択。
- **development**: 開発用に短縮されたシャットダウンモード。

### 基本的な使い方
```javascript
const gracefulShutdown = require('http-graceful-shutdown');
const server = app.listen();

gracefulShutdown(server, {
  onShutdown: async () => { /* DB切断などの処理 */ }
});
```
