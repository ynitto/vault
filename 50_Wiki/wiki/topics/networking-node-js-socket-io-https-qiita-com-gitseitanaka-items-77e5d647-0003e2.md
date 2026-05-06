---
title: "socket.ioのパケットを(触りだけ)キャプチャ"
type: "topic"
tags:
  - "networking"
  - "node-js"
  - "websocket"
  - "shunjikonishi"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/socket.ioのパケットを(触りだけ)キャプチャ.md"
summary: "この記事は、Node.jsのエンジニアがSocket.io（v1.3.5）の通信パケットを実際にキャプチャし、その内部挙動を理解するために調査・まとめた記…"
---

# socket.ioのパケットを(触りだけ)キャプチャ

## 概要

この記事は、Node.jsのエンジニアがSocket.io（v1.3.5）の通信パケットを実際にキャプチャし、その内部挙動を理解するために調査・まとめた記録です。

*発行: 2015-09-30 / [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]*

## 主要なトピック

- [[networking]]
- [[node-js]]
- [[websocket]]
- [[shunjikonishi]]

## 詳細

- この記事は、Node.jsのエンジニアがSocket.io（v1.3.5）の通信パケットを実際にキャプチャし、その内部挙動を理解するために調査・まとめた記録です。
- 要点
- **Socket.ioの仕組み**
- WebSocketとロングポーリング（polling）の両方をサポート。
- デフォルトではポーリングで接続し、可能であれば自動的にWebSocketへアップグレードする。
- **接続の主なステップ**
- 1. **HTTP取得**: HTMLやJSファイルの取得。
- 2. **セッション開始**: セッションIDと接続設定の交換。
- 3. **ポーリング**: HTTPを用いた初期通信。

*発行: 2015-09-30 / [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]*

## 関連テーマ

- [[networking]]
- [[node-js]]
- [[websocket]]
- [[shunjikonishi]]

## 出典

- `60_Resources/socket.ioのパケットを(触りだけ)キャプチャ.md`
- https://qiita.com/gitseitanaka/items/77e5d647fa364020d3f1
