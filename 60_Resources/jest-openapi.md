---
title: "jest-openapi"
source: "https://www.npmjs.com/package/jest-openapi"
author:
published: 2022-01-03
created: 2026-05-01
description: "Jest matchers for asserting that HTTP responses satisfy an OpenAPI spec. Latest version: 0.14.2, last published: 4 years ago. Start using jest-openapi in your project by running `npm i jest-openapi`. There are 3 other projects in the npm registry using jest-openapi."
tags:
  - "clippings"
---
### jest-openapi とは
Jest用のテストプラグインで、APIサーバーのレスポンスやオブジェクトがOpenAPI仕様（Swagger）に準拠しているかを自動検証します。

### 主な特徴
- **検証機能**: HTTPレスポンスのステータスとボディ、および特定のスキーマをOpenAPI仕様に基づきチェック可能。
- **柔軟性**: OpenAPI 2.0 / 3.0、YAML / JSON形式をサポート。
- **連携**: Axios, Supertest, Chai-httpなど主要なHTTPクライアントに対応。
- **読み込み**: ファイルパス、JSオブジェクト、またはURLから仕様を読み込み可能。

### 主な使い方
- `jestOpenAPI('path/to/spec.yml')` で仕様を読み込む。
- APIテスト: `expect(res).toSatisfyApiSpec()` で検証。
- ユニットテスト: `expect(data).toSatisfySchemaInApiSpec('SchemaName')` でスキーマ検証。