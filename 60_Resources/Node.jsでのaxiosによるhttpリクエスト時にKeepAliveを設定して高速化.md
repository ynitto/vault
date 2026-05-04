---
title: "Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化"
source: "https://qiita.com/omukaik/items/caef4953c2580fdee5ee"
author:
  - "[[omukaik]]"
published: 2023-03-29
created: 2026-05-01
description: "概要 Node.jsでaxiosでのhttpリクエスト時にKeelAliveを設定することで処理時間がどの程度短縮できるか試した際のメモ Node.js 19.0.0以前はKeepAliveはデフォルトで無効、19.0.0以降であればデフォルトで有効となっているらしい..."
tags:
  - "clippings"
---
### 要約
Node.js環境において、`axios`を用いたHTTPリクエスト時に`keepAlive`を設定することで、TCPコネクションを再利用し、2回目以降のリクエスト処理時間を大幅に短縮できることを解説した記事です。

### 要点
- **KeepAliveの効果**
    - 有効化によりTCPコネクションの確立・破棄を繰り返さなくなるため、リクエストのパフォーマンスが向上する。
- **実装方法**
    - `http.Agent`および`https.Agent`のインスタンスを作成し、`keepAlive: true`を設定して`axios`の`config`に渡す。
- **Node.jsのバージョンによる違い**
    - **Node.js 19.0.0以前**: デフォルト無効のため、明示的な設定が必要。
    - **Node.js 19.0.0以降**: デフォルトで有効化されており、設定なしでもコネクション再利用が適用される。
