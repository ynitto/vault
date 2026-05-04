---
title: "5スロットブリーフ"
type: concept
tags: [prompt-engineering, llm, claude, agent-skill]
created: 2026-05-04
updated: 2026-05-04
sources:
  - "モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った"
summary: "LLMへの指示をGoal/Constraints/Acceptance criteria/Context/Validationの5要素に整理する構造化プロンプト形式。"
---

# 5スロットブリーフ

## 概要

LLMへの指示を5つのスロットに整理することで、モデルへ意図を正確に伝達する構造化プロンプト形式。Claude Opus 4.7向けに最適化されている。

*発行: 2026-04-27 / [[モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った]]*

## 詳細

**5つのスロット**:
1. **Goal**: 成功の定義
2. **Constraints**: 制約条件（やってはいけないこと）
3. **Acceptance criteria**: 完了条件
4. **Context**: 文脈や関連情報
5. **Validation**: 自己検証のためのテストやコマンド（最大の品質レバー）

数行の依頼を80行程度の最適化されたブリーフに自動変換するAgent Skill（`claude-prompt-optimizer`）として実装されている。3モード対応: `generate`（生成）、`audit`（監査）、`route`（モデルエスカレーション制御）。

## 関連

- [[claude-opus-4-7]]
- [[front-loading]]
- [[ai-agent]]

## 出典

- [モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った](https://zenn.dev/shinyay/articles/opus-4-7-prompt-design-copilot-skill)
