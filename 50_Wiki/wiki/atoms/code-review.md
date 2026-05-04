---
title: "Code Review"
type: "concept"
tags:
  - "review"
  - "quality"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AIの成果物に責任を取る方法.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AIエージェントのハーネス設計｜Anthropicが公開した「生成と評価の分離」パターンを読み解く.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AI時代のコードレビュー ― 何を見るべきか、何は見なくてよくなったか.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agentic Repository.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon ECR でのライフサイクルポリシーを使用したイメージのクリーンアップの自動化.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Code に Codex の対立レビューを挟むと見えるもの — codex-plugin-cc で始めるセカンドオピニオン駆動開発.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Git の次へ。jj（Jujutsu）が変えるバージョン管理の常識.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub Copilot Chat のサブエージェントを検証してみた コンテキスト分離の効果と限界.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub Copilot エージェントの作成はエージェントに任せよう.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub Copilot サブエージェントによるオーケストレーター パターンの実践.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLab API で Merge Request のコメントを一括取得する方法.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLabと連携するMCP Serverを作った.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Obsidian でモーダルから入力できるプラグイン Modal Opener｜MaybeFix.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Obsidianで最適なPKM環境を考える.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ObsidianとClaudeではじめる日々のタスク管理と振り返り術.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Stacked Diffs (and why you should know about them).md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/git commit 時に実装を理解しているのか claude code に質問させる.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【Python】生成AIがこのコード書いたら気をつけろ！ - 事故らないためのチェックリスト.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ドキュメントをGit×Obsidianで管理してみませんか？【実プロジェクトでの導入事例とその手法】.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/仕様駆動を取り入れて4ヶ月ほど経ったので思うことなど.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/良いコードレビューとは.md"
summary: "コードレビューの観点と運用改善をまとめるページ。"
---

# Code Review

## 概要

























Code Review は品質担保だけでなく、知識共有とリスク検知のためのチームプロセスでもある。

























## 詳細

