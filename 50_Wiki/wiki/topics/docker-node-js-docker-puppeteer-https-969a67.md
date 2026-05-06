---
title: "Dockerコンテナ上でPuppeteerの実装"
type: "topic"
tags:
  - "docker"
  - "node-js"
  - "takayuki-miura0203"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Dockerコンテナ上でPuppeteerの実装.md"
summary: "Dockerコンテナ上でPuppeteer（スクレイピングツール）を正しく動作させるための構成方法を解説した記事です。ローカル環境とは異なり、Docker…"
---

# Dockerコンテナ上でPuppeteerの実装

## 概要

Dockerコンテナ上でPuppeteer（スクレイピングツール）を正しく動作させるための構成方法を解説した記事です。ローカル環境とは異なり、Docker上ではChromiumの実行に必要な依存ライブラリやフォントが不足しているため、それらをDockerfileで適切に設定する手順を紹介しています。

*発行: 2023-01-04 / [[docker-node-js-docker-puppeteer-https-969a67]]*

## 主要なトピック

- [[docker]]
- [[node-js]]
- [[takayuki-miura0203]]

## 詳細

- Dockerコンテナ上でPuppeteer（スクレイピングツール）を正しく動作させるための構成方法を解説した記事です。ローカル環境とは異なり、Docker上ではChromiumの実行に必要な依存ライブラリやフォントが不足しているため、それらをDockerfileで適切に設定する手順を紹介しています。
- 要点まとめ
- **課題**: Puppeteerはローカルでの実行が前提のため、Dockerコンテナ内ではChromeの実行環境構築が必要。
- **解決策**: `Dockerfile`で以下のライブラリ群をインストールする。
- `google-chrome-stable`（Chrome本体）
- 各種フォントパッケージ（日本語表示用など）
- `libxss1` 等の依存ライブラリ
- **重要な設定**:
- `puppeteer.launch` の引数に `--no-sandbox` を含める必要がある。

*発行: 2023-01-04 / [[docker-node-js-docker-puppeteer-https-969a67]]*

## 関連テーマ

- [[docker]]
- [[node-js]]
- [[takayuki-miura0203]]

## 出典

- `../60_Resources/Dockerコンテナ上でPuppeteerの実装.md`
- https://qiita.com/kouphasi/items/991c1b9da6d685b9cc36
