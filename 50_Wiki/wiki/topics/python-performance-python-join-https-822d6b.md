---
title: "【Python】文字列連結のパフォーマンス最適化 — joinって本当に速いの？"
type: "topic"
tags:
  - "python"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/【Python】文字列連結のパフォーマンス最適化 — joinって本当に速いの？.md"
summary: "Pythonにおける文字列結合の最適化：`+` vs `join`"
---

# 【Python】文字列連結のパフォーマンス最適化 — joinって本当に速いの？

## 概要

Pythonにおける文字列結合の最適化：`+` vs `join`

*発行: 2025-12-22 / [[python-performance-python-join-https-822d6b]]*

## 主要なトピック

- [[python]]
- [[performance]]

## 詳細

- Pythonの文字列連結において、`+`演算子よりも`\"\".join()`が推奨される理由をCPythonの内部実装とベンチマークに基づき解説した記事です。
- 要点まとめ
- **ベンチマーク結果**: `+`演算子は`join`と比較して約5倍低速である。
- **`+`が遅い理由**:
- 文字列は「不変（immutable）」オブジェクトであるため、結合するたびに新しいメモリ領域を確保し、全内容をコピーする必要がある。
- **`join`が速い理由**:
- 事前に全要素の長さを計算し、必要なバッファを一度だけ確保する。
- その後、各要素をまとめて書き込むため、コピーの効率が極めて高い。
- **使い分けの指針**:

*発行: 2025-12-22 / [[python-performance-python-join-https-822d6b]]*

## 関連テーマ

- [[python]]
- [[performance]]

## 出典

- `60_Resources/【Python】文字列連結のパフォーマンス最適化 — joinって本当に速いの？.md`
- https://zenn.dev/techliberty/articles/18afd8ab79526b
