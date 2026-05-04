---
title: "Node.jsでコマンドライン引数を取得する"
source: "https://qiita.com/furusin_oriver/items/f030d1eaa9e7b54233c3"
author:
  - "[[furusin_oriver]]"
published: 2016-09-02
created: 2026-05-01
description: "実装段階で値を変えながら試したい場合に、毎回忘れてしまうのでメモしておく。 コマンドライン引数を渡す 通常通り、引数を渡します。 terminal $ node test.js aaa bbb ccc ddd eee コマンドライン引数を受け取る 取得するインデ..."
tags:
  - "clippings"
---
### 記事の要約
Node.js環境において、コマンドラインから引数を受け取って実行する方法を解説しています。

### 要点
- **実行方法**
  - `$ node [ファイル名] [引数1] [引数2] ...` の形式で実行します。
- **引数の取得方法**
  - `process.argv` 配列を使用して取得します。
- **インデックスのルール**
  - `process.argv[0]`: 実行コマンド（node）
  - `process.argv[1]`: 実行ファイルパス
  - `process.argv[2]以降`: コマンドラインで渡された引数
- **実装例**
  - `process.argv.length` でループを回すことで、すべての引数を順次取得・表示可能です。