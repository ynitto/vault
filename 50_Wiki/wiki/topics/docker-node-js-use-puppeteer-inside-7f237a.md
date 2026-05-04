---
title: "How to use Puppeteer inside a Docker container"
type: "topic"
tags:
  - "docker"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How to use Puppeteer inside a Docker container.md"
summary: "この記事は、Node.jsのライブラリ「Puppeteer」をDockerコンテナ内で安定して実行するための最適な設定方法とDockerfileの例を解説…"
---

# How to use Puppeteer inside a Docker container

## 概要

この記事は、Node.jsのライブラリ「Puppeteer」をDockerコンテナ内で安定して実行するための最適な設定方法とDockerfileの例を解説しています。

*発行: 2022-03-31 / [[docker-node-js-use-puppeteer-inside-7f237a]]*

## 主要なトピック

- [[docker]]
- [[node-js]]

## 詳細

- この記事は、Node.jsのライブラリ「Puppeteer」をDockerコンテナ内で安定して実行するための最適な設定方法とDockerfileの例を解説しています。
- 要点
- **課題**: Node.jsの公式イメージに含まれるDebian版Chromiumはバージョンが古く、最新のPuppeteerと互換性がない場合がある。
- **解決策**: Google Chrome公式のDebianパッケージをインストールすることで、常に最新の安定版を利用する。
- **Dockerfileのポイント**:
- `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD`を`true`に設定し、内蔵のChromiumダウンロードをスキップする。
- `google-chrome-stable`をaptでインストールする。
- 依存ライブラリを適切にインストールすることで動作を安定させる。
- **注意点**:

*発行: 2022-03-31 / [[docker-node-js-use-puppeteer-inside-7f237a]]*

## 関連テーマ

- [[docker]]
- [[node-js]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How to use Puppeteer inside a Docker container.md`
- https://dev.to/cloudx/how-to-use-puppeteer-inside-a-docker-container-568c
