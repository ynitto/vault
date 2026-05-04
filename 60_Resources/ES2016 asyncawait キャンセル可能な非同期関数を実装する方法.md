---
title: "ES2016 async/await キャンセル可能な非同期関数を実装する方法"
source: "https://qiita.com/sukobuto/items/298de3f97c0862aa8c3c"
author:
published: 2016-11-14
created: 2026-05-01
description: "stack overflow にいいやり方が載っていたので紹介します。 出典：Abort ecmascript7 async function デモを書いてみました まずはこちらを見てください。何がやりたいかがわかりやすくなっているかと思います。 jsfiddle で動..."
tags:
  - "clippings"
---
### 概要
ES2016（当時のES7）の `async/await` に標準で存在しない「非同期処理のキャンセル」を、.NET Frameworkの `CancellationToken` パターンを応用して実装する方法の解説。

### 要点
- **実装の仕組み**
    - `CancellationToken` クラスを作成し、`Promise` を用いてキャンセル要求を伝播させる。
    - 非同期関数側でトークンを引数として受け取り、キャンセルが通知された際に処理を中断（reject）する。
- **主なメリット**
    - 既存の `async/await` の構文を変えることなく、標準的なエラーハンドリング（`try/catch`）でキャンセル処理を制御できる。
- **実装のポイント**
    - `register` メソッドでキャンセル時のコールバックを登録する。
    - `createDependentToken` で親トークンに依存した子トークンを作成し、キャンセルを連動させることが可能。
