---
title: "Archive and streaming utilities"
type: topic
tags:
  - "node-js"
  - "stream"
  - "archive"
  - "resource-ingest"
created: "2026-05-06"
updated: "2026-05-06"
sources:
  - "../60_Resources/archiverjsnode-archiver a streaming interface for archive generation.md"
  - "../60_Resources/samcdaynode-stream-buffer Readable and Writable Streams that use backing Buffers..md"
summary: "Node.js でアーカイブ生成やバッファ背後の Stream を扱う実用ライブラリ。"
---

# Archive and streaming utilities

## 概要

Node.js で ZIP/TAR などのアーカイブ生成や、検証向けのバッファベース Stream を扱うためのユーティリティ群。

## 主要なトピック

- [[node-js]]

## 詳細

- `archiver` は Stream API ベースで ZIP / TAR を生成し、ファイル・ディレクトリ・glob から柔軟にアーカイブを組み立てられる
- `node-stream-buffer` は Readable / Writable の両方をバッファ背後で提供し、テストや特殊な I/O 検証に向く

## 関連テーマ

- [[node-js]]

## 出典

- `../60_Resources/archiverjsnode-archiver a streaming interface for archive generation.md`
- `../60_Resources/samcdaynode-stream-buffer Readable and Writable Streams that use backing Buffers..md`
