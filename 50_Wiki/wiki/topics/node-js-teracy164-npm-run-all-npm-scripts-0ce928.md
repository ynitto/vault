---
title: "npm-run-allでnpm scriptsを整理してみた"
type: "topic"
tags:
  - "node-js"
  - "teracy164"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/npm-run-allでnpm scriptsを整理してみた.md"
summary: "Angularのマルチプロジェクト環境において、複雑化しがちな`package.json`のスクリプト管理を、`npm-run-all`を使って効率化・簡…"
---

# npm-run-allでnpm scriptsを整理してみた

## 概要

Angularのマルチプロジェクト環境において、複雑化しがちな`package.json`のスクリプト管理を、`npm-run-all`を使って効率化・簡潔化する方法を解説した記事です。

*発行: 2020-04-02 / [[node-js-teracy164-npm-run-all-npm-scripts-0ce928]]*

## 主要なトピック

- [[node-js]]
- [[teracy164]]

## 詳細

- Angularのマルチプロジェクト環境において、複雑化しがちな`package.json`のスクリプト管理を、`npm-run-all`を使って効率化・簡潔化する方法を解説した記事です。
- 要点
- **課題**
- プロジェクトが増えるたびにビルドやウォッチスクリプトを個別に定義する必要があり、メンテナンスが困難。
- **解決策：`npm-run-all`の活用**
- **ワイルドカード (`*`)**: `build-app:*`のように記述することで、該当する複数のスクリプトを一括実行。
- **並列・直列実行**: `run-s` (直列) や `run-p` (並列) を使い分け、実行フローを制御。
- **引数の利用**: `{1}` を使い、動的に対象プロジェクトを指定してスクリプトを実行可能。
- **メリット**

*発行: 2020-04-02 / [[node-js-teracy164-npm-run-all-npm-scripts-0ce928]]*

## 関連テーマ

- [[node-js]]
- [[teracy164]]

## 出典

- `../60_Resources/npm-run-allでnpm scriptsを整理してみた.md`
- https://qiita.com/teracy164/items/88eacfae61a683f6a29b
