---
original_source: 00_Inbox/Clippings/基礎知識０から、AIに自分用メモを書かせる時代へ適応してみた(mcp-obsidian).md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, obsidian, 2026-04]
---

---
title: "基礎知識０から、AIに自分用メモを書かせる時代へ適応してみた(mcp-obsidian)"
source: "https://zenn.dev/502/articles/f8aeaa8057fc49"
author:
published: 2025-05-05
created: 2026-04-19
description:
tags:
  - "clippings"
---
## AIメモ書き環境構築ガイド

この記事は、ClaudeとObsidianを連携させ、AIにメモを作成・編集させる方法を解説しています。

### 概要

* **目的:** AI（Claude）がObsidianにメモを作成・編集できるようにする環境を構築する。
* **対象:** AIやObsidianの初心者。
* **所要時間:** 約15分。
* **費用:** 通信料以外は無料（ClaudeのFree Planで利用可能）。

### できること

* Claude DesktopがObsidianのメモを直接作成・編集。

### 環境構築手順

1.  **Claude Desktopのインストール**
2.  **Gitのインストール (brew)**
3.  **uvのインストール**
4.  **Obsidianのインストール**
5.  **mcp-obsidianの導入**
    * Gitリポジトリをクローン。
6.  **MCP環境の整備**
    * **Obsidian側:** Local REST APIプラグインの有効化とAPIキーの取得。
    * **MCPサーバ側:** `.env`ファイルにAPIキーを設定。
    * **Claude Desktop側:** 設定ファイル (`claude_desktop_config.json`) にMCPサーバー情報を追記。

### AIメモ作成の開始

* Claude Desktopでチャットを開始し、「Obsidian」という単語を含めて指示。
* ClaudeがObsidianへの操作を試みる際に許可を求めるので、許可する。
* メモ作成、リンク作成、フォルダ整理などが可能。

### クリーンアップ

* uvのアンインストール。
* Claude Desktop、Obsidianのアンインストール。
* Gitはアンインストール非推奨（アップデート方法のみ記載）。

### まとめ

AIを活用してObsidianでのメモ作成を効率化し、学習速度を向上させるための入門ガイド。