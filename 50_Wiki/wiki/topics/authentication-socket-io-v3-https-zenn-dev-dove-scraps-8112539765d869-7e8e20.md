---
title: "socket.ioのv3で知らなかったこと"
type: "topic"
tags:
  - "authentication"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/socket.ioのv3で知らなかったこと.md"
summary: "本記事はSocket.io v3の主要機能と開発上の注意点をまとめた技術メモです。サーバー・クライアントの初期化から、ルーム、ミドルウェア、CORS、エラ…"
---

# socket.ioのv3で知らなかったこと

## 概要

本記事はSocket.io v3の主要機能と開発上の注意点をまとめた技術メモです。サーバー・クライアントの初期化から、ルーム、ミドルウェア、CORS、エラーハンドリング、バイナリ転送など、実践的な実装パターンを解説しています。

*発行: 2020/12/12にクローズ / [[authentication-socket-io-v3-https-zenn-dev-dove-scraps-8112539765d869-7e8e20]]*

## 主要なトピック

- [[authentication]]

## 詳細

- 本記事はSocket.io v3の主要機能と開発上の注意点をまとめた技術メモです。サーバー・クライアントの初期化から、ルーム、ミドルウェア、CORS、エラーハンドリング、バイナリ転送など、実践的な実装パターンを解説しています。
- 要点まとめ
- サーバー・クライアント共通
- **初期化**: サーバーはHTTP/Express等と共存可能。クライアントはドメインに応じて`io()`で接続。
- **通信**: `socket.emit`のほか、`socket.send`による`message`イベント利用も可能。
- **バイナリ対応**: JSONシリアライズ不要で直接オブジェクト送信可能（Map/Setは要シリアライズ）。
- サーバーサイド機能
- **ルーム**: `socket.join('name')`で参加。`socket.rooms`で管理。
- **ミドルウェア**: `io.use()`で実装。`next()`で進行、`next(Error)`で接続拒否。

*発行: 2020/12/12にクローズ / [[authentication-socket-io-v3-https-zenn-dev-dove-scraps-8112539765d869-7e8e20]]*

## 関連テーマ

- [[authentication]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/socket.ioのv3で知らなかったこと.md`
- https://zenn.dev/dove/scraps/8112539765d869
