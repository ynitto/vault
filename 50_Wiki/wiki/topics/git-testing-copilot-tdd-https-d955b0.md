---
title: "GitHub Copilot でサブエージェントからサブエージェントを呼び出して TDD（テスト駆動開発）ワークフローを作成"
type: "topic"
tags:
  - "git"
  - "testing"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/GitHub Copilot でサブエージェントからサブエージェントを呼び出して TDD（テスト駆動開発）ワークフローを作成.md"
summary: "2026年3月にリリースされたVS Code v1.113の新機能「Nested Subagents（サブエージェントの入れ子呼び出し）」を活用し、TDD…"
---

# GitHub Copilot でサブエージェントからサブエージェントを呼び出して TDD（テスト駆動開発）ワークフローを作成

## 概要

2026年3月にリリースされたVS Code v1.113の新機能「Nested Subagents（サブエージェントの入れ子呼び出し）」を活用し、TDD（テスト駆動開発）の自動化ワークフローを構築する手法の解説です。

*発行: 2026-04-03 / [[git-testing-copilot-tdd-https-d955b0]]*

## 主要なトピック

- [[git]]
- [[testing]]

## 詳細

- 2026年3月にリリースされたVS Code v1.113の新機能「Nested Subagents（サブエージェントの入れ子呼び出し）」を活用し、TDD（テスト駆動開発）の自動化ワークフローを構築する手法の解説です。
- 要点
- **Nested Subagentsとは**
- サブエージェントが別のサブエージェントを直接呼び出せる機能。
- 従来は無限再帰防止のため禁止されていたが、設定により可能になった。
- **サブエージェントの主な特徴**
- **コンテキスト分離**: メインの会話履歴を汚さず独立して動作。
- **同期実行**: メインエージェントは結果を待ってから次へ進む。
- **効率性**: 途中経過ではなく結果の要約のみを返すためトークンを節約可能。

*発行: 2026-04-03 / [[git-testing-copilot-tdd-https-d955b0]]*

## 関連テーマ

- [[git]]
- [[testing]]

## 出典

- `60_Resources/GitHub Copilot でサブエージェントからサブエージェントを呼び出して TDD（テスト駆動開発）ワークフローを作成.md`
- https://qiita.com/leomarokun/items/3040cd6ae4c51b2329f6
