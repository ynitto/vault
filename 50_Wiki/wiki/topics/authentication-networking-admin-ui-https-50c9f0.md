---
title: "Admin UI"
type: "topic"
tags:
  - "authentication"
  - "networking"
  - "node-js"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Admin UI.md"
summary: "Socket.IO Admin UI は、Socket.IO デプロイメントの状態を可視化・管理するための公式ツールです。"
---

# Admin UI

## 概要

Socket.IO Admin UI は、Socket.IO デプロイメントの状態を可視化・管理するための公式ツールです。

*発行: 2026-03-03 / [[authentication-networking-admin-ui-https-50c9f0]]*

## 主要なトピック

- [[authentication]]
- [[networking]]
- [[node-js]]
- [[performance]]

## 詳細

- Socket.IO Admin UI は、Socket.IO デプロイメントの状態を可視化・管理するための公式ツールです。
- 主な機能
- **状態監視**: 接続中のサーバーやクライアントのリアルタイムな一覧表示。
- **詳細確認**: 個別のソケットインスタンス、ルーム、イベント送受信ログの詳細調査。
- **管理操作**: 特定のクライアントの「参加」「離脱」「切断」といった操作を実行可能。
- 導入手順
- 1. **インストール**: `npm i @socket.io/admin-ui` を実行。
- 2. **サーバー設定**: `instrument` メソッドを Socket.IO サーバーに適用。
- 3. **アクセス**: [https://admin.socket.io](https://admin.socket.io) にアクセスし、サーバーURLと認証情報を入力。

*発行: 2026-03-03 / [[authentication-networking-admin-ui-https-50c9f0]]*

## 関連テーマ

- [[authentication]]
- [[networking]]
- [[node-js]]
- [[performance]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Admin UI.md`
- https://socket.io/docs/v4/admin-ui/
