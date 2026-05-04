---
title: "TypeScript の\"is\"と\"in\"を理解する"
source: "https://qiita.com/ryo2132/items/ce9e13899e45dcfaff9b"
author:
  - "[[ryo2132]]"
published: 2020-04-29
created: 2026-04-30
description: "TypeScript の構文の中でも、屈指のググラビリティの低さを誇る is と in を自分なりにまとめてみました。 \"is\" is は TypeScript の型推論を補強する user-defined type guard（ユーザー定義型ガード） で使われます。 u..."
tags:
  - "clippings"
---
### 記事の要約
TypeScriptにおける「is」と「in」という、型推論を補助・活用するための重要な構文についての解説記事です。

### 要点まとめ
- **「is」（ユーザー定義型ガード）**
    - **役割**: 関数内で戻り値に `引数 is 型` を指定することで、コンパイラに対して型情報を明示的に教える。
    - **活用**: `unknown` 型や `Union` 型の変数を、特定の型に絞り込む際に使用する。
    - **注意点**: 内部の型判定と `is` で指定する型が一致しないと、コンパイルは通っても実行時エラーになる可能性がある。

- **「in」（プロパティ存在確認・mapped types）**
    - **役割1（型ガード）**: オブジェクトが特定のプロパティを持つかを判定し、その結果に基づいて型を絞り込む。
    - **役割2（Mapped Types）**: `[P in keyof T]` のように記述し、既存の型のキーを反復処理して新しい型を定義する。
