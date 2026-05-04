---
title: "Node.js でメモリ肥大化の原因を特定してみた"
source: "https://zenn.dev/ubie_dev/articles/f64561d59918d1"
author:
published: 2023-12-07
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 内容要約
Node.js環境下で`langchain`ライブラリを使用中に発生したメモリ肥大化問題について、デバッグ手法から原因特定、解決に至るまでのプロセスを解説した技術記事です。

### 要点まとめ
- **現象**: Podのメモリ制限(500MB)により、JavaScriptのヒープ領域が枯渇しクラッシュが発生。
- **原因**: `langchain`内の`getEncoding`関数が呼ばれるたびに、約50MBの`Tiktoken`オブジェクトが新規生成され続けていた。
- **分析手法**:
    - `process.memoryUsage()`によるヒープ状況の確認。
    - VSCodeのデバッガーと「Heap Profile」を使用して、メモリを大量消費している関数を特定。
- **解決策**: JSONベースで毎回生成していたキャッシュ戦略を見直し、`Tiktoken`オブジェクト自体をキャッシュするように修正してプルリクエストを送付・マージ。
