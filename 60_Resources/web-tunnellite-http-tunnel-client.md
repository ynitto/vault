---
title: web-tunnel/lite-http-tunnel-client
source: https://github.com/web-tunnel/lite-http-tunnel-client/tree/main
author: null
published: null
created: 2026-05-05
description: Contribute to web-tunnel/lite-http-tunnel-client development by creating
  an account on GitHub.
tags:
- clippings
- resource/web
- 2026-05
original_source: 00_Inbox/Clippings/web-tunnellite-http-tunnel-client.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 概要
「Lite HTTP Tunnel Client」は、ローカル環境で動作するHTTPサーバーを公開・外部アクセス可能にするためのNode.js製ツールです。

### 要点
- **主な機能**: リモートのHTTPトンネルサーバーを経由して、ローカルサーバーをパブリックに公開。
- **インストール方法**: `npm i -g lite-http-tunnel` でグローバルインストール。
- **主なコマンド**:
    - `config server`: トンネルサーバーのアドレスを設定。
    - `auth`: 認証用ユーザー名・パスワードを設定。
    - `start`: 指定したポートでトンネルを開始（例: `lite-http-tunnel start 8080`）。
- **利便性**: 開発中のローカルWebサイトなどを、設定した外部ドメインから即座にアクセス可能にする。
