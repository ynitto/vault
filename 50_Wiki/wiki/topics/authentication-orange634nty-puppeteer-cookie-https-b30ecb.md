---
title: "PuppeteerでCookieを使ってログインする方法"
type: "topic"
tags:
  - "authentication"
  - "orange634nty"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/PuppeteerでCookieを使ってログインする方法.md"
summary: "Puppeteerを使用してWebサイトへのログインを自動化し、Cookie情報を保存・再利用することで、ログイン状態が必要なページを効率的にスクレイピン…"
---

# PuppeteerでCookieを使ってログインする方法

## 概要

Puppeteerを使用してWebサイトへのログインを自動化し、Cookie情報を保存・再利用することで、ログイン状態が必要なページを効率的にスクレイピングする方法の解説記事です。

*発行: 2019-06-09 / [[authentication-orange634nty-puppeteer-cookie-https-b30ecb]]*

## 主要なトピック

- [[authentication]]
- [[orange634nty]]

## 詳細

- Puppeteerを使用してWebサイトへのログインを自動化し、Cookie情報を保存・再利用することで、ログイン状態が必要なページを効率的にスクレイピングする方法の解説記事です。
- 要点
- **ログインとCookie保存**
- Puppeteerでログイン処理を行い、`page.cookies()`でCookieを取得・ファイルへJSON出力する。
- **Cookieの再利用**
- 保存したJSONを読み込み、`page.setCookie()`でブラウザにセットすることで、再ログインなしで認証が必要なページへアクセスする。
- **注意点**
- 負荷軽減のため、対象サイトの規約を遵守すること。
- WebAPIが提供されている場合は、APIの利用を優先すること。

*発行: 2019-06-09 / [[authentication-orange634nty-puppeteer-cookie-https-b30ecb]]*

## 関連テーマ

- [[authentication]]
- [[orange634nty]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/PuppeteerでCookieを使ってログインする方法.md`
- https://qiita.com/orange634nty/items/8971bfa9349125ba0a78
