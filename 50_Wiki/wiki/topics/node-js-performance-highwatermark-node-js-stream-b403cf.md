---
title: "highWaterMarkから探るNode.jsのStreamの仕組み"
type: "topic"
tags:
  - "node-js"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/highWaterMarkから探るNode.jsのStreamの仕組み.md"
summary: "Node.jsにおける「Stream」の重要性と、そのパフォーマンスやメモリ消費を最適化する仕組みである「バックプレッシャー」と「highWaterMar…"
---

# highWaterMarkから探るNode.jsのStreamの仕組み

## 概要

Node.jsにおける「Stream」の重要性と、そのパフォーマンスやメモリ消費を最適化する仕組みである「バックプレッシャー」と「highWaterMark」の役割を解説した記事です。

*発行: 2016-12-08 / [[node-js-performance-highwatermark-node-js-stream-b403cf]]*

## 主要なトピック

- [[node-js]]
- [[performance]]

## 詳細

- Node.jsにおける「Stream」の重要性と、そのパフォーマンスやメモリ消費を最適化する仕組みである「バックプレッシャー」と「highWaterMark」の役割を解説した記事です。
- 要点まとめ
- **Streamの重要性**: Node.jsの根幹である非同期I/Oを支える仕組みであり、「Streamを制するものはNode.jsを制す」と言われるほど重要。
- **highWaterMarkの役割**: ストリームの内部バッファの閾値（デフォルト16KB）。この値が性能とメモリ使用量のバランスを決定する。
- **バックプレッシャー（背圧）**: 上流と下流の処理速度差を吸収し、メモリの過度な圧迫を防ぐ仕組み。
- **pipe()の実装**: `pipe()`は`highWaterMark`を監視し、バッファが一杯になると読み込みを一時停止（pause）、余裕ができると再開（resume）することで、効率的なデータ伝送を実現している。
- **調整の影響**: `highWaterMark`が小さすぎるとイベントループの頻度（drain回数）が増加し、パフォーマンスが低下する。

*発行: 2016-12-08 / [[node-js-performance-highwatermark-node-js-stream-b403cf]]*

## 関連テーマ

- [[node-js]]
- [[performance]]

## 出典

- `60_Resources/highWaterMarkから探るNode.jsのStreamの仕組み.md`
- https://techblog.yahoo.co.jp/advent-calendar-2016/node-stream-highwatermark/
