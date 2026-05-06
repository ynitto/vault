---
title: "mr/tmuxでタイムスタンプ付きログ"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-06"
sources:
  - "../60_Resources/mrtmuxでタイムスタンプ付きログ.md"
  - "../60_Resources/tmuxのpipe-paneを利用してリモートサーバでの作業ログをローカルに記録する.md"
summary: "tmuxのセッションログに日時を付与し、かつANSIエスケープシーケンス（制御コード）を除去して読みやすく保存する手法の解説です。"
---

# mr/tmuxでタイムスタンプ付きログ

## 概要

tmuxのセッションログに日時を付与し、かつANSIエスケープシーケンス（制御コード）を除去して読みやすく保存する手法の解説です。

## 主要なトピック


## 詳細

- tmuxのセッションログに日時を付与し、かつANSIエスケープシーケンス（制御コード）を除去して読みやすく保存する手法の解説です。
- `pipe-pane` を直接使う方法では、リモートサーバ上の操作ログをローカル側に保存でき、長時間実行エージェントの証跡採取にも応用できる。
- 実装の手順
- **ディレクトリ作成**: ログ保存用に `~/wiki/topicstmux` を作成します。
- **フィルター用スクリプト**: `awk` で日時を付与し、`sed` で制御コードを削除する `tslog` スクリプトを作成し、`/usr/local/bin` 等に配置します。
- 設定方法
- `~/wiki/topicstmux.conf` に以下のキーバインドを追加します。
- **ログ開始**: `bind-key H pipe-pane 'tslog >\\"$HOME/wiki/topicstmux/%Y%m%d-%H%M%S-#P.log\\"'`
- **ログ停止**: `bind-key h pipe-pane`
- これにより、ワンタッチでログの記録・停止が可能になります。

## 関連テーマ


## 出典

- `../60_Resources/mrtmuxでタイムスタンプ付きログ.md`
- `../60_Resources/tmuxのpipe-paneを利用してリモートサーバでの作業ログをローカルに記録する.md`
- https://kemasoft.net/?mr/tmux%E3%81%A7%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%97%E4%BB%98%E3%81%8D%E3%83%AD%E3%82%B0
