---
title: "docker exec — Docker-docs-ja 24.0 ドキュメント"
source: "https://docs.docker.jp/engine/reference/commandline/exec.html"
author:
published:
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 概要
`docker exec` は、稼働中のコンテナ内で新たにコマンドを実行するためのコマンドです。

### 主なポイント
* **基本用途**: 実行中のコンテナに対して外部からコマンドを送る際に使用します。
* **実行条件**: コンテナのメインプロセス（PID 1）が稼働中である必要があります。
* **制限事項**: 
    * コンテナが一時停止（paused）状態では実行できません。
    * 連結コマンド（`&&`など）を直接指定すると動作しないため、`sh -c` を介す必要があります。
* **主なオプション**:
    * `-d`: バックグラウンドで実行
    * `-it`: 対話モード（標準入力とTTYの有効化）
    * `-e`: 環境変数の設定
    * `-u`: ユーザー/UIDの指定
    * `-w`: 作業ディレクトリの変更
