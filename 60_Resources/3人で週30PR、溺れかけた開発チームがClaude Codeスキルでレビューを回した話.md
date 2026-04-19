---
original_source: 00_Inbox/Clippings/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, git, 2026-04]
---

---
title: "3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話"
source: "https://zenn.dev/tokium_dev/articles/pr-review-workflow-with-claude-code-skills"
author:
published: 2026-03-31
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
TOKIUMの3人チームが、Claude Codeを活用して「週30本以上のPRをさばく」開発体制におけるレビューボトルネックを解消した事例の紹介。

### 要点
- **背景**: 実装効率化でPR数が増加し、レビューが停滞。
- **解決策**: レビューの効率化に向けた3つの主要仕組みを構築。
  - **jira-to-pr**: チケットからPR作成までを一気通貫で自動化。
  - **agent-review**: 変更内容に基づき専門エージェントを動的に選定・並列実行。
  - **review-pattern-analysis**: 過去の指摘を分析し、ガイドラインを自動更新。
- **得られた成果**
  - AIによる一次スクリーニングで人間が本質的な判断に集中できる環境を実現。
  - 課題検知から改善までを高速で回せる、チームの自律的なスキル育成サイクルを確立。
- **今後の展望**
  - AIが自律的に品質を維持するハーネスエンジニアリング基盤の構築。