- [[claude-code-code-review-3-30pr-claude-4218c0]]: TOKIUMの3人チームが、Claude Codeを活用して「週30本以上のPRをさばく」開発体制におけるレビューボトルネックを解消した事例の紹介。
*発行: 2026-03-31 / [[claude-code-code-review-3-30pr-claude-4218c0]]*
- [[git-code-review-ai-https-zenn-dev-headwaters-articles-68de421c45931b-862b76]]: AIコーディング全盛期において、エンジニアは「自ら書く者」から「AIをマネジメントする意思決定者」へ役割が変化しています。AIに全責任を負わせるのではなく、人間が責任者として、プ…
*発行: 2026-04-24 / [[git-code-review-ai-https-zenn-dev-headwaters-articles-68de421c45931b-862b76]]*
- [[code-review-ai-anthropic-https-zenn-dev-takibilab-articles-anthropic-har-e438c5]]: Anthropicが公開した「Harness design for long-running application development」を基に、AIエージェントに長時間タス…
*発行: 2026-03-27 / [[code-review-ai-anthropic-https-zenn-dev-takibilab-articles-anthropic-har-e438c5]]*
- [[code-review-performance-ai-https-zenn-dev-pivotmedia-articles-ai-era-cod-e73bba]]: AIコーディング支援の普及により、コードレビューの役割は「実装の細部の修正」から「設計の妥当性の判断」へとシフトしています。
*発行: 2025-12-28 / [[code-review-performance-ai-https-zenn-dev-pivotmedia-articles-ai-era-cod-e73bba]]*
- [[ai-agent-claude-code-agent-skills-claude-43aee6]]: Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動収集・解説する「CVE…
*発行: 2026-03-17 / [[ai-agent-claude-code-agent-skills-claude-43aee6]]*
- [[ai-agent-git-agentic-repository-https-9fa56f]]: AIエージェントがGitHub上のIssue起票から実装、レビュー、デプロイ、エラー修正までを自律的に行う「Agentic Repository」の概念と、その実践における知見や…
*発行: 14日前にコメント追加 / [[ai-agent-git-agentic-repository-https-9fa56f]]*
- [[aws-amazon-ecr-amazon-ecr-https-c5efc2]]: Amazon ECR ライフサイクルポリシーの概要
- [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]: Claude Code向け公式プラグイン「codex-plugin-cc」を活用し、AnthropicのClaudeとOpenAIのCodexという異なるモデルを組み合わせること…
*発行: 2026-04-24 / [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]*
- [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]: Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度の低下を解決するため、複…
*発行: 2026-01-13 / [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]*
- [[git-code-review-git-jj-jujutsu-ae98c6]]: Googleエンジニアが開発した、Gitと完全互換性を持つ次世代バージョン管理システムです。Gitの複雑なワークフローを簡略化し、学習コストを低減することを目指しています。
*発行: 2026-01-27 / [[git-code-review-git-jj-jujutsu-ae98c6]]*
- [[git-code-review-copilot-chat-https-839576]]: GitHub Copilot Chat サブエージェントの概要と活用
*発行: 2025-12-03 / [[git-code-review-copilot-chat-https-839576]]*
- [[git-code-review-copilot-https-zenn-dev-microsoft-articles-264b7b02b406f0-1c035f]]: GitHub Copilot エージェントの開発効率化を目的とした「エージェントビルダー」の活用手法と、ワークフロー設計のベストプラクティスを解説しています。エージェント作成を個…
*発行: 2025-12-24 / [[git-code-review-copilot-https-zenn-dev-microsoft-articles-264b7b02b406f0-1c035f]]*
- [[git-code-review-copilot-https-zenn-dev-openjny-articles-e11450f61d067f-d0a5f9]]: VS Code v1.107の新機能である「カスタムエージェント（.agent.md）を`runSubagent`で直接呼び出す機能」を活用し、開発ワークフロー全体（Issue作…
*発行: 2025-12-03 / [[git-code-review-copilot-https-zenn-dev-openjny-articles-e11450f61d067f-d0a5f9]]*
- [[git-code-review-gitlab-api-merge-e03a0c]]: GitLab APIを活用し、チーム開発におけるコードレビューの質や量を定量化するための「Merge Request（MR）コメント集計ツール」の作成手法を解説した記事です。
*発行: 2021-12-21 / [[git-code-review-gitlab-api-merge-e03a0c]]*
- [[mcp-python-gitlab-mcp-server-85738e]]: GitLabとAIアシスタント（Cursor/Claude）を連携させ、開発効率を向上させるための「GitLab MCP Server」の開発・導入方法を紹介する記事です。
*発行: 2025-03-20 / [[mcp-python-gitlab-mcp-server-85738e]]*
- [[obsidian-code-review-obsidian-modal-opener-c13dc3]]: Obsidian プラグイン「Modal Opener」
*発行: 2024-11-17 / [[obsidian-code-review-obsidian-modal-opener-c13dc3]]*
- [[obsidian-git-obsidian-pkm-https-7aba73]]: 情報の整理が苦手な著者が、負担を減らしつつ必要な情報を管理・整理するため、Obsidianを用いたPKM（Personal Knowledge Management）環境を構築す…
*発行: 2023-12-20 / [[obsidian-git-obsidian-pkm-https-7aba73]]*
- [[obsidian-code-review-obsidian-claude-https-f71e1b]]: ObsidianとClaudeCodeによるタスク管理・振り返り術
*発行: 2025-12-20 / [[obsidian-code-review-obsidian-claude-https-f71e1b]]*
- [[cloudformation-code-review-stacked-diffs-why-142485]]: この記事は、MetaやGoogleで採用されている効率的なコードレビュー手法「Stacked Diffs（スタックド・ディフ）」について解説しています。これは、大きな機能を小さな…
- [[claude-code-git-git-commit-claude-4cfdea]]: AIエージェントへの実装丸投げによる「コード理解度の低下」を防ぐため、Gitの`pre-commit`フックを利用して「実装内容の自己確認」を自動化した取り組みについての記事です。
*発行: 2026-01-17 / [[claude-code-git-git-commit-claude-4cfdea]]*
- [[python-code-review-python-ai-https-379f7e]]: AIが生成するPythonコードには、開発速度を向上させる反面、セキュリティや保守性の観点で放置できない「危険なコードパターン」が混入することがあります。本記事では、AIが生成し…
*発行: 2025-09-20 / [[python-code-review-python-ai-https-379f7e]]*
- [[claude-code-code-review-claude-https-zenn-dev-oreguchi-articles-bf6ef30d-fcf3c9]]: Claude Codeなどの既存AIスキルを、言語・ロケール・実行エージェントといった3つの軸で、意図した通りの仕様に正確に変換するプラグイン「skill-conversion」…
*発行: 2026-04-28 / [[claude-code-code-review-claude-https-zenn-dev-oreguchi-articles-bf6ef30d-fcf3c9]]*
- [[obsidian-git-git-obsidian-https-7cfe86]]: Qiita記事要約：Git×Obsidianによるドキュメント管理
*発行: 2025-09-01 / [[obsidian-git-git-obsidian-https-7cfe86]]*
- [[code-review-4-https-zenn-dev-dress-code-articles-6ff2a65a02d2f7-1dadd9]]: Dress Code社のプロダクトエンジニアが、開発プロセスに「仕様駆動開発（Specification-Driven Development）」を導入して4ヶ月が経過した振り返…
*発行: 2026-04-26 / [[code-review-4-https-zenn-dev-dress-code-articles-6ff2a65a02d2f7-1dadd9]]*
- [[code-review-https-zenn-dev-danimal141-articles-a907e3d35561a0-reviewer-r-30a982]]: コードレビューの目的を「品質担保」「知識共有」「責任共有」と定義し、Reviewer（レビュワー）とReviewee（レビュイー）それぞれの視点から、実践すべきポイントと心構えを…
  *発行: 2024-12-09 / [[code-review-https-zenn-dev-danimal141-articles-a907e3d35561a0-reviewer-r-30a982]]*

