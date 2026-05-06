---
title: "qmd"
type: product
tags: [qmd, search, markdown, mcp, local-search]
created: 2026-05-06
updated: 2026-05-06
sources:
  - ".wiki/atoms/wiki/atomswiki/atoms/wiki/atomswiki/atoms/../60_Resources/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで｜Seiji Takahashi@ベースマキナ.md"
  - "../60_Resources/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで｜Seiji Takahashi@ベースマキナ.md"
  - "../60_Resources/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで.md"
summary: "ローカル Markdown を BM25・ベクトル検索・LLM 再ランキングで横断検索し、MCP 経由で Claude Code などから使える検索基盤。"
---

# qmd

## 概要

`qmd` はローカル Markdown を検索対象にする CLI / MCP ツールで、BM25・ベクトル検索・LLM 再ランキングを組み合わせたハイブリッド検索を提供する。

*発行: 2026-01-31*

## 詳細

- ローカル完結で動作し、Markdown 群を SQLite ベースで保持できる
- `full-text` / `semantic` / `hybrid` を切り替えられ、Claude Code からも MCP 経由で参照可能
- 第二の脳や LLM Wiki のようなローカル知識ベースに対し、検索精度の底上げ手段として使いやすい

## 関連

- [[mcp]]
- [[obsidian]]
- [[claude-code]]

## 出典

- `.wiki/atoms/wiki/atomswiki/atoms/wiki/atomswiki/atoms/../60_Resources/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで｜Seiji Takahashi@ベースマキナ.md`（Note, 2026-01-31）
- `../60_Resources/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで｜Seiji Takahashi@ベースマキナ.md`
- `../60_Resources/qmdで始めるローカルAI検索 — ハイブリッド検索の仕組みからClaude Code連携まで.md`
