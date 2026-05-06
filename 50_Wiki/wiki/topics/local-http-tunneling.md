---
title: "Local HTTP tunneling"
type: topic
tags:
  - "networking"
  - "node-js"
  - "tunnel"
  - "resource-ingest"
created: "2026-05-06"
updated: "2026-05-06"
sources:
  - "../60_Resources/web-tunnellite-http-tunnel-client.md"
summary: "ローカルで動く HTTP サーバを外部公開するための軽量トンネルクライアント。"
---

# Local HTTP tunneling

## 概要

開発中のローカル HTTP サーバを、トンネルサーバ経由で外部公開するための仕組み。Webhook 検証や一時的なデモ公開などに向く。

## 主要なトピック

- [[networking]]
- [[node-js]]

## 詳細

- `lite-http-tunnel-client` は Node.js ベースの軽量トンネルクライアントで、サーバ設定・認証設定・ポート公開を CLI で行える
- 開発環境をそのまま外部へ見せたいときの簡易公開手段として使いやすい

## 関連テーマ

- [[networking]]
- [[node-js]]

## 出典

- `../60_Resources/web-tunnellite-http-tunnel-client.md`
