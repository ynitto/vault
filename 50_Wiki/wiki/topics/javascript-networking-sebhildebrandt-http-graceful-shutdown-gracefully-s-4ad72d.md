---
title: "sebhildebrandt/http-graceful-shutdown: Gracefully shuts down node http server - can be used with http, express, koa, ..."
type: "topic"
tags:
  - "javascript"
  - "networking"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/sebhildebrandthttp-graceful-shutdown Gracefully shuts down node http server - can be used with http, express, koa, ....md"
summary: "`http-graceful-shutdown` は、Node.jsのHTTPサーバーを安全に終了させるためのライブラリです。接続中のクライアントに影響を…"
---

# sebhildebrandt/http-graceful-shutdown: Gracefully shuts down node http server - can be used with http, express, koa, ...

## 概要

`http-graceful-shutdown` は、Node.jsのHTTPサーバーを安全に終了させるためのライブラリです。接続中のクライアントに影響を与えず、リクエスト処理の完了を待ってからサーバーを停止させる「グレースフル・シャットダウン（正常終了）」を実現します。

## 主要なトピック

- [[javascript]]
- [[networking]]
- [[node-js]]

## 詳細

- `http-graceful-shutdown` は、Node.jsのHTTPサーバーを安全に終了させるためのライブラリです。接続中のクライアントに影響を与えず、リクエスト処理の完了を待ってからサーバーを停止させる「グレースフル・シャットダウン（正常終了）」を実現します。
- 主な特徴
- **互換性:** Express, Koa, Fastify, ネイティブHTTP/HTTPSサーバー等に対応。
- **安全な終了:** 既存の接続を追跡し、シャットダウン信号（SIGINT, SIGTERM等）受信後に新規接続を拒否します。
- **柔軟な制御:**
- **preShutdown:** 接続が残っている状態での前処理。
- **onShutdown:** データベース接続のクローズなど、終了時の非同期処理。
- **finally:** 終了直前に実行する同期処理。
- **構成可能:** タイムアウト設定、シグナル定義、プロセス終了の強制有無（forceExit）を自由に設定可能。

## 関連テーマ

- [[javascript]]
- [[networking]]
- [[node-js]]

## 出典

- `../60_Resources/sebhildebrandthttp-graceful-shutdown Gracefully shuts down node http server - can be used with http, express, koa, ....md`
- https://github.com/sebhildebrandt/http-graceful-shutdown/tree/master
