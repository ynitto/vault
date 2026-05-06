---
title: "npm link について調べる"
type: "topic"
tags:
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/npm link について調べる.md"
summary: "npm linkは、自作パッケージを公開せずに別のプロジェクトからローカル参照として利用するためのコマンドです。シンボリックリンクを作成することで、開発中…"
---

# npm link について調べる

## 概要

npm linkは、自作パッケージを公開せずに別のプロジェクトからローカル参照として利用するためのコマンドです。シンボリックリンクを作成することで、開発中の変更を即座に反映させることが可能です。

*発行: 2022/12/27にコメント追加 / [[node-js-npm-link-https-zenn-dev-negi-scraps-ff8cc6bf68521a-72fa6b]]*

## 主要なトピック

- [[node-js]]

## 詳細

- npm linkは、自作パッケージを公開せずに別のプロジェクトからローカル参照として利用するためのコマンドです。シンボリックリンクを作成することで、開発中の変更を即座に反映させることが可能です。
- 手順まとめ
- 1. パッケージを提供する側
- 対象ディレクトリで `npm link` を実行する。
- グローバル領域にパッケージのシンボリックリンクが作成されます。
- 2. パッケージを使う側
- 利用したいプロジェクトのディレクトリで `npm link <パッケージ名>` を実行する。
- `node_modules` 内にパッケージへのシンボリックリンクが作成され、通常のパッケージと同様に `import` が可能になります。
- 3. 削除手順（解除）

*発行: 2022/12/27にコメント追加 / [[node-js-npm-link-https-zenn-dev-negi-scraps-ff8cc6bf68521a-72fa6b]]*

## 関連テーマ

- [[node-js]]

## 出典

- `60_Resources/npm link について調べる.md`
- https://zenn.dev/negi/scraps/ff8cc6bf68521a
