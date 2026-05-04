---
title: "Parse a JavaScript string function definition and return a function object. Does not use eval."
source: "https://gist.github.com/lamberta/3768814"
author:
published:
created: 2026-05-01
description: "Parse a JavaScript string function definition and return a function object. Does not use eval. - parseFunction.js"
tags:
  - "clippings"
---
### 概要
GitHub Gistに投稿された、文字列として定義されたJavaScript関数を`eval`を使用せずに再構成し、実行可能な関数オブジェクトに変換するユーティリティコードです。

### 主要なポイント
*   **機能**: 関数定義の文字列から関数名、引数、本体を抽出し、`Function`コンストラクタを用いて新しい関数を生成します。
*   **仕組み**: 
    *   関数文字列の`{}`や`()`の位置から要素を分解。
    *   `Function.apply`を使用してスコープと引数を引き継ぎます。
*   **利点**: 
    *   `eval`を回避することで、セキュリティリスクやデバッグの難しさを軽減します。
*   **制限と課題**:
    *   **ES6対応**: デストラクチャリング（分割代入）引数などには対応していません。
    *   **Async対応**: 標準の実装では非同期関数(`async`)に対応していないため、コメント欄にて`AsyncFunction`を用いた拡張案が提案されています。
*   **活用事例**: 動的なコード解析や、シリアライズされた関数定義の復元ツールとして利用されています。