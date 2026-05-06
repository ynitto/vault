---
title: "Harness Engineering"
type: topic
tags:
  - "ai-agent"
  - "harness"
  - "reliability"
  - "observability"
  - "resource-ingest"
created: "2026-05-06"
updated: "2026-05-06"
sources:
  - ".50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた.md"
  - "60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた.md"
  - "60_Resources/aws-samplessample-long-running-app-harness.md"
summary: "AI エージェントを長時間・無人で安定稼働させるための、状態管理・障害回復・排他制御・可観測性を含む運用設計。"
---

# Harness Engineering

## 概要

Harness Engineering は、AI エージェントを実戦投入するための周辺基盤を指す。モデル単体ではなく、状態管理・障害回復・承認フロー・観測性まで含めて設計する点が重要。

## 主要なトピック

- [[ai-agent]]
- [[observability]]
- [[mcp]]
- [[aws]]

## 詳細

- 長時間実行エージェントでは、WIP の保存、セッション継続、ヘルスチェック、排他制御が品質を左右する
- 実装例として `aws-samples/sample-long-running-app-harness` は、Issue 承認 → 自動実装 → テスト → CloudFront プレビューまでを一続きのハーネスとして構成している
- 特定ツールの使い方より、「壊れにくい自律運用パターン」を抽象化して理解する方が再利用しやすい

## 関連テーマ

- [[ai-agent]]
- [[observability]]
- [[cloudfront]]
- [[mcp]]

## 出典

- `.50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた.md`
- `60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた.md`
- `60_Resources/aws-samplessample-long-running-app-harness.md`
