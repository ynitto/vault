---
title: "Admin UI"
source: "https://socket.io/docs/v4/admin-ui/"
author:
published: 2026-03-03
created: 2026-05-01
description: "The Socket.IO admin UI can be used to have an overview of the state of your Socket.IO deployment."
tags:
  - "clippings"
---
### Socket.IO Admin UI の概要
Socket.IO Admin UI は、Socket.IO デプロイメントの状態を可視化・管理するための公式ツールです。

### 主な機能
- **状態監視**: 接続中のサーバーやクライアントのリアルタイムな一覧表示。
- **詳細確認**: 個別のソケットインスタンス、ルーム、イベント送受信ログの詳細調査。
- **管理操作**: 特定のクライアントの「参加」「離脱」「切断」といった操作を実行可能。

### 導入手順
1. **インストール**: `npm i @socket.io/admin-ui` を実行。
2. **サーバー設定**: `instrument` メソッドを Socket.IO サーバーに適用。
3. **アクセス**: [https://admin.socket.io](https://admin.socket.io) にアクセスし、サーバーURLと認証情報を入力。

### 設定のポイント
- **セキュリティ**: `auth` オプションで認証設定が可能（Basic認証など）。
- **パフォーマンス**: 本番環境では `mode: "production"` を指定することで、詳細情報の送信を抑制しメモリ負荷を軽減可能。
- **マルチサーバー**: 複数サーバー構成の場合は `serverId` を個別に指定し、必要に応じて `RedisStore` 等のカスタムストアを使用する。
