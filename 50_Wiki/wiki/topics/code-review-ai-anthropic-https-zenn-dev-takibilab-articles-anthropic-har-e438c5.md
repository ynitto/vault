---
title: "AIエージェントのハーネス設計｜Anthropicが公開した「生成と評価の分離」パターンを読み解く"
type: "topic"
tags:
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/AIエージェントのハーネス設計｜Anthropicが公開した「生成と評価の分離」パターンを読み解く.md"
summary: "Anthropicが公開した「Harness design for long-running application development」を基に、AI…"
---

# AIエージェントのハーネス設計｜Anthropicが公開した「生成と評価の分離」パターンを読み解く

## 概要

Anthropicが公開した「Harness design for long-running application development」を基に、AIエージェントに長時間タスクを実行させるための「設計パターン（ハーネス）」を解説しています。AIの自己評価の甘さとコンテキスト劣化という課題に対し、エージェントを役割分担させる手法が紹介されています。

*発行: 2026-03-27 / [[code-review-ai-anthropic-https-zenn-dev-takibilab-articles-anthropic-har-e438c5]]*

## 主要なトピック

- [[code-review]]

## 詳細

- Anthropicが公開した「Harness design for long-running application development」を基に、AIエージェントに長時間タスクを実行させるための「設計パターン（ハーネス）」を解説しています。AIの自己評価の甘さとコンテキスト劣化という課題に対し、エージェントを役割分担させる手法が紹介されています。
- 要点まとめ
- **根本的な問題**
- **コンテキスト不安**: 長時間タスクで作業を途中で切り上げようとする（リセットで解消可能）。
- **自己評価の罠**: 自分で自分の仕事を評価すると甘くなるため、第三者的な評価が必要。
- **推奨される「3エージェント分業」モデル**
- **Planner**: ユーザーの依頼を詳細なプロダクト仕様書に変換する。
- **Generator**: 仕様書に基づき実装・自己テストを行う。
- **Evaluator**: ブラウザ等を用いてユーザー視点で客観的にテスト・採点する。

*発行: 2026-03-27 / [[code-review-ai-anthropic-https-zenn-dev-takibilab-articles-anthropic-har-e438c5]]*

## 関連テーマ

- [[code-review]]

## 出典

- `../60_Resources/AIエージェントのハーネス設計｜Anthropicが公開した「生成と評価の分離」パターンを読み解く.md`
- https://zenn.dev/takibilab/articles/anthropic-harness-design
