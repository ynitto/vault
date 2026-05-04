---
title: "Integrating with Jest | Step CI Docs"
source: "https://docs.stepci.com/integration/jest.html"
author:
published: 2024-08-03
created: 2026-05-01
description: "API Testing and Monitoring made simple."
tags:
  - "clippings"
---
### ステップCIのJest統合ガイド
このドキュメントでは、JavaScriptのテストフレームワーク「Jest」でStep CIランナーを使用してAPIテストを実行する方法を解説しています。

#### 準備
- **ディレクトリ構成**: ワークフローファイルを `tests/` フォルダ内に配置。
- **依存関係のインストール**: 以下のコマンドを実行します。
  `npm install --save-dev @stepci/runner`

#### テスト実行方法
- **ファイルから実行**: `runFromFile` 関数を使用し、ワークフローファイルを読み込んでテストします。
- **設定オブジェクトから直接実行**: `run` 関数に直接ワークフローの定義（YAML相当のオブジェクト）を渡してテストします。

#### ポイント
- `@stepci/runner` を導入することで、既存のJestテストスイート内にAPIテストを組み込めます。
- `result.passed` を検証することで、テストの成功・失敗をJestの `expect` で簡単に判定可能です。