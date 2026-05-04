---
title: "How to use Puppeteer inside a Docker container"
source: "https://dev.to/cloudx/how-to-use-puppeteer-inside-a-docker-container-568c"
author:
published: 2022-03-31
created: 2026-05-01
description: "Introduction   Puppeteer is a Node.js library which provides a high-level API to control... Tagged with docker, node, javascript, automation."
tags:
  - "clippings"
---
### 要約
この記事は、Node.jsのライブラリ「Puppeteer」をDockerコンテナ内で安定して実行するための最適な設定方法とDockerfileの例を解説しています。

### 要点
- **課題**: Node.jsの公式イメージに含まれるDebian版Chromiumはバージョンが古く、最新のPuppeteerと互換性がない場合がある。
- **解決策**: Google Chrome公式のDebianパッケージをインストールすることで、常に最新の安定版を利用する。
- **Dockerfileのポイント**:
  - `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD`を`true`に設定し、内蔵のChromiumダウンロードをスキップする。
  - `google-chrome-stable`をaptでインストールする。
  - 依存ライブラリを適切にインストールすることで動作を安定させる。
- **注意点**:
  - ARMベースのCPU（Apple M1など）ではビルド時に`--platform linux/amd64`を指定する必要がある。
  - Puppeteer起動時に`executablePath: '/usr/bin/google-chrome'`を設定し、インストールしたChromeを指定する。
  - 実行環境（Lambda等）によっては、必要なX11関連の依存パッケージが不足していないか確認が必要。