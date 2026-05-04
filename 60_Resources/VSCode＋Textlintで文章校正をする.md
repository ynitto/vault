---
title: "VSCode＋Textlintで文章校正をする"
source: "https://qiita.com/fuk101/items/d6e0160f9466363649d7"
author:
  - "[[fuk101]]"
published: 2022-01-25
created: 2026-05-01
description: "はじめに Visual Studio Code（VSCode）＋textlintで文章校正をするための導入手順です。 環境 Windows11 64bit Visual Studio Code version 1.63 Node.js v16.13.2 npm 8.1..."
tags:
  - "clippings"
---
### 要約
この記事は、Visual Studio Code (VSCode) 上で `textlint` を利用し、Markdown形式の文章を自動校正する環境を構築する手順を解説しています。

### 導入のポイント
- **前提条件:** Node.js のインストールが必須です。
- **プロジェクト準備:** 任意のフォルダをVSCodeで開き、`npm init` で環境を作成します。
- **インストール:** `textlint` 本体と、技術文書向けルールセット (`textlint-rule-preset-ja-technical-writing` 等) を導入します。
- **設定ファイル:** `.textlintrc` ファイルを作成し、使用する校正ルールを定義します。
- **連携:** 拡張機能「vscode-textlint」を導入し、必要に応じて「Node Path」を設定することで、エディタ上でリアルタイムの校正が可能になります。