---
title: "VSCodeでTypeScriptをデバッグする環境をつくってみた"
source: "https://qiita.com/yuzukaki/items/68ca1aed777b296145d5"
author:
  - "[[yuzukaki]]"
published: 2019-10-17
created: 2026-05-01
description: "VSCodeでTypeScriptをデバッグする環境をつくってみた 環境作った足跡メモです。 色々と雑でごめんなさい。 やりたいこと 目的：VSCodeでTypeScriptをデバッグしたい 要件 ブレークポイントを設定してデバッグしたいのはTypeScript（生..."
tags:
  - "clippings"
---
### 概要
VSCodeで現在開いているTypeScriptファイルを直接デバッグするための環境構築手順のメモです。

### 要点
- **目的**: TSファイルへのブレークポイント設定によるデバッグ。
- **環境構築の流れ**:
    1. **Node.js/npm**: インストール済みであること。
    2. **TypeScript導入**: `npm install -g typescript` でインストール。
    3. **プロジェクト初期化**: `tsc --init` で `tsconfig.json` を生成。
- **設定ファイル**: 
    - `launch.json`: デバッグ構成を定義。`preLaunchTask` でコンパイルを指定し、`program` に `${file}` を設定。
    - `tasks.json`: コンパイルタスクを定義し、`launch.json` と連携。
    - `tsconfig.json`: `sourceMap: true` に設定し、デバッグ用にソースマップを生成。
- **動作確認**: VSCode上で対象ファイルを開き、定義したデバッグ構成を実行することでブレークポイントでの一時停止が可能。
