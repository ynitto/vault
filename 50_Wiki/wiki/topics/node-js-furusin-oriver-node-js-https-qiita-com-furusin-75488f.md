---
title: "Node.jsでコマンドライン引数を取得する"
type: "topic"
tags:
  - "node-js"
  - "furusin-oriver"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Node.jsでコマンドライン引数を取得する.md"
summary: "Node.js環境において、コマンドラインから引数を受け取って実行する方法を解説しています。"
---

# Node.jsでコマンドライン引数を取得する

## 概要

Node.js環境において、コマンドラインから引数を受け取って実行する方法を解説しています。

*発行: 2016-09-02 / [[node-js-furusin-oriver-node-js-https-qiita-com-furusin-75488f]]*

## 主要なトピック

- [[node-js]]
- [[furusin-oriver]]

## 詳細

- Node.js環境において、コマンドラインから引数を受け取って実行する方法を解説しています。
- 要点
- **実行方法**
- `$ node [ファイル名] [引数1] [引数2] ...` の形式で実行します。
- **引数の取得方法**
- `process.argv` 配列を使用して取得します。
- **インデックスのルール**
- `process.argv[0]`: 実行コマンド（node）
- `process.argv[1]`: 実行ファイルパス

*発行: 2016-09-02 / [[node-js-furusin-oriver-node-js-https-qiita-com-furusin-75488f]]*

## 関連テーマ

- [[node-js]]
- [[furusin-oriver]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Node.jsでコマンドライン引数を取得する.md`
- https://qiita.com/furusin_oriver/items/f030d1eaa9e7b54233c3
