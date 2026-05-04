---
title: "Node.js で https をサポートする http proxy サーバを 80行で書いた"
type: "topic"
tags:
  - "networking"
  - "node-js"
  - "lightspeedc"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Node.js で https をサポートする http proxy サーバを 80行で書いた.md"
summary: "Node.jsを用いて、HTTPS通信をサポートする簡易的なHTTPプロキシサーバーを約80行のコードで実装する方法を解説した技術記事です。"
---

# Node.js で https をサポートする http proxy サーバを 80行で書いた

## 概要

Node.jsを用いて、HTTPS通信をサポートする簡易的なHTTPプロキシサーバーを約80行のコードで実装する方法を解説した技術記事です。

*発行: 2013-09-02 / [[networking-node-js-node-js-https-http-a88720]]*

## 主要なトピック

- [[networking]]
- [[node-js]]
- [[lightspeedc]]

## 詳細

- Node.jsを用いて、HTTPS通信をサポートする簡易的なHTTPプロキシサーバーを約80行のコードで実装する方法を解説した技術記事です。
- 要点
- **HTTPSサポート**: HTTP/1.1のCONNECTメソッドを実装することで、HTTPSサイトへのアクセスを実現。
- **最小構成**: 外部ライブラリに依存せず、Node.jsの標準モジュールのみで構成。
- **機能と特徴**:
- 上位プロキシサーバーの指定が可能（多段構成対応）。
- ストリーム処理（pipe）を活用し、効率的な通信を実現。
- セキュリティ面では必要最小限の機能に留めており、運用の際は注意が必要。
- **拡張性**: 接続制御（ホワイトリスト）、接続監視、広告ブロック、ステルスモードなどのカスタマイズ例を紹介。

*発行: 2013-09-02 / [[networking-node-js-node-js-https-http-a88720]]*

## 関連テーマ

- [[networking]]
- [[node-js]]
- [[lightspeedc]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Node.js で https をサポートする http proxy サーバを 80行で書いた.md`
- https://qiita.com/LightSpeedC/items/5c1edc2c974206c743f4
