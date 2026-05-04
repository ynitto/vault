---
title: "\"new Function\" 構文"
source: "https://ja.javascript.info/new-function"
author:
published:
created: 2026-05-01
description:
tags:
  - "clippings"
---
### new Function 構文の要約
`new Function` は、実行時に文字列から関数を生成するための特殊な方法です。通常は使用されませんが、サーバから動的にコードを受け取るような特殊なケースで利用されます。

#### 主要なポイント
- **構文**: `let func = new Function([arg1, arg2, ...argN], functionBody)`
- **実行環境**: `new Function` で作成された関数は、生成元のレキシカル環境ではなく、**グローバル環境**のみを参照します。
- **外部変数へのアクセス**: 外部のローカル変数にはアクセスできません。変数を渡す場合は必ず引数を使用する必要があります。
- **Minifier（圧縮ツール）対策**: コード圧縮時に変数名が変更されても、引数として明示的に渡す設計にすることでエラーを防げます。
- **推奨**: アーキテクチャ上の観点やエラー防止のため、可能な限り通常の関数宣言を使用することが推奨されます。