---
title: 'samcday/node-stream-buffer: Readable and Writable Streams that use backing
  Buffers.'
source: https://github.com/samcday/node-stream-buffer/tree/main
author: null
published: null
created: 2026-05-05
description: Readable and Writable Streams that use backing Buffers. - samcday/node-stream-buffer
tags:
- clippings
- resource/web
- 2026-05
- node-js
original_source: 00_Inbox/Clippings/samcdaynode-stream-buffer Readable and Writable
  Streams that use backing Buffers..md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 概要
`node-stream-buffer`は、Node.jsの`Buffer`を利用してデータを保持・送受信するためのシンプルな「読み込み可能（Readable）」および「書き込み可能（Writable）」なストリームライブラリです。主にテストやデバッグ、特殊なエッジケースでの利用を想定しています。

### 主要なポイント
- **WritableStreamBuffer**
    - 標準の`stream.Writable`を実装。
    - 書き込まれたデータを内部バッファに蓄積し、必要に応じて自動拡張します。
    - 書き込み完了後に`getContents()`や`getContentsAsString()`で保持データを取り出し可能です。
- **ReadableStreamBuffer**
    - 標準の`stream.Readable`を実装。
    - `put()`メソッドでデータを追加すると、設定した頻度（frequency）とチャンクサイズでデータをストリームへ流し出します。
- **利用上の注意**
    - **Node 16以降を使用している場合は、公式の「Utility Consumers」の利用が推奨されています。**
    - パフォーマンスを優先する設計ではなく、あくまで検証やデバッグ向けです。
- **インストールと導入**
    - `npm install stream-buffers --save` でインストール。
    - `require('stream-buffers')` でインポートして利用します。
