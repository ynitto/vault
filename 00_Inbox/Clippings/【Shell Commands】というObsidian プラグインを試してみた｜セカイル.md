---
title: "【Shell Commands】というObsidian プラグインを試してみた｜セカイル"
source: "https://note.com/2ndillness/n/naebeded17bdd"
author:
  - "[[セカイル]]"
published: 2026-02-04
created: 2026-04-19
description: "前置き  「Shell Commands」って何？を一言で言うと、シェルコマンドを「Obsidian」上から実行できるようにするプラグインです。  Index - Shell commands documentation - Obsidian PublishShell commands - Documentation Shell commands is a communitypublish.obsidian.md  「Obsidian」ってなんぞ?って言う方はとりまググってもろて。  Obsidian - Sharpen your thinking"
tags:
  - "clippings"
---
Obsidianのコミュニティプラグイン「Shell Commands」の導入と設定方法について解説した記事。

## 要点

### 1. Shell Commandsプラグインとは
- Obsidian上からシェルコマンドを実行可能にするプラグイン。
- 高度なカスタマイズが可能で、シェルコマンドでできることはほぼ何でも実現できる。
- Templaterプラグインでも類似の機能は実現できるが、より自由度が高い。

### 2. プラグインの主な設定項目
- **Shell commands**: 実行するコマンドの登録。
- **Environments**: 使用するシェルの設定。
- **Preactions**: コマンド実行前に実行する入力ダイアログなどの設定。
- **Output**: エラーメッセージや実行完了メッセージの設定。
- **Events**: イベントトリガーの設定。
- **Variables**: カスタム変数の設定。

### 3. 各コマンド毎の設定
- **General**: コマンドの別名やアイコンの設定。
- **Preactions**: 作成したダイアログとコマンドの紐付け。
- **Output**: コマンド実行結果の処理設定（例: ファイルを開く）。

### 4. 実装例
- 新しい記事のタイトルを入力するダイアログを表示。
- タイトルと現在日時を基にファイル名を決定し、新しいMarkdownファイルを生成。
- YAMLフロントマターに日時や定型プロパティを記載。
- ファイル生成後、Obsidianで開く。
- Pythonスクリプトと連携して実現。

### 5. まとめ
- 設定項目が多く、初見では難易度が高いが、スクリプトと連携することで多様な自動化が可能。
- ObsidianのUIと自作スクリプトの橋渡し役として有用。