---
title: "JSON Patchをキャッチアップしました"
type: "topic"
tags:
  - "testing"
  - "taknuki"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/JSON Patchをキャッチアップしました.md"
summary: "JSONドキュメントの一部を更新するための標準規格である「JSON Patch (RFC 6902)」および、その場所を特定するための「JSON Poin…"
---

# JSON Patchをキャッチアップしました

## 概要

JSONドキュメントの一部を更新するための標準規格である「JSON Patch (RFC 6902)」および、その場所を特定するための「JSON Pointer (RFC 6901)」の解説記事です。

*発行: 2021-06-06 / [[testing-taknuki-json-patch-https-7a7a71]]*

## 主要なトピック

- [[testing]]
- [[taknuki]]

## 詳細

- JSONドキュメントの一部を更新するための標準規格である「JSON Patch (RFC 6902)」および、その場所を特定するための「JSON Pointer (RFC 6901)」の解説記事です。
- 要点
- **JSON Pointer**: スラッシュ区切りでJSON内の特定の場所を指し示す仕組み。特殊文字（`/`, `~`）のエスケープが必要。
- **JSON Patchの基本**: `application/json-patch+json`形式で操作内容（オペレーション）を定義し、PATCHメソッドで送信する。
- **主要オペレーション**:
- `add`: 値の追加（配列の場合はインデックスや最後への追加も可）。
- `replace`: 指定した場所の値を置換。
- `remove`: 指定した値の削除。
- `move`: 値の移動。

*発行: 2021-06-06 / [[testing-taknuki-json-patch-https-7a7a71]]*

## 関連テーマ

- [[testing]]
- [[taknuki]]

## 出典

- `60_Resources/JSON Patchをキャッチアップしました.md`
- https://qiita.com/zhang_yid/items/31358f9b2922165ce78d
