---
title: "Integrating with Jest | Step CI Docs"
type: "topic"
tags:
  - "testing"
  - "javascript"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Integrating with Jest  Step CI Docs.md"
summary: "このドキュメントでは、JavaScriptのテストフレームワーク「Jest」でStep CIランナーを使用してAPIテストを実行する方法を解説しています。"
---

# Integrating with Jest | Step CI Docs

## 概要

このドキュメントでは、JavaScriptのテストフレームワーク「Jest」でStep CIランナーを使用してAPIテストを実行する方法を解説しています。

*発行: 2024-08-03 / [[testing-javascript-integrating-jest-step-e035d3]]*

## 主要なトピック

- [[testing]]
- [[javascript]]
- [[node-js]]

## 詳細

- このドキュメントでは、JavaScriptのテストフレームワーク「Jest」でStep CIランナーを使用してAPIテストを実行する方法を解説しています。
- 準備
- **ディレクトリ構成**: ワークフローファイルを `tests/` フォルダ内に配置。
- **依存関係のインストール**: 以下のコマンドを実行します。
- `npm install --save-dev @stepci/runner`
- テスト実行方法
- **ファイルから実行**: `runFromFile` 関数を使用し、ワークフローファイルを読み込んでテストします。
- **設定オブジェクトから直接実行**: `run` 関数に直接ワークフローの定義（YAML相当のオブジェクト）を渡してテストします。
- ポイント

*発行: 2024-08-03 / [[testing-javascript-integrating-jest-step-e035d3]]*

## 関連テーマ

- [[testing]]
- [[javascript]]
- [[node-js]]

## 出典

- `60_Resources/Integrating with Jest  Step CI Docs.md`
- https://docs.stepci.com/integration/jest.html
