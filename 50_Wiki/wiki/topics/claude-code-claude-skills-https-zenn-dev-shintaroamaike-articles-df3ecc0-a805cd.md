---
title: "Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する"
type: "topic"
tags:
  - "claude-code"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する.md"
summary: "Claude Codeのコーディングルール管理を自動化するスキル「AutoHarness」の紹介記事です。プロジェクト固有の規約を自動生成・適用することで…"
---

# Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する

## 概要

Claude Codeのコーディングルール管理を自動化するスキル「AutoHarness」の紹介記事です。プロジェクト固有の規約を自動生成・適用することで、AIによるコード品質の継続的な改善を実現します。

*発行: 2026-04-01 / [[claude-code-claude-skills-https-zenn-dev-shintaroamaike-articles-df3ecc0-a805cd]]*

## 主要なトピック

- [[claude-code]]

## 詳細

- Claude Codeのコーディングルール管理を自動化するスキル「AutoHarness」の紹介記事です。プロジェクト固有の規約を自動生成・適用することで、AIによるコード品質の継続的な改善を実現します。
- 要点
- **AutoHarnessとは**
- DeepMindの論文の着想を得た、プロジェクト固有のルール（型定義、命名規則、禁止パターン）を管理するフレームワーク。
- 開発現場の「暗黙知」を文章化し、Claude Codeへ適切に指示するコストを削減します。
- **主な機能**
- `/autoharness-init`: プロジェクトを解析し、ルールファイル（`.claude/rules/harness.md`）と検証スクリプトを自動生成。
- `/autoharness-update`: コード生成後のフィードバックやエラーに基づき、ルールを自律的に改善。
- **メリット**

*発行: 2026-04-01 / [[claude-code-claude-skills-https-zenn-dev-shintaroamaike-articles-df3ecc0-a805cd]]*

## 関連テーマ

- [[claude-code]]

## 出典

- `../60_Resources/Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する.md`
- https://zenn.dev/shintaroamaike/articles/df3ecc0ddee047
