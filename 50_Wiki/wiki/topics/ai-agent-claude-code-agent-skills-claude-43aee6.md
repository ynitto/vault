---
title: "Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた"
type: "topic"
tags:
  - "ai-agent"
  - "claude-code"
  - "code-review"
  - "security"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../../60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md"
summary: "Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動…"
---

# Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた

## 概要

Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動収集・解説する「CVE 脆弱性情報収集くん」を作成した記録です。

*発行: 2026-03-17 / [[ai-agent-claude-code-agent-skills-claude-43aee6]]*

## 主要なトピック

- [[ai-agent]]
- [[claude-code]]
- [[code-review]]
- [[security]]

## 詳細

- Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動収集・解説する「CVE 脆弱性情報収集くん」を作成した記録です。
- 重要なポイント
- **Skills の3層構造（Progressive Disclosure）**:
- `YAML frontmatter`: 常時ロードされるトリガ情報
- `SKILL.md`: 詳細な指示書
- `references/`: 補足資料やリファレンス
- **設計のベストプラクティス**:
- 命名規則: `kebab-case`（例: `cve-report`）を厳守。
- 推奨される記述: `description` は Claude が迷わないよう、実行トリガーを「強めに」書く。

*発行: 2026-03-17 / [[ai-agent-claude-code-agent-skills-claude-43aee6]]*

## 関連テーマ

- [[ai-agent]]
- [[claude-code]]
- [[code-review]]
- [[security]]

## 出典

- `../../60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md`
- https://dev.classmethod.jp/articles/claude-code-skills-cve-report/
