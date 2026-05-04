---
title: "【Fiddler】Windows 上で HTTP / HTTPS 通信をキャプチャする"
source: "https://qiita.com/nt-7/items/c897e9460ef43af6ed14"
author:
  - "[[nt-7]]"
published: 2021-06-07
created: 2026-05-01
description: "本記事では Windows 上で HTTP / HTTPS 通信のリクエスト、レスポンスを確認したり、そのトラブルシューティング等に利用できる便利なツール「Fiddler」をご紹介します。 色々便利な機能はありますが、とりあえず今回の記事ではシンプルに導入からキャプチャ・保..."
tags:
  - "clippings"
---
### 記事の要約
Windows環境におけるHTTP/HTTPS通信のキャプチャ・解析ツール「Fiddler Classic」の導入から、基本的な操作方法およびログ保存手順を解説しています。

### 主要なポイント
- **Fiddlerの役割**
  - WebデバッギングプロキシとしてHTTP/HTTPS通信を記録・解析可能。
  - HTTPS通信の復号やWebSocketのキャプチャにも対応。

- **初期セットアップ**
  - ツール起動後、通信キャプチャを一時停止し、ログをクリア。
  - [Tools] > [Options] > [HTTPS] タブからHTTPS通信の復号設定（Decrypt HTTPS traffic）を有効化し、証明書をインストールする。

- **キャプチャ手順**
  - [File] メニューからキャプチャを開始（Capturingと表示）。
  - ブラウザで対象の操作を実行し、終了後にキャプチャを停止。
  - 右側の「Inspectors」タブで各リクエスト/レスポンスの詳細を確認可能。

- **データの共有・応用**
  - [File] > [Save] > [All Sessions] で`.saz`形式としてログを保存・共有できる。
  - 拡張機能（FiddlerImportNetlog）を導入することで、ブラウザのNetLog（net-export）ファイルの読み込みにも対応。
