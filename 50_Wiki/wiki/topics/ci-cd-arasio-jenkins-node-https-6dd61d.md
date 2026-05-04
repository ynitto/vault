---
title: "Jenkins のパイプラインでマスターで実行するタスクを node ブロックで囲む意味 - あらしおブログ"
type: "topic"
tags:
  - "ci-cd"
  - "arasio"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Jenkins のパイプラインでマスターで実行するタスクを node ブロックで囲む意味 - あらしおブログ.md"
summary: "Jenkinsパイプラインにおいて、スクリプトを `node` ブロックで囲むかどうかの違いは、実行に使用される「エグゼキューター」の種類と役割にあります。"
---

# Jenkins のパイプラインでマスターで実行するタスクを node ブロックで囲む意味 - あらしおブログ

## 概要

Jenkinsパイプラインにおいて、スクリプトを `node` ブロックで囲むかどうかの違いは、実行に使用される「エグゼキューター」の種類と役割にあります。

*発行: 2016-10-03 / [[ci-cd-arasio-jenkins-node-https-6dd61d]]*

## 主要なトピック

- [[ci-cd]]
- [[arasio]]

## 詳細

- Jenkinsパイプラインにおいて、スクリプトを `node` ブロックで囲むかどうかの違いは、実行に使用される「エグゼキューター」の種類と役割にあります。
- 要点まとめ
- **エグゼキューターの種類**
- **重量エグゼキューター (Heavyweight):** ノード上で実行される通常のタスク用。スロットを消費し、リソースを占有する。
- **軽量エグゼキューター (Flyweight):** ノード外で実行される一時的な処理用。スロットを消費せず、マスターで実行される。
- **`node` ブロックで囲む理由**
- ビルドなど、リソースを多く消費する重い処理は、マスターへの負荷軽減とスロット管理のために `node` ブロック内で実行すべき。
- **`node` ブロックで囲まない方が良いケース**
- ユーザーの入力を待つ `input` など、長時間のブロッキング処理。

*発行: 2016-10-03 / [[ci-cd-arasio-jenkins-node-https-6dd61d]]*

## 関連テーマ

- [[ci-cd]]
- [[arasio]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Jenkins のパイプラインでマスターで実行するタスクを node ブロックで囲む意味 - あらしおブログ.md`
- https://arasio.hatenablog.com/entry/2016/10/03/011513
