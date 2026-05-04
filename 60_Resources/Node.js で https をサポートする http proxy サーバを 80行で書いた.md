---
title: "Node.js で https をサポートする http proxy サーバを 80行で書いた"
source: "https://qiita.com/LightSpeedC/items/5c1edc2c974206c743f4"
author:
  - "[[LightSpeedC]]"
published: 2013-09-02
created: 2026-05-01
description: "新しく普通に使える http proxyサーバ を書いた。 https をサポートする http proxy サーバ 前回、Qiitaに投稿した記事「Node.jsによる必要最小限のhttpサーバとhttpsサーバとhttp proxyサーバ」では、 http proxy..."
tags:
  - "clippings"
---
### 概要
Node.jsを用いて、HTTPS通信をサポートする簡易的なHTTPプロキシサーバーを約80行のコードで実装する方法を解説した技術記事です。

### 要点
- **HTTPSサポート**: HTTP/1.1のCONNECTメソッドを実装することで、HTTPSサイトへのアクセスを実現。
- **最小構成**: 外部ライブラリに依存せず、Node.jsの標準モジュールのみで構成。
- **機能と特徴**:
  - 上位プロキシサーバーの指定が可能（多段構成対応）。
  - ストリーム処理（pipe）を活用し、効率的な通信を実現。
  - セキュリティ面では必要最小限の機能に留めており、運用の際は注意が必要。
- **拡張性**: 接続制御（ホワイトリスト）、接続監視、広告ブロック、ステルスモードなどのカスタマイズ例を紹介。
- **技術的知見**: Node.jsにおけるストリーム制御やクロージャの活用、エラー処理の重要性が学べる実践的な内容。