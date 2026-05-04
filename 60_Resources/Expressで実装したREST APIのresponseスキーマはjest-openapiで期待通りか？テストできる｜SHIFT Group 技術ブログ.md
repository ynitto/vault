---
title: "Expressで実装したREST APIのresponseスキーマはjest-openapiで期待通りか？テストできる｜SHIFT Group 技術ブログ"
source: "https://note.shiftinc.jp/n/n3725f8a55b8d"
author:
  - "[[SHIFT Group 技術ブログ]]"
published: 2022-01-12
created: 2026-05-01
description: "はじめに  こんにちは、SHIFT の開発部門に所属しているKatayamaです。  今回は前回のREST APIをExpressで実装する際にrequestのスキーマvalidation・sanitizationをするには？の続きで、APIから返されるresponseスキーマがOpenAPIの定義と一致していることをどのようにテストするのか？について理解を深めていこうと思います。これはjest-openapiで簡単に実装でき、その実装を行っていく中で理解した事を備忘録のようなものとしてまとめておこうと思います。 （今後、mockデータではなくDBに接続してCRUDを処理、の1編を続編"
tags:
  - "clippings"
---
### 内容要約
Expressで作成したREST APIのレスポンスが、OpenAPI（Swagger）定義と一致しているかを`jest-openapi`を用いて自動テストする方法についての技術解説です。

### 要点
- **目的**: 実装されたAPIレスポンスが、設計段階で定義したスキーマと乖離していないかをテストで検証する。
- **使用ツール**: `jest-openapi`パッケージを使用。
- **主な実装**: 
    - `jestOpenAPI(path_to_yaml)`でOpenAPI定義を読み込む。
    - テストコード内で `expect(res).toSatisfyApiSpec()` を呼び出し、レスポンスのステータスとスキーマを検証する。
- **重要な注意点**:
    - OpenAPI定義の `responses` や `requestBody` に `examples` キーを含めるとエラーになる場合がある。
    - プロパティごとの `example` は問題なく利用可能。