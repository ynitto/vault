---
title: "Harness as Code — CoDD活用ガイド #2 コード → 設計書　「神頼みデプロイ」と「深夜障害連絡電話」からの解放"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Harness as Code — CoDD活用ガイド 2 コード → 設計書　「神頼みデプロイ」と「深夜障害連絡電話」からの解放.md"
summary: "既存の設計書が存在しないレガシーコード（ブラウンフィールド）に対し、AIを活用して自動で設計書を復元する手法「CoDD（Coherence-Driven…"
---

# Harness as Code — CoDD活用ガイド #2 コード → 設計書　「神頼みデプロイ」と「深夜障害連絡電話」からの解放

## 概要

既存の設計書が存在しないレガシーコード（ブラウンフィールド）に対し、AIを活用して自動で設計書を復元する手法「CoDD（Coherence-Driven Development）」の有効性を検証した記事です。AIにコードベースのみを渡し、6層の構造で設計書を生成させた結果、F1スコア全層0.953以上という極めて高い精度で復元に成功しました。

*発行: 2026-04-05 / [[harness-as-codd-2-https-edbd15]]*

## 主要なトピック


## 詳細

- 既存の設計書が存在しないレガシーコード（ブラウンフィールド）に対し、AIを活用して自動で設計書を復元する手法「CoDD（Coherence-Driven Development）」の有効性を検証した記事です。AIにコードベースのみを渡し、6層の構造で設計書を生成させた結果、F1スコア全層0.953以上という極めて高い精度で復元に成功しました。
- 要点まとめ
- **AIによる設計書の高精度復元**
- AIにコードを読み込ませるだけで、既存設計書と照合しF1スコア0.953以上で復元。
- 実在しない項目（ハルシネーション）は0件であった。
- **「ドキュメントの健康診断」機能としての側面**
- AIは設計書に記載のない実在の項目を146件発見。
- 過去のドキュメントの書き漏れをAIが修正・補完する「AIによるAIの尻拭い」が実現した。
- **自律的な適応力**

*発行: 2026-04-05 / [[harness-as-codd-2-https-edbd15]]*

## 関連テーマ


## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Harness as Code — CoDD活用ガイド 2 コード → 設計書　「神頼みデプロイ」と「深夜障害連絡電話」からの解放.md`
- https://zenn.dev/shio_shoppaize/articles/shogun-codd-brownfield
