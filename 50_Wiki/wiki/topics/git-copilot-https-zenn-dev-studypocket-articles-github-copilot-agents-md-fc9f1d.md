---
title: "GitHub Copilot カスタムエージェント作成のベストプラクティス"
type: "topic"
tags:
  - "git"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/GitHub Copilot カスタムエージェント作成のベストプラクティス.md"
summary: "GitHub Copilot カスタムエージェント作成のベストプラクティス"
---

# GitHub Copilot カスタムエージェント作成のベストプラクティス

## 概要

GitHub Copilot カスタムエージェント作成のベストプラクティス

*発行: 2025-11-27 / [[git-copilot-https-zenn-dev-studypocket-articles-github-copilot-agents-md-fc9f1d]]*

## 主要なトピック

- [[git]]

## 詳細

- GitHub Copilot のカスタムエージェントを活用することで、プロジェクトに特化した専門性の高い開発支援チームを構築可能です。
- 1. エージェントの定義（.agent.md）
- **配置場所**: `../.github/agents/` 配下に `*.agent.md` ファイルとして配置。
- **役割**: ペルソナ、ツール、プロジェクト構造、コードスタイル、禁止事項を定義。
- **注意点**: 30,000バイトの文字数制限があるため、内容を厳選する。
- 2. 効果的なエージェントに必要な6つの要素
- **コマンド**: 実行すべきテストやビルドのコマンドを具体的に明記。
- **テスト**: 使用するフレームワークと実行方法を記述。
- **プロジェクト構造**: 各ディレクトリの役割を定義。

*発行: 2025-11-27 / [[git-copilot-https-zenn-dev-studypocket-articles-github-copilot-agents-md-fc9f1d]]*

## 関連テーマ

- [[git]]

## 出典

- `../60_Resources/GitHub Copilot カスタムエージェント作成のベストプラクティス.md`
- https://zenn.dev/studypocket/articles/github-copilot-agents-md-best-practices
