---
title: "t_wadaさんと「単体テストの使い方/考え方」の疑問点についてディスカッションしました"
type: "topic"
tags:
  - "testing"
  - "observability"
  - "swet-blog"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/t_wadaさんと「単体テストの使い方考え方」の疑問点についてディスカッションしました.md"
summary: "SWETグループが書籍『単体テストの使い方/考え方』の輪読会で生じた疑問に対し、t_wada氏を招いて行ったディスカッションの記録です。テスト戦略、設計、…"
---

# t_wadaさんと「単体テストの使い方/考え方」の疑問点についてディスカッションしました

## 概要

SWETグループが書籍『単体テストの使い方/考え方』の輪読会で生じた疑問に対し、t_wada氏を招いて行ったディスカッションの記録です。テスト戦略、設計、テストダブルの使い所など、現場の実践的な観点から深い議論が交わされました。

*発行: 2023-11-13 / [[testing-observability-t-wada-https-b7c007]]*

## 主要なトピック

- [[testing]]
- [[observability]]
- [[swet-blog]]

## 詳細

- SWETグループが書籍『単体テストの使い方/考え方』の輪読会で生じた疑問に対し、t_wada氏を招いて行ったディスカッションの記録です。テスト戦略、設計、テストダブルの使い所など、現場の実践的な観点から深い議論が交わされました。
- 主なトピックと要点
- 1. 「退行に対する保護」とテストのあり方
- **バグ検出の仕組み**: 実装とテストで「クロスチェック」する構造が、退行に対する保護の度合いを高める。
- **アサーションの使い分け**: 偽陰性と偽陽性のトレードオフを意識し、ユニットテスト（ピンポイント）と上位レイヤーのテスト（全体確認）を使い分ける。
- 2. リファクタリングへの耐性と偽陽性
- **課題**: 偽陽性は「Fragile Test（書き方の問題）」と「Flaky Test（安定性の問題）」に大別され、後者が実務上の大きな課題。
- **注意点**: 本書の推奨事項も「鵜呑みにせず、現場で検証すること」が重要。
- 3. テストサイズとスコープ

*発行: 2023-11-13 / [[testing-observability-t-wada-https-b7c007]]*

## 関連テーマ

- [[testing]]
- [[observability]]
- [[swet-blog]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/t_wadaさんと「単体テストの使い方考え方」の疑問点についてディスカッションしました.md`
- https://swet.dena.com/entry/2023/11/13/170000
