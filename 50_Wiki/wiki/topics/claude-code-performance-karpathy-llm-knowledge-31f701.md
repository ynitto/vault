---
title: "Karpathy 氏が言語化した「LLM Knowledge Base」というパターン"
type: "topic"
tags:
  - "claude-code"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Karpathy 氏が言語化した「LLM Knowledge Base」というパターン.md"
summary: "Andrej Karpathy氏が提唱した「LLM Knowledge Base」という概念を紹介し、生のドキュメントをLLMに構造化・コンパイルさせるこ…"
---

# Karpathy 氏が言語化した「LLM Knowledge Base」というパターン

## 概要

Andrej Karpathy氏が提唱した「LLM Knowledge Base」という概念を紹介し、生のドキュメントをLLMに構造化・コンパイルさせることで、永続的なナレッジベースを構築する手法と自身の運用事例を解説しています。

*発行: 2026-04-05 / [[claude-code-performance-karpathy-llm-knowledge-31f701]]*

## 主要なトピック

- [[claude-code]]
- [[performance]]

## 詳細

- Andrej Karpathy氏が提唱した「LLM Knowledge Base」という概念を紹介し、生のドキュメントをLLMに構造化・コンパイルさせることで、永続的なナレッジベースを構築する手法と自身の運用事例を解説しています。
- LLM Knowledge Baseの重要ポイント
- **コンセプト**: 生データ（Raw sources）をLLMが読み込み、規約（Schema）に基づいて整理・構造化されたWikiを生成・永続化する。
- **RAGとの違い**:
- **RAG**: 質問ごとに断片を検索（一時的）。
- **LLM Knowledge Base**: 知識を事前に整理し蓄積（永続的）。回答をWikiへフィードバックし、知識を複利的に成長させる。
- **3つの操作**:
- **Ingest**: ソースを統合・整理。
- **Query**: 質問し、回答をWikiに還元。

*発行: 2026-04-05 / [[claude-code-performance-karpathy-llm-knowledge-31f701]]*

## 関連テーマ

- [[claude-code]]
- [[performance]]

## 出典

- `../60_Resources/Karpathy 氏が言語化した「LLM Knowledge Base」というパターン.md`
- https://dev.classmethod.jp/articles/karpathy-llm-knowledge-base/
