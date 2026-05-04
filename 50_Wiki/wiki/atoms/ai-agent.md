---
title: "AI Agents"
type: "concept"
tags:
  - "ai"
  - "agent"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AIエージェント開発の新標準 ADLC を読み解く — IBM × Anthropicのガイドへの共感と、本番運用からの実践的フィードバック.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agent Skillsを行動評価する.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agentic Repository.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Codeで記憶領域を持つための独自のAgent Skillsを使っている.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応).md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【革命】AIが6時間自律コーディング！Anthropicの3エージェントHarnessが「放置開発」を実現した.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md"
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/🔥 はじめての Agent Skills 🔥 12 選＆リポジトリ一覧！GitHub Copilot でも使える AI の手順書.md"
summary: "AI エージェント設計・運用の知見を集約するページ。"
---

# AI Agents

## 概要














AI エージェントはタスク分解、ツール利用、評価、ガードレールなどを組み合わせて仕事を進める自律的なソフトウェア。














## 詳細

- [[ai-agent-ai-adlc-ibm-anthropic-fc72b4]]: IBMとAnthropicが提唱する「ADLC（Agent Development Lifecycle）」を軸に、AIエージェントを本番環境で運用するための新しい開発アプローチと…
*発行: 2026-04-04 / [[ai-agent-ai-adlc-ibm-anthropic-fc72b4]]*
- [[ai-agent-claude-code-agent-skills-claude-43aee6]]: Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動収集・解説する「CVE…
*発行: 2026-03-17 / [[ai-agent-claude-code-agent-skills-claude-43aee6]]*
- [[ai-agent-claude-code-agent-skills-https-b4ead4]]: AIエージェントの「Agent Skills」において、不安定なアウトプット（成果物）を直接評価するのではなく、**人事評価における「行動評価（コンピテンシー評価）」の概念を導入…
*発行: 2026-03-19 / [[ai-agent-claude-code-agent-skills-https-b4ead4]]*
- [[ai-agent-git-agentic-repository-https-9fa56f]]: AIエージェントがGitHub上のIssue起票から実装、レビュー、デプロイ、エラー修正までを自律的に行う「Agentic Repository」の概念と、その実践における知見や…
*発行: 14日前にコメント追加 / [[ai-agent-git-agentic-repository-https-9fa56f]]*
- [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]: Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度の低下を解決するため、複…
*発行: 2026-01-13 / [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]*
- [[ai-agent-claude-code-claude-agent-skills-7696df]]: Claude Codeで作業の中断・再開をスムーズにするための、Markdownベースの個人用記憶領域「agent-memory」スキルの導入方法と利点について解説しています。
*発行: 2026-01-05 / [[ai-agent-claude-code-claude-agent-skills-7696df]]*
- [[ai-agent-claude-code-claude-cli-agent-e8cd76]]: 「generating-skills-from-logs」は、Claude Codeの操作履歴やターミナルのCLIコマンド履歴を分析し、ユーザーの繰り返している作業を抽出して「A…
*発行: 2026-02-11 / [[ai-agent-claude-code-claude-cli-agent-e8cd76]]*
- [[ai-agent-git-copilot-agent-teams-6dc7c4]]: GitHubのリポジトリを「掲示板」として利用することで、離れた場所にある2台のPC間でGitHub Copilot Agentを協調させる仕組み「GH-Copilot Mult…
*発行: 2026-04-17 / [[ai-agent-git-copilot-agent-teams-6dc7c4]]*
- [[ai-agent-claude-code-obsidian-ai-claude-658516]]: Obsidian Agent Client Plugin: AIエージェントとチャット
*発行: 2026-02-25 / [[ai-agent-claude-code-obsidian-ai-claude-658516]]*
- [[ai-agent-mcp-python-mcp-vscode-854412]]: VSCode v1.99で導入された「Copilot Agent Mode」において、MCP（Model Context Protocol）を使用して外部ツールをAIに利用させる…
*発行: 2025-04-30 / [[ai-agent-mcp-python-mcp-vscode-854412]]*
- [[ai-agent-claude-code-skills-50-agent-3668e6]]: 本記事では、50個以上の「Agent Skills」を運用する中で直面した管理コスト増大の課題に対し、著者が見出した**CI・テスト・品質管理の具体的な設計手法**を解説していま…
*発行: 2026-04-03 / [[ai-agent-claude-code-skills-50-agent-3668e6]]*
- [[ai-agent-emi-ndk-ai-6-anthropic-e5b38d]]: Anthropicが提案した「3-Agent Harness」アーキテクチャは、Planner・Generator・Evaluatorの3つのエージェントを役割分担させることで、…
*発行: 2026-04-22 / [[ai-agent-emi-ndk-ai-6-anthropic-e5b38d]]*
- [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]: Microsoft製ツール「APM (Agent Package Manager)」の解説とハンズオン
*発行: 2026-04-25 / [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]*
- [[ai-agent-git-agent-skills-12-5d95b6]]: Agent Skills は、AI エージェントに専門知識や特定のワークフローをパッケージ化して教えるためのオープンスタンダードです。
  *発行: 2025-12-24 / [[ai-agent-git-agent-skills-12-5d95b6]]*

## 関連

- [[ai-agent-ai-adlc-ibm-anthropic-fc72b4]]
- [[claude-code]]
- [[mcp]]
- [[code-review]]
- [[ai-agent-claude-code-agent-skills-claude-43aee6]]
- [[ai-agent-claude-code-agent-skills-https-b4ead4]]
- [[ai-agent-git-agentic-repository-https-9fa56f]]
- [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]
- [[ai-agent-claude-code-claude-agent-skills-7696df]]
- [[ai-agent-claude-code-claude-cli-agent-e8cd76]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AIエージェント開発の新標準 ADLC を読み解く — IBM × Anthropicのガイドへの共感と、本番運用からの実践的フィードバック.md`
- https://zenn.dev/dxclab/articles/9f015ee80cd809
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md`
- https://dev.classmethod.jp/articles/claude-code-skills-cve-report/
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agent Skillsを行動評価する.md`
- https://zenn.dev/levtech/articles/3d066a9e59785d
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Agentic Repository.md`
- https://zenn.dev/ishiharu/scraps/bdc773cc8e3f79
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md`
- https://zenn.dev/cureapp/articles/c5016035a7d53d
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Codeで記憶領域を持つための独自のAgent Skillsを使っている.md`
- https://zenn.dev/yamadashy/articles/claude-code-agent-skills-agent-memory
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する.md`
- https://zenn.dev/takiko/articles/claude-code-skill-from-logs
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った.md`
- https://qiita.com/aktsmm/items/28f38fd1edea4edab31b
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応).md`
- https://zenn.dev/tokium_dev/articles/2fc1fa15407efe
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する.md`
- https://zenn.dev/mochizuki875/articles/1f7f3f3527fcf9
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md`
- https://qiita.com/nogataka/items/61365a15677fb62aa41a
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【革命】AIが6時間自律コーディング！Anthropicの3エージェントHarnessが「放置開発」を実現した.md`
- https://qiita.com/emi_ndk/items/facb4cecfd145f6d6c1a
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md`
- https://zenn.dev/microsoft/articles/agent-package-manager-handson
- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/🔥 はじめての Agent Skills 🔥 12 選＆リポジトリ一覧！GitHub Copilot でも使える AI の手順書.md`
- https://qiita.com/aktsmm/items/08eef2cdeeb0a32b69a2
