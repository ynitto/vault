---
title: "Start XState inspector locally · statelyai/xstate"
type: "topic"
tags:
  - "networking"
  - "performance"
  - "websocket"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Start XState inspector locally · statelyaixstate.md"
summary: "XState InspectorをWebブラウザ以外（React Native等）の環境でローカル実行する方法についての議論。外部サービス（statech…"
---

# Start XState inspector locally · statelyai/xstate

## 概要

XState InspectorをWebブラウザ以外（React Native等）の環境でローカル実行する方法についての議論。外部サービス（statecharts.io）に依存せず、ローカルサーバーを立ててデバッグ環境を構築する手順が共有されています。

## 主要なトピック

- [[networking]]
- [[performance]]
- [[websocket]]

## 詳細

- XState InspectorをWebブラウザ以外（React Native等）の環境でローカル実行する方法についての議論。外部サービス（statecharts.io）に依存せず、ローカルサーバーを立ててデバッグ環境を構築する手順が共有されています。
- 要点まとめ
- **課題**: `xstate-inspect`が標準で新しいブラウザウィンドウを開こうとするため、Webアプリ以外の環境で利用しにくい。
- **解決策**:
- `statecharts.io/inspect`のページをローカルに保存し、静的ファイルとして自身の開発サーバーから配信する。
- アプリ側からそのローカルURL（例: `localhost:xxxx/inspect`）へ接続するように設定する。
- **実装のヒント**:
- `import { inspect } from "@xstate/inspect/lib/server.js"` をマシン定義前に記述する必要がある。
- 複数のマシンを検査する場合、WebSocket通信による負荷やメモリリークに注意が必要。

## 関連テーマ

- [[networking]]
- [[performance]]
- [[websocket]]

## 出典

- `../60_Resources/Start XState inspector locally · statelyaixstate.md`
- https://github.com/statelyai/xstate/discussions/1626
