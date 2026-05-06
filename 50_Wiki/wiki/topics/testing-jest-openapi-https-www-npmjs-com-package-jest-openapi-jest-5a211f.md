---
title: "jest-openapi"
type: "topic"
tags:
  - "testing"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/jest-openapi.md"
summary: "Jest用のテストプラグインで、APIサーバーのレスポンスやオブジェクトがOpenAPI仕様（Swagger）に準拠しているかを自動検証します。"
---

# jest-openapi

## 概要

Jest用のテストプラグインで、APIサーバーのレスポンスやオブジェクトがOpenAPI仕様（Swagger）に準拠しているかを自動検証します。

*発行: 2022-01-03 / [[testing-jest-openapi-https-www-npmjs-com-package-jest-openapi-jest-5a211f]]*

## 主要なトピック

- [[testing]]

## 詳細

- Jest用のテストプラグインで、APIサーバーのレスポンスやオブジェクトがOpenAPI仕様（Swagger）に準拠しているかを自動検証します。
- 主な特徴
- **検証機能**: HTTPレスポンスのステータスとボディ、および特定のスキーマをOpenAPI仕様に基づきチェック可能。
- **柔軟性**: OpenAPI 2.0 / 3.0、YAML / JSON形式をサポート。
- **連携**: Axios, Supertest, Chai-httpなど主要なHTTPクライアントに対応。
- **読み込み**: ファイルパス、JSオブジェクト、またはURLから仕様を読み込み可能。
- 主な使い方
- `jestOpenAPI('path/to/spec.yml')` で仕様を読み込む。
- APIテスト: `expect(res).toSatisfyApiSpec()` で検証。

*発行: 2022-01-03 / [[testing-jest-openapi-https-www-npmjs-com-package-jest-openapi-jest-5a211f]]*

## 関連テーマ

- [[testing]]

## 出典

- `60_Resources/jest-openapi.md`
- https://www.npmjs.com/package/jest-openapi
