---
title: "ESLint Flat Configを使ってみた(課題あり)"
source: "https://zenn.dev/daichi_suyama/articles/d6263aeb9be200"
author:
published: 2023-04-15
created: 2026-05-01
description:
tags:
  - "clippings"
---
### ESLint Flat Config の導入要約
ESLintの新しい設定形式「Flat Config」を試した際の手順と知見についての記事です。

### 要点まとめ
- **有効化方法**
  - プロジェクト直下に `eslint.config.js` を作成する。
  - または環境変数 `ESLINT_USE_FLAT_CONFIG=true` を設定する。
- **VSCodeでの設定**
  - 拡張機能（v2.4.0以降）で利用可能。
  - `settings.json` に `\\"eslint.experimental.useFlatConfig\\": true` を追記して有効化する必要がある。
- **設定ファイルの書き方**
  - `export default [...]` を使用。
  - `files` キーで対象ファイルを指定、`ignores` キーで除外設定が可能。
- **現状の注意点**
  - 環境によりCommonJS記法でないと動作しないケースがある。
  - Reactへの適用や本番環境への導入は、公式の対応進捗を見極める段階である。