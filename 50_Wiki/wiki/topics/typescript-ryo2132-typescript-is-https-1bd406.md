---
title: "TypeScript の\"is\"と\"in\"を理解する"
type: "topic"
tags:
  - "typescript"
  - "ryo2132"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/TypeScript のisとinを理解する.md"
summary: "TypeScriptにおける「is」と「in」という、型推論を補助・活用するための重要な構文についての解説記事です。"
---

# TypeScript の\"is\"と\"in\"を理解する

## 概要

TypeScriptにおける「is」と「in」という、型推論を補助・活用するための重要な構文についての解説記事です。

*発行: 2020-04-29 / [[typescript-ryo2132-typescript-is-https-1bd406]]*

## 主要なトピック

- [[typescript]]
- [[ryo2132]]

## 詳細

- TypeScriptにおける「is」と「in」という、型推論を補助・活用するための重要な構文についての解説記事です。
- 要点まとめ
- **「is」（ユーザー定義型ガード）**
- **役割**: 関数内で戻り値に `引数 is 型` を指定することで、コンパイラに対して型情報を明示的に教える。
- **活用**: `unknown` 型や `Union` 型の変数を、特定の型に絞り込む際に使用する。
- **注意点**: 内部の型判定と `is` で指定する型が一致しないと、コンパイルは通っても実行時エラーになる可能性がある。
- **「in」（プロパティ存在確認・mapped types）**
- **役割1（型ガード）**: オブジェクトが特定のプロパティを持つかを判定し、その結果に基づいて型を絞り込む。
- **役割2（Mapped Types）**: `[P in keyof T]` のように記述し、既存の型のキーを反復処理して新しい型を定義する。

*発行: 2020-04-29 / [[typescript-ryo2132-typescript-is-https-1bd406]]*

## 関連テーマ

- [[typescript]]
- [[ryo2132]]

## 出典

- `../60_Resources/TypeScript のisとinを理解する.md`
- https://qiita.com/ryo2132/items/ce9e13899e45dcfaff9b
