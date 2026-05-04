---
title: "Puppeteerが遅いなと感じたときの高速化Tips"
source: "https://qiita.com/markey/items/ebf2b48626b6ac61ee89"
author:
  - "[[markey]]"
published: 2019-02-27
created: 2026-05-01
description: "先日、毎朝8時に私の住んでいる地域の洗濯指数をSlackで送ってくれるプログラムを作りました。天気予報とか自分で見ないもので、、今日洗濯しようかどうか決めるのに役立っています。 仕組みとしては、GCPのCloud Scheduler→Pub/Sub→FirebaseのCl..."
tags:
  - "clippings"
---
### 内容要約
PuppeteerをGoogle Cloud Functionsで実行する際に発生するパフォーマンス低下（タイムアウト問題）を解決するための高速化手法を紹介しています。

### 高速化の要点
- **launchオプションの最適化**
    - 不要な機能を無効化するargs設定を追加することで、起動時間を短縮。
    - 設定例: `--disable-gpu`, `--no-sandbox`, `--single-process` など。
- **不要なリクエストのブロック**
    - `page.setRequestInterception(true)`を活用。
    - スクレイピングに不要な画像やCSS、スクリプトの読み込みを`abort()`することで、リソース消費を抑えレスポンス速度を劇的に改善。
- **効果**
    - 上記の対応により、処理時間を30秒以上（タイムアウト）から約5秒まで短縮することに成功。
