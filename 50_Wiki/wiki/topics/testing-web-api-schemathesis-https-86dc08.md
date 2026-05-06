---
title: "Web APIのテストデータを自動生成してくれるツール「Schemathesis」の紹介"
type: "topic"
tags:
  - "testing"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Web APIのテストデータを自動生成してくれるツール「Schemathesis」の紹介.md"
summary: "OpenAPI/GraphQL仕様に基づき、APIのテストデータを自動生成・検証するPythonツール。仕様と実装の乖離や、人間では見落としがちなエッジケ…"
---

# Web APIのテストデータを自動生成してくれるツール「Schemathesis」の紹介

## 概要

OpenAPI/GraphQL仕様に基づき、APIのテストデータを自動生成・検証するPythonツール。仕様と実装の乖離や、人間では見落としがちなエッジケースの発見に有効です。

*発行: 2025-07-18 / [[testing-web-api-schemathesis-https-86dc08]]*

## 主要なトピック

- [[testing]]

## 詳細

- OpenAPI/GraphQL仕様に基づき、APIのテストデータを自動生成・検証するPythonツール。仕様と実装の乖離や、人間では見落としがちなエッジケースの発見に有効です。
- 主な特徴と利点
- **自動生成**: 仕様からテストケースを自動生成し、APIを呼び出す。
- **品質向上**: テストコードでは網羅しきれない境界値や例外ケースをテスト可能。
- **柔軟性**: pytestとの統合や、コマンドライン（CLI）からの単独実行に対応。
- 利用方法
- **pytestとの統合**: `schema.parametrize()`を利用し、pytestのテストとして実行。`from_wsgi`/`from_asgi`を使えばアプリを直接呼び出し高速にテスト可能。
- **CLI実行**: `schemathesis run <URL>`コマンドで、スクリプト作成なしで即座に検証可能。
- **カスタマイズ**: `hypothesis`の戦略定義を用いたテストデータの絞り込みや、`schemathesis.toml`での設定管理が可能。

*発行: 2025-07-18 / [[testing-web-api-schemathesis-https-86dc08]]*

## 関連テーマ

- [[testing]]

## 出典

- `60_Resources/Web APIのテストデータを自動生成してくれるツール「Schemathesis」の紹介.md`
- https://gihyo.jp/article/2025/07/monthly-python-2507
