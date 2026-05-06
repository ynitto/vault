---
title: "Puppeteerが遅いなと感じたときの高速化Tips"
type: "topic"
tags:
  - "performance"
  - "markey"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Puppeteerが遅いなと感じたときの高速化Tips.md"
summary: "PuppeteerをGoogle Cloud Functionsで実行する際に発生するパフォーマンス低下（タイムアウト問題）を解決するための高速化手法を紹…"
---

# Puppeteerが遅いなと感じたときの高速化Tips

## 概要

PuppeteerをGoogle Cloud Functionsで実行する際に発生するパフォーマンス低下（タイムアウト問題）を解決するための高速化手法を紹介しています。

*発行: 2019-02-27 / [[performance-markey-puppeteer-tips-https-ad0d07]]*

## 主要なトピック

- [[performance]]
- [[markey]]

## 詳細

- PuppeteerをGoogle Cloud Functionsで実行する際に発生するパフォーマンス低下（タイムアウト問題）を解決するための高速化手法を紹介しています。
- 高速化の要点
- **launchオプションの最適化**
- 不要な機能を無効化するargs設定を追加することで、起動時間を短縮。
- 設定例: `--disable-gpu`, `--no-sandbox`, `--single-process` など。
- **不要なリクエストのブロック**
- `page.setRequestInterception(true)`を活用。
- スクレイピングに不要な画像やCSS、スクリプトの読み込みを`abort()`することで、リソース消費を抑えレスポンス速度を劇的に改善。
- **効果**

*発行: 2019-02-27 / [[performance-markey-puppeteer-tips-https-ad0d07]]*

## 関連テーマ

- [[performance]]
- [[markey]]

## 出典

- `60_Resources/Puppeteerが遅いなと感じたときの高速化Tips.md`
- https://qiita.com/markey/items/ebf2b48626b6ac61ee89
