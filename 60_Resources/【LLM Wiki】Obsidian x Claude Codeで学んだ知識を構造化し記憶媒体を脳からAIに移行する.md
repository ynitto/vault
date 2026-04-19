---
title: 【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する
source: https://zenn.dev/dely_jp/articles/8b55114cc0b958
author: null
published: 2026-04-14
created: 2026-04-19
description: null
tags:
- resource/web
- obsidian
- ai-agent
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md
copied_at: 2026-04-19 10:51:13+09:00
---
# LLM Wikiの概要

本記事では、Karpathy氏が提唱する「LLM Wiki」の概念をClaude Codeのスキルとして実装し、Obsidianと連携して運用する方法について解説しています。

## LLM Wikiのコンセプト
*   **RAGとの違い**: RAGが質問ごとにゼロから知識を検索・合成するのに対し、LLM Wikiは知識を一度「コンパイル」し、永続的に蓄積・整理・育成していくアプローチ。
*   **知識のコンパイル**: 生のドキュメントから情報を整理・統合し、相互参照された構造（Wiki）に変換することで、LLMが効率的に知識を利用できるようにする。

## 3層アーキテクチャ
1.  **Raw Sources**: ユーザーが集めた不変の生ドキュメント。
2.  **Wiki**: LLMが生成・管理するマークダウンファイル（要約、概念、エンティティ、比較、総合考察ページなど）。
3.  **Schema**: Wikiの構造と規約を定義するドキュメント。

## 4つの基本操作
1.  **ingest (取り込み)**: 新しいソースを読み込み、Wikiページを作成・更新し、相互参照を確立する。
2.  **query (質問)**: Wiki内の知識を検索・統合して回答を生成する。
3.  **lint (健全性チェック)**: Wikiの矛盾、孤立ページ、不足概念などを定期的に検出・修正する。
4.  **index + log**: Wikiの全体カタログと操作記録を管理し、LLMが知識構造を把握しやすくする。

## 実装と運用
*   **Claude Codeスキルへの落とし込み**: Karpathy氏のGistを`skill-creator`に投入し、対話的にSKILL.mdを生成。
*   **Obsidianとの連携**: ローカルのマークダウンファイルとしてWikiを管理し、[[wikilinks]]によるグラフビューで知識構造を可視化。
*   **Obsidian Web Clipper**: Web記事をマークダウン形式で容易に保存し、ingestのソースとして活用。

## 著者によるアレンジ（3つの設計判断）
LLMの挙動のブレを抑え、実運用に適した形にするためのカスタマイズ。
1.  **2層index/log構造**: 全体indexとジャンル別index/logに分け、コンテキストウィンドウの肥大化を抑制。
2.  **ページの作成・更新・分割の判断基準**: 新規作成、既存更新、分割の明確な基準をSKILL.mdに明文化し、LLMの判断を安定化。
3.  **query結果の保存判断基準**: 回答をWikiに保存すべきか否かの基準を設け、Wikiの品質維持と知識の蓄積を両立。