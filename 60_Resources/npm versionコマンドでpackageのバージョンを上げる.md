---
title: "npm versionコマンドでpackageのバージョンを上げる"
source: "https://qiita.com/kyntk/items/d03d0fb5f23251515c02"
author:
  - "[[htanjo]]"
published: 2022-07-29
created: 2026-04-30
description: "npmのバージョンを上げ、タグを切ってくれるコマンドがnpmにあるのを知らなかったので、触りながら調べてみました。 sandbox用のpackage作成 npm initをして、最初にversion 0.0.0で作ったpackageを使っていきます。 npm ver..."
tags:
  - "clippings"
---
### 記事の要約
本記事は、Node.js開発でパッケージのバージョン管理とタグ付けを自動化できる`npm version`コマンドの基本的な使い方と実践的なオプションを紹介する技術解説です。

### 要点まとめ
- **`npm version`コマンドの役割**
  - パッケージのバージョン（`package.json`）を更新し、同時にGitのコミットとタグ付けを自動で行います。
- **主なバージョン操作**
  - `patch`: バグ修正（0.0.x）
  - `minor`: 新機能追加（0.x.0）
  - `major`: 破壊的変更（x.0.0）
- **プレリリース設定**
  - `prerelease`: `-0`, `-1`などのサフィックスを付与。
  - `--preid`: `alpha`や`beta`などの識別子を指定可能（例: `1.0.0-alpha.0`）。
- **カスタマイズ**
  - `-m`オプション: バージョン番号を挿入したカスタムコミットメッセージ（例: `Upgrade to %s`）の設定が可能。
