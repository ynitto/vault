---
title: "VSCodeでTypeScriptをデバッグする環境をつくってみた"
type: "topic"
tags:
  - "node-js"
  - "typescript"
  - "yuzukaki"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/VSCodeでTypeScriptをデバッグする環境をつくってみた.md"
summary: "VSCodeで現在開いているTypeScriptファイルを直接デバッグするための環境構築手順のメモです。"
---

# VSCodeでTypeScriptをデバッグする環境をつくってみた

## 概要

VSCodeで現在開いているTypeScriptファイルを直接デバッグするための環境構築手順のメモです。

*発行: 2019-10-17 / [[node-js-typescript-vscode-typescript-https-c71aef]]*

## 主要なトピック

- [[node-js]]
- [[typescript]]
- [[yuzukaki]]

## 詳細

- VSCodeで現在開いているTypeScriptファイルを直接デバッグするための環境構築手順のメモです。
- 要点
- **目的**: TSファイルへのブレークポイント設定によるデバッグ。
- **環境構築の流れ**:
- 1. **Node.js/npm**: インストール済みであること。
- 2. **TypeScript導入**: `npm install -g typescript` でインストール。
- 3. **プロジェクト初期化**: `tsc --init` で `tsconfig.json` を生成。
- **設定ファイル**:
- `launch.json`: デバッグ構成を定義。`preLaunchTask` でコンパイルを指定し、`program` に `${file}` を設定。

*発行: 2019-10-17 / [[node-js-typescript-vscode-typescript-https-c71aef]]*

## 関連テーマ

- [[node-js]]
- [[typescript]]
- [[yuzukaki]]

## 出典

- `../60_Resources/VSCodeでTypeScriptをデバッグする環境をつくってみた.md`
- https://qiita.com/yuzukaki/items/68ca1aed777b296145d5
