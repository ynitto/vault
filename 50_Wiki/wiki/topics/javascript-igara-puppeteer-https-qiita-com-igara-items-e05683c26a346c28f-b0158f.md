---
title: "puppeteer経由でインストール済みのアプリケーションを操作する"
type: "topic"
tags:
  - "javascript"
  - "igara"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/puppeteer経由でインストール済みのアプリケーションを操作する.md"
summary: "Puppeteerを使用して、すでにインストールされているデスクトップアプリ（Chrome、Slack、Discordなど）を自動操作・カスタマイズする方…"
---

# puppeteer経由でインストール済みのアプリケーションを操作する

## 概要

Puppeteerを使用して、すでにインストールされているデスクトップアプリ（Chrome、Slack、Discordなど）を自動操作・カスタマイズする方法についての技術解説です。

*発行: 2020-04-07 / [[javascript-igara-puppeteer-https-qiita-com-igara-items-e05683c26a346c28f-b0158f]]*

## 主要なトピック

- [[javascript]]
- [[igara]]

## 詳細

- Puppeteerを使用して、すでにインストールされているデスクトップアプリ（Chrome、Slack、Discordなど）を自動操作・カスタマイズする方法についての技術解説です。
- 要点
- **目的**: チャットツール等で文字以外のコミュニケーションを補完するツール作成の一環として、既存アプリの操作を自動化。
- **対象アプリ**:
- **Chrome**: プロファイル内のCookieを利用してTwitterやFacebookへログイン状態でアクセスし、CSS操作（表示変更）などを実施。
- **Electron**: SlackやDiscordにおいて、`userDataDir`を指定することでログイン状態を保持したままPuppeteerによる制御が可能。
- **主な手法**:
- `executablePath`で各アプリの実行ファイルを指定して起動。
- `page.addStyleTag`によるUIの動的変更。

*発行: 2020-04-07 / [[javascript-igara-puppeteer-https-qiita-com-igara-items-e05683c26a346c28f-b0158f]]*

## 関連テーマ

- [[javascript]]
- [[igara]]

## 出典

- `../60_Resources/puppeteer経由でインストール済みのアプリケーションを操作する.md`
- https://qiita.com/igara/items/e05683c26a346c28feca
