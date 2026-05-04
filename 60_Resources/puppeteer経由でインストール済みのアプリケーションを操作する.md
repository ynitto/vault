---
title: "puppeteer経由でインストール済みのアプリケーションを操作する"
source: "https://qiita.com/igara/items/e05683c26a346c28feca"
author:
  - "[[igara]]"
published: 2020-04-07
created: 2026-05-01
description: "最初に この記事でやろうとしたことを思ったきっかけとして 最近声をかけられるということが少なくなったのでせめてSlackとかのチャットで文字だけでなく声を発してくれるようなのが欲しいと思ったのがはじまりでした。 （このままだと聞き取り能力下がるんじゃないかというの危険視し..."
tags:
  - "clippings"
---
### 記事の要約
Puppeteerを使用して、すでにインストールされているデスクトップアプリ（Chrome、Slack、Discordなど）を自動操作・カスタマイズする方法についての技術解説です。

### 要点
- **目的**: チャットツール等で文字以外のコミュニケーションを補完するツール作成の一環として、既存アプリの操作を自動化。
- **対象アプリ**:
    - **Chrome**: プロファイル内のCookieを利用してTwitterやFacebookへログイン状態でアクセスし、CSS操作（表示変更）などを実施。
    - **Electron**: SlackやDiscordにおいて、`userDataDir`を指定することでログイン状態を保持したままPuppeteerによる制御が可能。
- **主な手法**:
    - `executablePath`で各アプリの実行ファイルを指定して起動。
    - `page.addStyleTag`によるUIの動的変更。
    - `page.evaluate`を用いた高度なJavaScript実行による操作の自動化。
- **注意点**: macOS環境での検証であり、一部のストレージデータ（ローカルストレージ等）の暗号化による複合化の難しさなど、技術的な制約も言及されています。