---
title: "【革命】AIが6時間自律コーディング！Anthropicの3エージェントHarnessが「放置開発」を実現した"
type: "topic"
tags:
  - "ai-agent"
  - "emi-ndk"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/【革命】AIが6時間自律コーディング！Anthropicの3エージェントHarnessが「放置開発」を実現した.md"
summary: "Anthropicが提案した「3-Agent Harness」アーキテクチャは、Planner・Generator・Evaluatorの3つのエージェント…"
---

# 【革命】AIが6時間自律コーディング！Anthropicの3エージェントHarnessが「放置開発」を実現した

## 概要

Anthropicが提案した「3-Agent Harness」アーキテクチャは、Planner・Generator・Evaluatorの3つのエージェントを役割分担させることで、長時間にわたる高度な自律コーディングを実現する手法です。これにより、単一エージェントで発生しがちなコンテキスト崩壊や自己評価の甘さを克服し、実用レベルのプロダクト開発を可能にしました。

*発行: 2026-04-22 / [[ai-agent-emi-ndk-ai-6-anthropic-e5b38d]]*

## 主要なトピック

- [[ai-agent]]
- [[emi-ndk]]

## 詳細

- Anthropicが提案した「3-Agent Harness」アーキテクチャは、Planner・Generator・Evaluatorの3つのエージェントを役割分担させることで、長時間にわたる高度な自律コーディングを実現する手法です。これにより、単一エージェントで発生しがちなコンテキスト崩壊や自己評価の甘さを克服し、実用レベルのプロダクト開発を可能にしました。
- 主要なポイント
- **エージェントの役割分担**
- **Planner**: 曖昧な指示を詳細仕様書に展開。
- **Generator**: スプリント単位でコードを実装・管理。
- **Evaluator**: Playwright等で実際に動作テストを行い、客観的に品質を評価。
- **なぜ分割が効くのか**
- 「自己評価バイアス」を排除し、明確な契約（成功基準）に基づいた開発が可能。
- 手戻りの抑制と品質維持を実現。

*発行: 2026-04-22 / [[ai-agent-emi-ndk-ai-6-anthropic-e5b38d]]*

## 関連テーマ

- [[ai-agent]]
- [[emi-ndk]]

## 出典

- `../60_Resources/【革命】AIが6時間自律コーディング！Anthropicの3エージェントHarnessが「放置開発」を実現した.md`
- https://qiita.com/emi_ndk/items/facb4cecfd145f6d6c1a
