---
title: "Claude Opus 4.7"
type: product
tags: [claude, anthropic, llm, model]
created: 2026-05-04
updated: 2026-05-06
sources:
  - "../60_Resources/モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った.md"
summary: "Anthropicのフラッグシップモデル。adaptive thinkingへの一本化とトークナイザー変更により4.6と最適プロンプトが異なる。"
---

# Claude Opus 4.7

## 概要

Anthropicのフラッグシップ大規模言語モデル。adaptive thinkingへの一本化とトークナイザーの変更により、Claude 4.6とは最適な指示の仕方が異なる。

*発行: 2026-04-27*

## 詳細

**プロンプト設計の変化点**:
- ターンごとにコストがかかるため、対話で詰めるのではなく最初のターンに必要な情報をすべて詰め込む「フロントローディング」が最適解
- [[five-slot-brief]]（5スロットブリーフ）という構造化プロンプト形式が有効

**モデルルーティング戦略**:
- タスク難易度に応じてHaiku 4.5 / Sonnet 4.5 → Opus 4.7 へエスカレーション
- コストと品質のバランスを最適化

## 関連

- [[five-slot-brief]]
- [[front-loading]]
- [[ai-agent]]
- [[claude-code]]

## 出典

- `../60_Resources/モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った.md`
