---
title: "Obsidian Web Clipperと生成AIでクリップの自動要約がうまくいかない"
type: "topic"
tags:
  - "obsidian"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Obsidian Web Clipperと生成AIでクリップの自動要約がうまくいかない.md"
summary: "Obsidian Web ClipperでのAI要約問題解決"
---

# Obsidian Web Clipperと生成AIでクリップの自動要約がうまくいかない

## 概要

Obsidian Web ClipperでのAI要約問題解決

*発行: 2025-03-13 / [[obsidian-obsidian-web-clipper-ai-c52245]]*

## 主要なトピック

- [[obsidian]]

## 詳細

- Obsidian Web ClipperでGeminiやGPT-4oがWebページをうまく要約しない、またはコンテキストが渡されない問題の解決策。
- 問題点
- AI要約時にWebページの`content`や`fullHtml`がAIに正しく渡されていない。
- 解決策
- **テンプレート側で「インタープリターコンテキスト」を明示的に設定する。**
- 詳細設定だけでなく、実際に使用するテンプレートのJSON設定にも`\\"context\\": \\"{{fullHtml}}\\"`を含める。
- 要約指示:`\\"noteContentFormat\\": \\"{{\\"内容を要約してください。。\

*発行: 2025-03-13 / [[obsidian-obsidian-web-clipper-ai-c52245]]*

## 関連テーマ

- [[obsidian]]

## 出典

- `../60_Resources/Obsidian Web Clipperと生成AIでクリップの自動要約がうまくいかない.md`
- https://zenn.dev/2rezure/articles/e662f43ad9ea35
