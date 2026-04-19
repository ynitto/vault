---
title: "Obsidian CLI"
source: "https://obsidian.md/ja/help/cli"
author:
published:
created: 2026-04-19
description: "Obsidian CLI - Obsidian ヘルプ"
tags:
  - "clippings"
---
# Obsidian CLIの概要

Obsidian CLIは、ターミナルからObsidianを操作できるコマンドラインインターフェースです。スクリプト作成、自動化、外部ツールとの連携に利用できます。Obsidianで行えるほぼすべての操作が可能です。

## 主な機能と使い方

### 1. インストール
-   Obsidian 1.12+インストーラーにアップデートする。
-   Obsidianの**設定** → **一般**で**コマンドラインインターフェース**を有効にする。
-   プロンプトに従って登録する。

### 2. 基本的な利用方法
-   **Obsidianアプリが起動していること**が必須。
-   単一コマンド実行：`obsidian <command>`
-   ターミナルユーザーインターフェース (TUI) ：`obsidian`と入力後、コマンドを入力。
    -   TUIは自動補完、コマンド履歴、逆方向検索 (Ctrl+R) をサポート。
-   **パラメータとフラグ**: `parameter=value`形式、フラグは値なしで有効化。
-   **保管庫の指定**: `vault=<name>`または`vault=<id>`をコマンドの最初のパラメータとして指定。
-   **ファイルの指定**: `file=<name>`（ファイル名）または`path=<path>`（保管庫ルートからのパス）を使用。
-   **出力のコピー**: 任意のコマンドに`--copy`を追加してクリップボードにコピー。

### 3. 主要コマンドカテゴリ
-   **一般**: `help`, `version`, `reload`, `restart`。
-   **ファイル/フォルダ**: `create`, `read`, `append`, `prepend`, `move`, `rename`, `delete`, `open`, `files`, `folders`。
-   **デイリーノート**: `daily` (開く), `daily:read`, `daily:append`, `daily:prepend`。
-   **リンク**: `backlinks`, `links`, `unresolved`, `orphans`, `deadends`。
-   **タグとプロパティ**: `tags`, `tag`, `properties`, `property:set`, `property:read`。
-   **タスク**: `tasks` (一覧表示), `task` (表示/更新/切り替え)。
-   **検索**: `search` (テキスト検索), `search:context`, `search:open`。
-   **プラグイン/テーマ**: `plugins`, `plugin:enable`, `plugin:disable`, `plugin:install`, `plugin:reload` (開発者向け), `themes`, `theme:set`。
-   **Obsidianサービス**: `publish:list`, `publish:add`, `sync:status`, `sync:history`。
-   **開発者コマンド**: `devtools` (開発者ツール開閉), `dev:screenshot` (スクリーンショット), `eval` (JavaScript実行), `dev:dom` (DOM要素クエリ)。

### 4. キーボードショートカット (TUI内)
-   ナビゲーション、編集、自動補完、履歴検索 (Ctrl+R)、終了 (Ctrl+C/D) などが利用可能。

### 5. トラブルシューティング
-   最新インストーラー、CLI設定の再有効化、ターミナル再起動を確認。
-   Obsidianアプリが起動している必要がある。
-   OSごとの特定の登録・PATH設定の確認 (`Windows`, `macOS`, `Linux`のセクションを参照)。