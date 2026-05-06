---
title: "PC起動時にWSL2の自動起動【ログインすらしたくない場合】"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/PC起動時にWSL2の自動起動【ログインすらしたくない場合】.md"
summary: "Windows PCの電源ONのみでWSL2を起動し、ログインなしで外部からSSH接続できるようにするための設定手順のまとめです。"
---

# PC起動時にWSL2の自動起動【ログインすらしたくない場合】

## 概要

Windows PCの電源ONのみでWSL2を起動し、ログインなしで外部からSSH接続できるようにするための設定手順のまとめです。

*発行: 2024-01-27 / [[pc-wsl2-https-zenn-dev-shishimaruwo-articles-f106b12896e2ba-windows-f9846c]]*

## 主要なトピック


## 詳細

- Windows PCの電源ONのみでWSL2を起動し、ログインなしで外部からSSH接続できるようにするための設定手順のまとめです。
- 要点
- **WSLの自動起動**
- タスクスケジューラを使い、システム起動時に `C:\\Program Files\\WSL\\wsl.exe` を実行するように設定。
- **SSHサーバーの構築**
- WSL内に `openssh-server` をインストールし有効化。
- **通信設定**
- Windows側で `netsh interface portproxy` を使用し、Windowsの22番ポートへのアクセスをWSLに転送。
- Windowsファイアウォールで22番ポートのインバウンド/アウトバウンドを許可。

*発行: 2024-01-27 / [[pc-wsl2-https-zenn-dev-shishimaruwo-articles-f106b12896e2ba-windows-f9846c]]*

## 関連テーマ


## 出典

- `../60_Resources/PC起動時にWSL2の自動起動【ログインすらしたくない場合】.md`
- https://zenn.dev/shishimaruwo/articles/f106b12896e2ba
