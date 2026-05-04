---
title: "openapi-generator/docs/generators/cwiki.md at master"
source: "https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/cwiki.md"
author:
published:
created: 2026-05-01
description: "OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3) - openapi-generator/docs/generators/cwiki.md at master · OpenAPITools/openapi-generator"
tags:
  - "clippings"
---
### 概要
本ドキュメントは、OpenAPI Generatorにおける「cwiki」ジェネレーターの仕様書です。このジェネレーターは、OpenAPI定義からConfluence Wiki用のマークアップ言語を生成するツールです。

### 要点
- **基本情報**
    - ジェネレーター名: `cwiki`
    - タイプ: `DOCUMENTATION` (ドキュメント生成)
    - テンプレートエンジン: `mustache`
    - 安定性: `STABLE`

- **主な設定オプション**
    - `enumUnknownDefaultCase`: enumの型安全性を高めるためのデフォルト値生成機能。
    - `sortParamsByRequiredFlag` / `sortModelPropertiesByRequiredFlag`: 必須パラメーターを先頭にソートする機能。
    - `disallowAdditionalPropertiesIfNotPresent`: JSONスキーマ仕様への準拠制御。

- **対応機能**
    - **データ型**: Int, Float, Double, String, Boolean, Date, DateTime, Map, Arrayなど、主要な型をサポート。
    - **グローバル機能**: Host, BasePath, Info, Consumes/Produces, ExternalDocumentationなど、APIドキュメントに必要な基本構成に対応。
    - **パラメーター**: Path, Query, Header, Body, Formなど広範囲に対応。
    - **制限事項**: Security (認証関連) や `allOf`/`oneOf` などの高度なポリモーフィズム/スキーマ合成には非対応。