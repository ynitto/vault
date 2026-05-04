---
title: "VSCode＋Textlintで文章校正をする"
type: "topic"
tags:
  - "node-js"
  - "fuk101"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/VSCode＋Textlintで文章校正をする.md"
summary: "この記事は、Visual Studio Code (VSCode) 上で `textlint` を利用し、Markdown形式の文章を自動校正する環境を構…"
---

# VSCode＋Textlintで文章校正をする

## 概要

この記事は、Visual Studio Code (VSCode) 上で `textlint` を利用し、Markdown形式の文章を自動校正する環境を構築する手順を解説しています。

*発行: 2022-01-25 / [[node-js-fuk101-vscode-textlint-https-226e0c]]*

## 主要なトピック

- [[node-js]]
- [[fuk101]]

## 詳細

- この記事は、Visual Studio Code (VSCode) 上で `textlint` を利用し、Markdown形式の文章を自動校正する環境を構築する手順を解説しています。
- 導入のポイント
- **前提条件:** Node.js のインストールが必須です。
- **プロジェクト準備:** 任意のフォルダをVSCodeで開き、`npm init` で環境を作成します。
- **インストール:** `textlint` 本体と、技術文書向けルールセット (`textlint-rule-preset-ja-technical-writing` 等) を導入します。
- **設定ファイル:** `.textlintrc` ファイルを作成し、使用する校正ルールを定義します。
- **連携:** 拡張機能「vscode-textlint」を導入し、必要に応じて「Node Path」を設定することで、エディタ上でリアルタイムの校正が可能になります。

*発行: 2022-01-25 / [[node-js-fuk101-vscode-textlint-https-226e0c]]*

## 関連テーマ

- [[node-js]]
- [[fuk101]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/VSCode＋Textlintで文章校正をする.md`
- https://qiita.com/fuk101/items/d6e0160f9466363649d7
