---
title: "【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点"
type: "topic"
tags:
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点.md"
summary: "2026年3月31日に発生した axios を悪用したサプライチェーン攻撃に対し、個人の開発環境を守るための具体的な設定方法を解説しています。"
---

# 【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点

## 概要

2026年3月31日に発生した axios を悪用したサプライチェーン攻撃に対し、個人の開発環境を守るための具体的な設定方法を解説しています。

*発行: 2026-04-05 / [[node-js-axios-2-npmrc-ignore-scripts-30264e]]*

## 主要なトピック

- [[node-js]]

## 詳細

- 2026年3月31日に発生した axios を悪用したサプライチェーン攻撃に対し、個人の開発環境を守るための具体的な設定方法を解説しています。
- 対策の要点
- 以下の設定を行うことで、攻撃の被害を未然に防ぐことが可能です。
- 1. postinstall スクリプトの無効化
- **設定**: `npm config set ignore-scripts true`
- **効果**: 悪意のあるパッケージが自動実行するインストーラ（RATドロッパー等）の動作を遮断します。
- **注意**: スクリプトに依存するパッケージが動かなくなった場合は、必要なものだけ `npm rebuild [パッケージ名] --ignore-scripts=false` で個別に許可します。
- 2. 公開直後のパッケージを除外
- **設定**: `npm config set min-release-age 3`

*発行: 2026-04-05 / [[node-js-axios-2-npmrc-ignore-scripts-30264e]]*

## 関連テーマ

- [[node-js]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点.md`
- https://zenn.dev/junko_ai/articles/721d89181b844f
