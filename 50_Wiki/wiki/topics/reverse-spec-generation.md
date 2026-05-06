---
title: "Reverse spec generation"
type: topic
tags:
  - "ai-agent"
  - "claude-code"
  - "specification"
  - "legacy"
  - "resource-ingest"
created: "2026-05-06"
updated: "2026-05-06"
sources:
  - "60_Resources/既存コードから仕様書を逆生成するClaude Codeスキル cc-rsg を作ってみた.md"
  - "60_Resources/sandecoreversa Transform legacy systems into executable specifications for AI coding agents.md"
  - "60_Resources/sandecoreversa Transform legacy systems into executable specifications for AI coding agents 1.md"
summary: "既存コードやレガシーシステムから、AI が安全に扱える仕様書・実行可能仕様を逆生成するアプローチ。"
---

# Reverse spec generation

## 概要

既存コードやレガシーシステムから、AI エージェントが安全に利用できる仕様書を逆生成するアプローチ。推測で埋めず、トレーサビリティと未確定事項の可視化を重視する点が特徴。

## 主要なトピック

- [[claude-code]]
- [[code-review]]
- [[testing]]

## 詳細

- `cc-rsg` は、行番号参照・インベントリ抽出・Question Bank・機械的カバレッジ検証を組み合わせ、LLM の「もっともらしいフィクション」を抑制する
- `reversa` は、レガシーシステムから C4 図・ERD・OpenAPI などの実行可能仕様を抽出し、信頼度を緑/黄/赤で管理する
- どちらも「分からないことを分からないまま保持する」設計が安全性の鍵になっている

## 関連テーマ

- [[claude-code]]
- [[testing]]
- [[code-review]]

## 出典

- `60_Resources/既存コードから仕様書を逆生成するClaude Codeスキル cc-rsg を作ってみた.md`
- `60_Resources/sandecoreversa Transform legacy systems into executable specifications for AI coding agents.md`
- `60_Resources/sandecoreversa Transform legacy systems into executable specifications for AI coding agents 1.md`
