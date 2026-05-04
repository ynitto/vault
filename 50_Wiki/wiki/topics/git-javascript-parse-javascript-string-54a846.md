---
title: "Parse a JavaScript string function definition and return a function object. Does not use eval."
type: "topic"
tags:
  - "git"
  - "javascript"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Parse a JavaScript string function definition and return a function object. Does not use eval..md"
summary: "GitHub Gistに投稿された、文字列として定義されたJavaScript関数を`eval`を使用せずに再構成し、実行可能な関数オブジェクトに変換する…"
---

# Parse a JavaScript string function definition and return a function object. Does not use eval.

## 概要

GitHub Gistに投稿された、文字列として定義されたJavaScript関数を`eval`を使用せずに再構成し、実行可能な関数オブジェクトに変換するユーティリティコードです。

## 主要なトピック

- [[git]]
- [[javascript]]

## 詳細

- GitHub Gistに投稿された、文字列として定義されたJavaScript関数を`eval`を使用せずに再構成し、実行可能な関数オブジェクトに変換するユーティリティコードです。
- 主要なポイント
- **機能**: 関数定義の文字列から関数名、引数、本体を抽出し、`Function`コンストラクタを用いて新しい関数を生成します。
- **仕組み**:
- 関数文字列の`{}`や`()`の位置から要素を分解。
- `Function.apply`を使用してスコープと引数を引き継ぎます。
- **利点**:
- `eval`を回避することで、セキュリティリスクやデバッグの難しさを軽減します。
- **制限と課題**:

## 関連テーマ

- [[git]]
- [[javascript]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Parse a JavaScript string function definition and return a function object. Does not use eval..md`
- https://gist.github.com/lamberta/3768814
