---
title: "JSONもどき（値として関数を持つ）をJSON.stringifyしたりJSON.parseしたりする"
type: "topic"
tags:
  - "javascript"
  - "suetake"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/JSONもどき（値として関数を持つ）をJSON.stringifyしたりJSON.parseしたりする.md"
summary: "JavaScriptにおいて、通常は仕様上不可能な「関数を含むオブジェクト（JSONもどき）」を、`JSON.stringify`で文字列化し、`JSON…"
---

# JSONもどき（値として関数を持つ）をJSON.stringifyしたりJSON.parseしたりする

## 概要

JavaScriptにおいて、通常は仕様上不可能な「関数を含むオブジェクト（JSONもどき）」を、`JSON.stringify`で文字列化し、`JSON.parse`で元の関数付きオブジェクトに復元する手法を解説した記事。

*発行: 2013-10-09 / [[javascript-suetake-json-json-stringify-json-parse-7e2273]]*

## 主要なトピック

- [[javascript]]
- [[suetake]]

## 詳細

- JavaScriptにおいて、通常は仕様上不可能な「関数を含むオブジェクト（JSONもどき）」を、`JSON.stringify`で文字列化し、`JSON.parse`で元の関数付きオブジェクトに復元する手法を解説した記事。
- 要点
- **背景**: JSON標準仕様では関数を含めることができないため、関数を持つオブジェクトのシリアライズには工夫が必要。
- **解決策**:
- **変換**: シリアライズ前に、値が関数のものを文字列へ変換する。
- **復元**: `JSON.parse`の第二引数（レブーバー関数）を利用し、文字列化された関数を`eval()`で再評価して関数に戻す。
- **簡単な実装テクニック**:
- `Function.prototype.toJSON = Function.prototype.toString;` を定義することで、`JSON.stringify`呼び出し時に自動的に関数が文字列化されるようになり、記述を簡略化できる。
- **注意点**: 内部ツールや特定のコンテキスト内での利用を想定したTipsである。

*発行: 2013-10-09 / [[javascript-suetake-json-json-stringify-json-parse-7e2273]]*

## 関連テーマ

- [[javascript]]
- [[suetake]]

## 出典

- `../60_Resources/JSONもどき（値として関数を持つ）をJSON.stringifyしたりJSON.parseしたりする.md`
- https://qiita.com/emadurandal/items/37fae542938907ef5d0c
