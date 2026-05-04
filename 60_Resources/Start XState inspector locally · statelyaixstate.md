---
title: "Start XState inspector locally · statelyai/xstate"
source: "https://github.com/statelyai/xstate/discussions/1626"
author:
published:
created: 2026-05-01
description: "Start XState inspector locally"
tags:
  - "clippings"
---
### 内容の要約
XState InspectorをWebブラウザ以外（React Native等）の環境でローカル実行する方法についての議論。外部サービス（statecharts.io）に依存せず、ローカルサーバーを立ててデバッグ環境を構築する手順が共有されています。

### 要点まとめ
- **課題**: `xstate-inspect`が標準で新しいブラウザウィンドウを開こうとするため、Webアプリ以外の環境で利用しにくい。
- **解決策**:
    - `statecharts.io/inspect`のページをローカルに保存し、静的ファイルとして自身の開発サーバーから配信する。
    - アプリ側からそのローカルURL（例: `localhost:xxxx/inspect`）へ接続するように設定する。
- **実装のヒント**:
    - `import { inspect } from "@xstate/inspect/lib/server.js"` をマシン定義前に記述する必要がある。
    - 複数のマシンを検査する場合、WebSocket通信による負荷やメモリリークに注意が必要。
    - ブラウザのデバッガーを開きっぱなしにするとメモリ消費が増える傾向がある。