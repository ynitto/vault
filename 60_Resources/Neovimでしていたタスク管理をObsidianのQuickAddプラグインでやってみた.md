---
title: Neovimでしていたタスク管理をObsidianのQuickAddプラグインでやってみた
source: https://zenn.dev/moneyforward/articles/94d5a22f3ab4f1
author: null
published: 2025-09-15
created: 2026-04-19
description: null
tags:
- resource/web
- obsidian
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/Neovimでしていたタスク管理をObsidianのQuickAddプラグインでやってみた.md
copied_at: 2026-04-19 10:51:13+09:00
---
## 概要
Neovimで実現していたタスク管理方法（タスクのファイル化・アーカイブ）を、ObsidianのQuickAddプラグインとJavaScriptを活用して再現する手順を解説します。

## Neovimでのタスク管理（以前の手法）
-   `main.md`にタスクリストを記述。
-   各タスクの詳細は個別のMarkdownファイルに分割。
-   **ConvertTask**: `main.md`のタスク行から詳細ファイルを作成し、リンクに変換。
-   **ArchiveTask**: 完了したタスクのファイルをアーカイブディレクトリに移動。

## Obsidianでの実現方法
### 1. ディレクトリ構成
-   `vault/scripts/`: QuickAddマクロ用のJavaScriptファイルを配置。
-   `vault/tasks/`: 進行中のタスクファイルを保存。
-   `vault/archives/`: 完了・停止したタスクファイルを保存（日付ごとのサブディレクトリ）。
-   `vault/main.md`: メインタスクリスト。

### 2. JavaScriptファイルの準備
-   `convertTask.js`: 
    -   `main.md`上のカーソル行のタスクを認識。
    -   ユーザーからのファイル名入力に基づき、`tasks/`ディレクトリに新しいMarkdownファイルを作成。
    -   `main.md`のタスク行を、作成されたファイルへのリンクに更新。
    -   ファイル作成後、開くか選択できる。
-   `archiveTask.js`: 
    -   カーソル行がリンクされたタスクの場合、リンク先のファイルを`archives/YYYYMMDD/`ディレクトリに移動し、`main.md`のリンクを更新。
    -   カーソル行がリンクされていない通常のタスクの場合、タスク内容を`archives/YYYYMMDD/misc.md`に追記し、`main.md`からタスク行を削除。

### 3. QuickAddプラグインの設定
-   ObsidianでQuickAddプラグインをインストール。
-   QuickAdd設定画面で、`ConvertTask`と`ArchiveTask`という名前で「Macro」タイプのChoiceを追加。
-   各Macroの設定で、User Scriptsから対応するJavaScriptファイル（`scripts/convertTask.js`、`scripts/archiveTask.js`）を選択して追加。
-   Macroを有効化することで、コマンドパレットから直接実行可能になる。

## デモ
-   `main.md`上で`ConvertTask`を実行すると、新しいタスクファイルが作成され、元のタスク行がリンクに変わる様子を確認。
-   `ArchiveTask`を実行すると、リンクされたタスクファイルがアーカイブされ、元のタスク行が完了済みに変わる様子を確認。

## まとめ
-   Neovimのカスタムスクリプトによるタスク管理を、ObsidianのQuickAddとJavaScriptで同様に実現可能。
-   簡単なコーディング知識とAIの活用で、柔軟なカスタムロジックを実装できる。
-   JIRAなどの主要なスケジュール管理と併用し、個人的な詳細手順やメモ管理にこの方法が有効。