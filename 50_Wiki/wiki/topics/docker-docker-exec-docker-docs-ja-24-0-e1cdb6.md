---
title: "docker exec — Docker-docs-ja 24.0 ドキュメント"
type: "topic"
tags:
  - "docker"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/docker exec — Docker-docs-ja 24.0 ドキュメント.md"
summary: "`docker exec` は、稼働中のコンテナ内で新たにコマンドを実行するためのコマンドです。"
---

# docker exec — Docker-docs-ja 24.0 ドキュメント

## 概要

`docker exec` は、稼働中のコンテナ内で新たにコマンドを実行するためのコマンドです。

## 主要なトピック

- [[docker]]

## 詳細

- `docker exec` は、稼働中のコンテナ内で新たにコマンドを実行するためのコマンドです。
- 主なポイント
- **基本用途**: 実行中のコンテナに対して外部からコマンドを送る際に使用します。
- **実行条件**: コンテナのメインプロセス（PID 1）が稼働中である必要があります。
- **制限事項**:
- コンテナが一時停止（paused）状態では実行できません。
- 連結コマンド（`&&`など）を直接指定すると動作しないため、`sh -c` を介す必要があります。
- **主なオプション**:
- `-d`: バックグラウンドで実行

## 関連テーマ

- [[docker]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/docker exec — Docker-docs-ja 24.0 ドキュメント.md`
- https://docs.docker.jp/engine/reference/commandline/exec.html
