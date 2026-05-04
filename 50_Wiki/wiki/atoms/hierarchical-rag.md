---
title: "階層型RAG"
type: concept
tags: [rag, llm, knowledge-management, hierarchical]
created: 2026-05-04
updated: 2026-05-04
sources:
  - "ベクトルDBを使わないRAG。全てのナレッジを階層化する手法"
summary: "文書を階層ツリーに整理してLLMが探索するRAGアーキテクチャパターン。Corpus2Skillが代表実装。"
---

# 階層型RAG

## 概要

文書群を階層的なツリー構造に整理し、LLMエージェントが目次を辿るように情報を探索するRAGアーキテクチャパターン。ベクトル検索の網羅性の欠如を補う。

*発行: 2026-04-28 / [[ベクトルDBを使わないRAG。全てのナレッジを階層化する手法]]*

## 詳細

従来のベクトルRAGは類似度検索で断片的な情報を取得するが、階層型RAGは文書全体の構造を保持することで情報の網羅性を確保する。

**特徴**:
- 探索効率: O(log N)（文書数に対して対数時間）
- ベクトルDBが不要
- エンタープライズ環境での精度向上に有効

## 関連

- [[corpus2skill]]

## 出典

- [ベクトルDBを使わないRAG。全てのナレッジを階層化する手法](https://zenn.dev/knowledgesense/articles/7dddae04a7d828)