## 関連

- [[claude-code-code-review-3-30pr-claude-4218c0]]
- [[testing]]
- [[ai-agent]]
- [[git]]
- [[git-code-review-ai-https-zenn-dev-headwaters-articles-68de421c45931b-862b76]]
- [[code-review-ai-anthropic-https-zenn-dev-takibilab-articles-anthropic-har-e438c5]]
- [[code-review-performance-ai-https-zenn-dev-pivotmedia-articles-ai-era-cod-e73bba]]
- [[ai-agent-claude-code-agent-skills-claude-43aee6]]
- [[ai-agent-git-agentic-repository-https-9fa56f]]
- [[aws-amazon-ecr-amazon-ecr-https-c5efc2]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話.md`
- https://zenn.dev/tokium_dev/articles/pr-review-workflow-with-claude-code-skills
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AIの成果物に責任を取る方法.md`
- https://zenn.dev/headwaters/articles/68de421c45931b
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AIエージェントのハーネス設計｜Anthropicが公開した「生成と評価の分離」パターンを読み解く.md`
- https://zenn.dev/takibilab/articles/anthropic-harness-design
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AI時代のコードレビュー ― 何を見るべきか、何は見なくてよくなったか.md`
- https://zenn.dev/pivotmedia/articles/ai-era-code-review
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md`
- https://dev.classmethod.jp/articles/claude-code-skills-cve-report/
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agentic Repository.md`
- https://zenn.dev/ishiharu/scraps/bdc773cc8e3f79
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon ECR でのライフサイクルポリシーを使用したイメージのクリーンアップの自動化.md`
- https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/LifecyclePolicies.html
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Code に Codex の対立レビューを挟むと見えるもの — codex-plugin-cc で始めるセカンドオピニオン駆動開発.md`
- https://qiita.com/nogataka/items/52dcdb315c54dddede01
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md`
- https://zenn.dev/cureapp/articles/c5016035a7d53d
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Git の次へ。jj（Jujutsu）が変えるバージョン管理の常識.md`
- https://zenn.dev/yamitake/articles/jj-jujutsu-modern-vcs-guide
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub Copilot Chat のサブエージェントを検証してみた コンテキスト分離の効果と限界.md`
- https://zenn.dev/openjny/articles/2619050ec7f167
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub Copilot エージェントの作成はエージェントに任せよう.md`
- https://zenn.dev/microsoft/articles/264b7b02b406f0
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub Copilot サブエージェントによるオーケストレーター パターンの実践.md`
- https://zenn.dev/openjny/articles/e11450f61d067f
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLab API で Merge Request のコメントを一括取得する方法.md`
- https://qiita.com/akkie76/items/2cc798e309b0e82f13fc
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLabと連携するMCP Serverを作った.md`
- https://zenn.dev/owayo/articles/e4c4496e6d79e7
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Obsidian でモーダルから入力できるプラグイン Modal Opener｜MaybeFix.md`
- https://note.com/maybefix/n/n0adffb4ebfe3
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Obsidianで最適なPKM環境を考える.md`
- https://zenn.dev/game8_blog/articles/0e50c36cd63b98
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ObsidianとClaudeではじめる日々のタスク管理と振り返り術.md`
- https://qiita.com/inamuu/items/d9b013b54a31a78e9c13
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Stacked Diffs (and why you should know about them).md`
- https://newsletter.pragmaticengineer.com/p/stacked-diffs
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/git commit 時に実装を理解しているのか claude code に質問させる.md`
- https://zenn.dev/buno15/articles/bf8c2c7c5a137b
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【Python】生成AIがこのコード書いたら気をつけろ！ - 事故らないためのチェックリスト.md`
- https://qiita.com/Sakai_path/items/d4ec1e848672033ca256
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った.md`
- https://zenn.dev/oreguchi/articles/bf6ef30d916552
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ドキュメントをGit×Obsidianで管理してみませんか？【実プロジェクトでの導入事例とその手法】.md`
- https://qiita.com/oga_aiichiro/items/1eb903562851f4f4a206
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/仕様駆動を取り入れて4ヶ月ほど経ったので思うことなど.md`
- https://zenn.dev/dress_code/articles/6ff2a65a02d2f7
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/良いコードレビューとは.md`
- https://zenn.dev/danimal141/articles/a907e3d35561a0
