---
title: "Dockerコンテナ上でPuppeteerの実装"
source: "https://qiita.com/kouphasi/items/991c1b9da6d685b9cc36"
author:
  - "[[takayuki-miura0203]]"
published: 2023-01-04
created: 2026-05-01
description: "1.はじめに Webスクレイピングにおいて、用いるツールとして、Selenium, BeautifulSoupなど様々ありますが、JavaScriptにおいてはPuppeteerも代表的なスクレイピングツールとなっております。しかし、PuppeteerはローカルでChro..."
tags:
  - "clippings"
---
### 記事の要約
Dockerコンテナ上でPuppeteer（スクレイピングツール）を正しく動作させるための構成方法を解説した記事です。ローカル環境とは異なり、Docker上ではChromiumの実行に必要な依存ライブラリやフォントが不足しているため、それらをDockerfileで適切に設定する手順を紹介しています。

### 要点まとめ
*   **課題**: Puppeteerはローカルでの実行が前提のため、Dockerコンテナ内ではChromeの実行環境構築が必要。
*   **解決策**: `Dockerfile`で以下のライブラリ群をインストールする。
    *   `google-chrome-stable`（Chrome本体）
    *   各種フォントパッケージ（日本語表示用など）
    *   `libxss1` 等の依存ライブラリ
*   **重要な設定**:
    *   `puppeteer.launch` の引数に `--no-sandbox` を含める必要がある。
    *   `docker-compose` を用いて、起動時に `npm install` とスクリプト実行を行う構成が効率的。
*   **結論**: Dockerでの環境構築を成功させるには、公式ドキュメントに準拠したベースイメージ設定と依存パッケージの導入が不可欠。