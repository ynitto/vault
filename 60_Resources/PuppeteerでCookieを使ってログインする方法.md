---
title: "PuppeteerでCookieを使ってログインする方法"
source: "https://qiita.com/orange634nty/items/8971bfa9349125ba0a78"
author:
  - "[[orange634nty]]"
published: 2019-06-09
created: 2026-05-01
description: "Slackのボットと様々なWebAPIを組み合わせて、Slack上から情報を得られるのは非常に便利です。 しかし、サービスによってはWebAPIがなくCookie認証が必要な場合があります。 そういったサービスにPuppetteerを使ってログインしてスクレイピングする方法..."
tags:
  - "clippings"
---
### 内容の要約
Puppeteerを使用してWebサイトへのログインを自動化し、Cookie情報を保存・再利用することで、ログイン状態が必要なページを効率的にスクレイピングする方法の解説記事です。

### 要点
- **ログインとCookie保存**
  - Puppeteerでログイン処理を行い、`page.cookies()`でCookieを取得・ファイルへJSON出力する。
- **Cookieの再利用**
  - 保存したJSONを読み込み、`page.setCookie()`でブラウザにセットすることで、再ログインなしで認証が必要なページへアクセスする。
- **注意点**
  - 負荷軽減のため、対象サイトの規約を遵守すること。
  - WebAPIが提供されている場合は、APIの利用を優先すること。