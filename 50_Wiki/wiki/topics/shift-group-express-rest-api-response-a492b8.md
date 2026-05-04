---
title: "Expressで実装したREST APIのresponseスキーマはjest-openapiで期待通りか？テストできる｜SHIFT Group 技術ブログ"
type: "topic"
tags:
  - "shift-group"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Expressで実装したREST APIのresponseスキーマはjest-openapiで期待通りか？テストできる｜SHIFT Group 技術ブログ.md"
summary: "Expressで作成したREST APIのレスポンスが、OpenAPI（Swagger）定義と一致しているかを`jest-openapi`を用いて自動テス…"
---

# Expressで実装したREST APIのresponseスキーマはjest-openapiで期待通りか？テストできる｜SHIFT Group 技術ブログ

## 概要

Expressで作成したREST APIのレスポンスが、OpenAPI（Swagger）定義と一致しているかを`jest-openapi`を用いて自動テストする方法についての技術解説です。

*発行: 2022-01-12 / [[shift-group-express-rest-api-response-a492b8]]*

## 主要なトピック

- [[shift-group]]

## 詳細

- Expressで作成したREST APIのレスポンスが、OpenAPI（Swagger）定義と一致しているかを`jest-openapi`を用いて自動テストする方法についての技術解説です。
- 要点
- **目的**: 実装されたAPIレスポンスが、設計段階で定義したスキーマと乖離していないかをテストで検証する。
- **使用ツール**: `jest-openapi`パッケージを使用。
- **主な実装**:
- `jestOpenAPI(path_to_yaml)`でOpenAPI定義を読み込む。
- テストコード内で `expect(res).toSatisfyApiSpec()` を呼び出し、レスポンスのステータスとスキーマを検証する。
- **重要な注意点**:
- OpenAPI定義の `responses` や `requestBody` に `examples` キーを含めるとエラーになる場合がある。

*発行: 2022-01-12 / [[shift-group-express-rest-api-response-a492b8]]*

## 関連テーマ

- [[shift-group]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Expressで実装したREST APIのresponseスキーマはjest-openapiで期待通りか？テストできる｜SHIFT Group 技術ブログ.md`
- https://note.shiftinc.jp/n/n3725f8a55b8d
