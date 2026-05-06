---
title: "Corpus2Skill"
type: concept
tags: [rag, llm, knowledge-management, hierarchical, agent]
created: 2026-05-04
updated: 2026-05-06
sources:
  - "../60_Resources/ベクトルDBを使わないRAG。全てのナレッジを階層化する手法.md"
summary: "ベクトルDBを使わず文書を階層ツリーに整理し、LLMエージェントがナビゲートするRAG手法。"
---

# Corpus2Skill

## 概要

ベクトルデータベースを使用せず、全文書をクラスタリング・要約して階層型ディレクトリ構造（ツリー）を構築し、LLMエージェントが目次を辿るように情報へアクセスするRAGの手法。

*発行: 2026-04-28*

## 詳細

従来のベクトル検索は「木を見て森を見ず」の状態になりやすく、網羅的な情報取得が苦手という問題意識から生まれた。

**仕組み**:
- 事前に全文書をクラスタリング・要約し、`SKILL.md` 等として階層構造を出力
- 実行時にエージェントが階層を探索し、適切なドキュメントを選択・取得

**主なメリット**:
- ベクトルDBが不要
- 文書数が増えても探索効率が良い（対数時間 O(log N)）
- 既存のRAGベンチマーク（WixQA）で高い性能を実証

## 関連

- [[hierarchical-rag]]
- [[hierarchical-rag]]
- [[ai-agent]]

## 出典

- `../60_Resources/ベクトルDBを使わないRAG。全てのナレッジを階層化する手法.md`
