---
title: "WSL2 の localhostForwarding 機能がうまくうごかない"
source: "https://mrk21.hatenablog.com/entry/2022/01/30/183331"
author:
  - "[[mrk21]]"
published: 2022-01-30
created: 2026-05-01
description: "WSL2 の localhostForwarding 機能を使うと、WSL2側で listen したポートを自動的にWindows側で port forwarding してくれるので、Windows側からは localhost でWSL2側で listen しているポートにアクセスすることができる。 しかし、自分の環境ではアクセスはできるが、頻繁にハングすることがあり困っていた。 そのため、WSL2の localhostForwarding 機能を無効にして、かわりに netsh interface portproxy add v4tov4 コマンドを使って手動で port forwardin…"
tags:
  - "clippings"
---
### 概要
WSL2の標準機能である`localhostForwarding`によるポート転送が不安定（ハングする）な場合の代替手段として、`netsh interface portproxy`コマンドを用いた手動のポート転送設定方法を解説しています。

### 要点
- **課題**: WSL2の自動ポート転送機能が頻繁にハングする。
- **解決策**: `localhostForwarding`を無効にし、Windowsの`netsh`コマンドで手動転送を行う。

### 手順
- **IP取得**: `bash -c \\"ip route |grep 'eth0 proto'|cut -d ' ' -f9\\"`でWSL2のIPアドレスを取得。
- **設定コマンド**: `netsh interface portproxy add v4tov4`を利用してホストとWSL2間をルーティング。
- **自動化**: PowerShellスクリプトを作成し、管理者権限で実行することでポートを指定して転送を確立する。