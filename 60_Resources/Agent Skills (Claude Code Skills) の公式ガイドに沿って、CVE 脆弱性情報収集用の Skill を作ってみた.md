---
title: Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた
source: https://dev.classmethod.jp/articles/claude-code-skills-cve-report/
author:
- '[[かわい]]'
published: 2026-03-17
created: 2026-04-19
description: null
tags:
- resource/web
- ai-agent
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE
  脆弱性情報収集用の Skill を作ってみた.md
copied_at: 2026-04-19 10:51:13+09:00
---
## 概要
Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動収集・解説する「CVE 脆弱性情報収集くん」を作成した記録です。

## 重要なポイント
- **Skills の3層構造（Progressive Disclosure）**:
  - `YAML frontmatter`: 常時ロードされるトリガ情報
  - `SKILL.md`: 詳細な指示書
  - `references/`: 補足資料やリファレンス
- **設計のベストプラクティス**:
  - 命名規則: `kebab-case`（例: `cve-report`）を厳守。
  - 推奨される記述: `description` は Claude が迷わないよう、実行トリガーを「強めに」書く。
- **NVD API 利用時の注意点**:
  - 公式免責事項（\"This product uses the NVD API but is not endorsed or certified by the NVD.\"）の表示が必須。
- **品質向上手法**:
  - `skill-creator` を活用し、曖昧なトリガやエラーハンドリングの不足をレビューしてもらうのが有効。
- **実運用へのヒント**:
  - 特定ベンダやスコアでフィルタリングする機能を追加することで、パッチ管理の補助ツールとしての応用が可能。