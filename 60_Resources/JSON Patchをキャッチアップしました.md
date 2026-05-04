---
title: "JSON Patchをキャッチアップしました"
source: "https://qiita.com/zhang_yid/items/31358f9b2922165ce78d"
author:
  - "[[taknuki]]"
published: 2021-06-06
created: 2026-04-30
description: "前書き JavaScript Object Notation (JSON) Pointer JavaScript Object Notation (JSON) Patch についてキャッチアップしました。 今は API デザインしているので、PATCHに関する操作であ..."
tags:
  - "clippings"
---
### JSON Patchの要約
JSONドキュメントの一部を更新するための標準規格である「JSON Patch (RFC 6902)」および、その場所を特定するための「JSON Pointer (RFC 6901)」の解説記事です。

### 要点
- **JSON Pointer**: スラッシュ区切りでJSON内の特定の場所を指し示す仕組み。特殊文字（`/`, `~`）のエスケープが必要。
- **JSON Patchの基本**: `application/json-patch+json`形式で操作内容（オペレーション）を定義し、PATCHメソッドで送信する。
- **主要オペレーション**:
    - `add`: 値の追加（配列の場合はインデックスや最後への追加も可）。
    - `replace`: 指定した場所の値を置換。
    - `remove`: 指定した値の削除。
    - `move`: 値の移動。
    - `test`: 指定値と一致するかテスト（変更前の検証用）。
- **実装上の注意点**:
    - 空中衝突防止のため、`If-Match`ヘッダーの活用が推奨される。
    - 各操作は存在しないパスに対して行うとエラーになる。
