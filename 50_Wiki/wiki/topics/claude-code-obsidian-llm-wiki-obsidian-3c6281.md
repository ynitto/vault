---
title: "【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する"
type: "topic"
tags:
  - "claude-code"
  - "obsidian"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md"
summary: "本記事では、Karpathy氏が提唱する「LLM Wiki」の概念をClaude Codeのスキルとして実装し、Obsidianと連携して運用する方法につ…"
---

# 【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する

## 概要

本記事では、Karpathy氏が提唱する「LLM Wiki」の概念をClaude Codeのスキルとして実装し、Obsidianと連携して運用する方法について解説しています。

*発行: 2026-04-14 / [[claude-code-obsidian-llm-wiki-obsidian-3c6281]]*

## 主要なトピック

- [[claude-code]]
- [[obsidian]]

## 詳細

- 本記事では、Karpathy氏が提唱する「LLM Wiki」の概念をClaude Codeのスキルとして実装し、Obsidianと連携して運用する方法について解説しています。
- LLM Wikiのコンセプト
- **RAGとの違い**: RAGが質問ごとにゼロから知識を検索・合成するのに対し、LLM Wikiは知識を一度「コンパイル」し、永続的に蓄積・整理・育成していくアプローチ。
- **知識のコンパイル**: 生のドキュメントから情報を整理・統合し、相互参照された構造（Wiki）に変換することで、LLMが効率的に知識を利用できるようにする。
- 3層アーキテクチャ
- 1.  **Raw Sources**: ユーザーが集めた不変の生ドキュメント。
- 2.  **Wiki**: LLMが生成・管理するマークダウンファイル（要約、概念、エンティティ、比較、総合考察ページなど）。
- 3.  **Schema**: Wikiの構造と規約を定義するドキュメント。
- 4つの基本操作

*発行: 2026-04-14 / [[claude-code-obsidian-llm-wiki-obsidian-3c6281]]*

## 関連テーマ

- [[claude-code]]
- [[obsidian]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md`
- https://zenn.dev/dely_jp/articles/8b55114cc0b958
