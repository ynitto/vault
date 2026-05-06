---
title: "Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化"
type: "topic"
tags:
  - "networking"
  - "node-js"
  - "performance"
  - "omukaik"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化.md"
summary: "Node.js環境において、`axios`を用いたHTTPリクエスト時に`keepAlive`を設定することで、TCPコネクションを再利用し、2回目以降の…"
---

# Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化

## 概要

Node.js環境において、`axios`を用いたHTTPリクエスト時に`keepAlive`を設定することで、TCPコネクションを再利用し、2回目以降のリクエスト処理時間を大幅に短縮できることを解説した記事です。

*発行: 2023-03-29 / [[networking-node-js-node-js-axios-http-daa2fa]]*

## 主要なトピック

- [[networking]]
- [[node-js]]
- [[performance]]
- [[omukaik]]

## 詳細

- Node.js環境において、`axios`を用いたHTTPリクエスト時に`keepAlive`を設定することで、TCPコネクションを再利用し、2回目以降のリクエスト処理時間を大幅に短縮できることを解説した記事です。
- 要点
- **KeepAliveの効果**
- 有効化によりTCPコネクションの確立・破棄を繰り返さなくなるため、リクエストのパフォーマンスが向上する。
- **実装方法**
- `http.Agent`および`https.Agent`のインスタンスを作成し、`keepAlive: true`を設定して`axios`の`config`に渡す。
- **Node.jsのバージョンによる違い**
- **Node.js 19.0.0以前**: デフォルト無効のため、明示的な設定が必要。
- **Node.js 19.0.0以降**: デフォルトで有効化されており、設定なしでもコネクション再利用が適用される。

*発行: 2023-03-29 / [[networking-node-js-node-js-axios-http-daa2fa]]*

## 関連テーマ

- [[networking]]
- [[node-js]]
- [[performance]]
- [[omukaik]]

## 出典

- `../60_Resources/Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化.md`
- https://qiita.com/omukaik/items/caef4953c2580fdee5ee
