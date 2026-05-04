---
title: "WSL2 の localhostForwarding 機能がうまくうごかない"
type: "topic"
tags:
  - "mrk21"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/WSL2 の localhostForwarding 機能がうまくうごかない.md"
summary: "WSL2の標準機能である`localhostForwarding`によるポート転送が不安定（ハングする）な場合の代替手段として、`netsh interf…"
---

# WSL2 の localhostForwarding 機能がうまくうごかない

## 概要

WSL2の標準機能である`localhostForwarding`によるポート転送が不安定（ハングする）な場合の代替手段として、`netsh interface portproxy`コマンドを用いた手動のポート転送設定方法を解説しています。

*発行: 2022-01-30 / [[mrk21-wsl2-localhostforwarding-https-mrk21-hatenablog-com-entry-2022-01-1e0b37]]*

## 主要なトピック

- [[mrk21]]

## 詳細

- WSL2の標準機能である`localhostForwarding`によるポート転送が不安定（ハングする）な場合の代替手段として、`netsh interface portproxy`コマンドを用いた手動のポート転送設定方法を解説しています。
- 要点
- **課題**: WSL2の自動ポート転送機能が頻繁にハングする。
- **解決策**: `localhostForwarding`を無効にし、Windowsの`netsh`コマンドで手動転送を行う。
- 手順
- **IP取得**: `bash -c \\"ip route |grep 'eth0 proto'|cut -d ' ' -f9\\"`でWSL2のIPアドレスを取得。
- **設定コマンド**: `netsh interface portproxy add v4tov4`を利用してホストとWSL2間をルーティング。
- **自動化**: PowerShellスクリプトを作成し、管理者権限で実行することでポートを指定して転送を確立する。

*発行: 2022-01-30 / [[mrk21-wsl2-localhostforwarding-https-mrk21-hatenablog-com-entry-2022-01-1e0b37]]*

## 関連テーマ

- [[mrk21]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/WSL2 の localhostForwarding 機能がうまくうごかない.md`
- https://mrk21.hatenablog.com/entry/2022/01/30/183331
