---
title: qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで｜Seiji Takahashi@ベースマキナ
source: https://note.com/timakin/n/nbaa645e013c5
author:
- '[[Seiji Takahashi@ベースマキナ]]'
published: 2026-01-31
created: 2026-05-05
description: 皆さまこんにちは、株式会社ベースマキナの代表取締役社長を務めております高橋（@__timakin__）です。  最近、ローカルのMarkdownファイルを検索するツール「qmd」が話題になっています。作者はShopify
  CEOのTobi Lütke。「毎日使っている。昨年末に作ったシンプルなツール」とXでコメントしていて、GitHub Starsも2.5kを超えています。      何が注目されているかというと、BM25・ベクトル検索・LLM再ランキングを組み合わせたハイブリッド検索と、MCP（Model
  Context Protocol）対応でClaude CodeやClaude
tags:
- clippings
- resource/web
- 2026-05
- claude-code
- ai-agent
- qmd
- local-search
- search
original_source: 00_Inbox/Clippings/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで｜Seiji
  Takahashi@ベースマキナ.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 要約
Shopify CEOのTobi Lütke氏が開発したローカルMarkdown検索ツール「qmd」の紹介記事。BM25、ベクトル検索、LLM再ランキングを統合した「ハイブリッド検索」と、MCP（Model Context Protocol）によるClaude Code等との連携機能が特徴です。

### 主な要点
- **qmdの技術的特徴**
  - **検索モード**: 全文検索（BM25）、セマンティック検索（vsearch）、最高品質のハイブリッド検索（query）の3種。
  - **ハイブリッド検索**: クエリ拡張 → 並列検索 → RRF（結果融合） → LLM再ランキングのパイプラインで精度を最大化。
  - **ストレージ**: SQLiteを採用。ポータブルでバックアップも容易。
  - **必要なリソース**: 3つのモデルを使用し、合計約3GBのデータをダウンロード。

- **Claude Codeとの連携**
  - MCPサーバーとして動作するため、Claude DesktopやCursor等からローカルMarkdownを直接検索・参照可能。
  - 会議記録の検索や、ドキュメントを参照したコード生成に最適。

- **導入のメリット・制約**
  - **メリット**: オフライン・ローカル完結でプライバシーに配慮しつつ、高度な関連性検索が可能。
  - **制約**: Markdownファイル専用、CLIツール、初回モデルダウンロードの手間が必要。
