---
title: "Hurry Puppeteer とのろいの子"
source: "https://qiita.com/nightyknite/items/41be6919020a2965d30a"
author:
  - "[[nightyknite]]"
published: 2022-11-23
created: 2026-05-01
description: "このタイトル思いついて書いてみたのであとは蛇足みたいなものですが。 Headless Chromeを操作できるNode.jsのライブラリのPuppeteerで重いサイトを快速に使える方法がないか調べてみたがうまいこといかなかった話です。 waitUntilの待つタイミング..."
tags:
  - "clippings"
---
### 記事要約
Puppeteerを使用して重いサイトを高速に操作・スクレイピングするための手法を検証した記録です。特定の万能な解決策はなく、対象サイトの仕様や目的に応じて手法を使い分ける必要性について解説しています。

### 高速化の主なポイント
* **waitUntilの調整**: `domcontentloaded` を活用し、HTML解析完了時点での処理を目指す。
* **起動パラメーターの最適化**: `args` を適切に設定し不要な機能をオフにする（※セキュリティリスクに注意）。
* **ユーザーデータの保存**: `userDataDir` を指定してCSSなどのキャッシュを有効化する。
* **リソースのブロック**: `setRequestInterception` を使い、不要な画像や外部リソースの読み込みを停止する。
* **プロセスの管理**: ゾンビプロセスを防ぐため、必ず `browser.close()` を実行する。
* **ヘッドレスブラウザの回避**: JavaScriptの実行が不要な場合は、`axios` + `jsdom` 等の軽量ライブラリを検討する。
