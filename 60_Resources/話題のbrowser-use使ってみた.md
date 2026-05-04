---
title: "話題のbrowser-use使ってみた"
source: "https://qiita.com/OtsukaTomoaki/items/d108690f833a67eaee76"
author:
  - "[[OtsukaTomoaki]]"
published: 2025-01-24
created: 2026-04-30
description: "はじめに 開発業務で「情報収集」や「タスク自動化」をするときにスクレイピングやクローリングを用いる場合があると思います。一時期私もスクレイピング関連の本を読んでBeautifulSoup, Seleniumなどを使って自動化をしましたが、CSSセレクタを指定していくのが大..."
tags:
  - "clippings"
---
### 記事の要約
AIを活用してブラウザ操作を自動化するPythonライブラリ「browser-use」の紹介記事です。従来のCSSセレクタに依存したスクレイピング手法の課題を、AIによる指示ベースの操作で解決する実用的な事例が紹介されています。

### 要点まとめ
- **browser-useとは**
  - AI（LLM）がブラウザの操作を代行してくれるライブラリ。
  - テキストで指示を出すだけで、検索や情報抽出、タスク実行が可能。

- **主な特徴・メリット**
  - CSSセレクタやDOM構造の変化に左右されにくい。
  - 複雑なクローリングやデータ抽出コードを最小限に抑えられる。

- **導入手順**
  - `pip install browser-use` と `playwright install` を実行。
  - OpenAIのAPIキー設定（`.env`ファイル）のみで開始可能。

- **活用シーン**
  - Webタスクの自動化・効率化。
  - 特定サイトからのデータ収集（映画情報検索などのデモ事例あり）。
  - 自動テストやアプリケーションの操作自動化。
