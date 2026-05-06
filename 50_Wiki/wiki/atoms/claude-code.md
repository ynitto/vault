---
title: "Claude Code"
type: "product"
tags:
  - "ai"
  - "claude-code"
created: "2026-05-02"
updated: "2026-05-06"
sources:
  - "../60_Resources/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話.md"
  - "../../60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md"
  - "../60_Resources/Agent Skillsを行動評価する.md"
  - "../60_Resources/Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する.md"
  - "../60_Resources/Claude Code Hooks × markitdown で非MDファイルを透過的にMarkdown変換する.md"
  - "../60_Resources/Claude Code × Obsidian Vault で作る「何でも相談」プロジェクト ― フォルダ構成・CLAUDE.md・MCP設定まで全公開.md"
  - "../60_Resources/Claude Code に Codex の対立レビューを挟むと見えるもの — codex-plugin-cc で始めるセカンドオピニオン駆動開発.md"
  - "../60_Resources/Claude Code の Skills でエラー調査を自動化！初動対応を 3 分に短縮する方法.md"
  - "../60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md"
  - "../60_Resources/Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口.md"
  - "../60_Resources/Claude CodeでSkillsを定期実行で自動化する方法.md"
  - "../60_Resources/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md"
  - "../60_Resources/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話-2.md"
  - "../60_Resources/あなたのClaude CodeのWebFetch、実はWebをちゃんと読んでいない.md"
  - "../60_Resources/既存コードから仕様書を逆生成するClaude Codeスキル cc-rsg を作ってみた.md"
  - "../60_Resources/Claude Codeで記憶領域を持つための独自のAgent Skillsを使っている.md"
  - "../60_Resources/Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する.md"
  - "../60_Resources/Claude Codeのloopで自律的にパフォーマンスチューニングのPDCAを回させる仕組みを作った【autoresearch】.md"
  - "../60_Resources/Claude CodeのエージェントでAIコンサルタントを構築する｜McKinsey流フレームワークの実装方法.md"
  - "../60_Resources/Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する.md"
  - "../60_Resources/Claude Codeの拡張機能を活用した並列開発プラグインの設計と実装.md"
  - "../60_Resources/Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った.md"
  - "../60_Resources/Claude Code・Codex・Gemini の会話ログを日次Markdownとして自動整理する ― chat_logs から LLM_history を自動生成する仕組み.md"
  - "../60_Resources/CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた.md"
  - "../60_Resources/Karpathy 氏が言語化した「LLM Knowledge Base」というパターン.md"
  - "../60_Resources/LLMに長期記憶を実装する.md"
  - "../60_Resources/Markdown ドキュメント間の整合性を検証する contextlint を作っている話.md"
  - "../60_Resources/Obsidian CLI が全ユーザーに無料開放されたので Claude Code 用スキルと一緒にセットアップした.md"
  - "../../60_Resources/Obsidian x AIで執筆革命！Windows(WSL2)でClaude CodeとGemini CLIを連携させる最強ガイド.md"
  - "../60_Resources/Obsidian × Claude Codeで情報整理を緩くやってみたけど、想像以上によかった話.md"
  - "../../60_Resources/ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応).md"
  - "../60_Resources/ObsidianとCodex CLIの使い道.md"
  - "../60_Resources/Skill SeekersでURLやローカルドキュメントからClaude Codeのスキルを生成してみる.md"
  - "../60_Resources/Skillsで実現する軽量パーソナルRAG.md"
  - "../60_Resources/TAKT を調べて気づいた、Claude Code ネイティブでも同じ課題を解けるということ.md"
  - "../60_Resources/git commit 時に実装を理解しているのか claude code に質問させる.md"
  - "../60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md"
  - "../60_Resources/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md"
  - "../60_Resources/あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った.md"
  - "../60_Resources/コピペで使えるエージェント設計テンプレート ── agency-agentsの5原則から学ぶ「良いエージェント」の作り方.md"
  - "../60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md"
  - "../60_Resources/プロンプトの改善効果を可視化するClaude Codeプラグインを作った.md"
summary: "Claude Code とスキル活用に関する知見。"
---

# Claude Code

## 概要







































Claude Code は AI エージェント的なコーディング支援を行う CLI で、スキルやレビュー自動化との相性が高い。







































## 詳細

- [[claude-code-code-review-3-30pr-claude-4218c0]]: TOKIUMの3人チームが、Claude Codeを活用して「週30本以上のPRをさばく」開発体制におけるレビューボトルネックを解消した事例の紹介。
*発行: 2026-03-31 / [[claude-code-code-review-3-30pr-claude-4218c0]]*
- [[ai-agent-claude-code-agent-skills-claude-43aee6]]: Claude Code Skills（AIに繰り返し作業の手順を覚えさせる仕組み）を活用し、NVD（米国脆弱性データベース）から直近の重要脆弱性情報を自動収集・解説する「CVE…
*発行: 2026-03-17 / [[ai-agent-claude-code-agent-skills-claude-43aee6]]*
- [[ai-agent-claude-code-agent-skills-https-b4ead4]]: AIエージェントの「Agent Skills」において、不安定なアウトプット（成果物）を直接評価するのではなく、**人事評価における「行動評価（コンピテンシー評価）」の概念を導入…
*発行: 2026-03-19 / [[ai-agent-claude-code-agent-skills-https-b4ead4]]*
- [[claude-code-performance-boris-cherny-claude-md-bdfa7a]]: `CLAUDE.md`は、Claude Codeがセッション開始時に読み込む設定ファイルです。プロジェクトルートに配置することで、AIにチームのルールや作業方針を事前に伝え、AI…
*発行: 2026-02-23 / [[claude-code-performance-boris-cherny-claude-md-bdfa7a]]*
- [[claude-code-obsidian-claude-hooks-markitdown-86362e]]: Claude Code の `PreToolUse Hook` と Microsoft の `markitdown` を活用し、PDFやOfficeファイルなどの非Markdow…
*発行: 2026-04-23 / [[claude-code-obsidian-claude-hooks-markitdown-86362e]]*
- [[claude-code-aws-claude-obsidian-vault-5c1a30]]: Claude CodeとObsidianを連携させ、プロジェクト成果物を自動整理・蓄積する「何でも相談-pj」の構築手法。プロジェクトルートを汚さず、知識をグラフ化・管理する効率…
*発行: 2026-04-18 / [[claude-code-aws-claude-obsidian-vault-5c1a30]]*
- [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]: Claude Code向け公式プラグイン「codex-plugin-cc」を活用し、AnthropicのClaudeとOpenAIのCodexという異なるモデルを組み合わせること…
*発行: 2026-04-24 / [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]*
- [[claude-code-mcp-claude-skills-3-5ddf67]]: 本記事では、Claude CodeのSkillsとMCP（Model Context Protocol）を組み合わせ、エラー発生時の調査からGitHubへのIssue作成までを自…
*発行: 2026-03-30 / [[claude-code-mcp-claude-skills-3-5ddf67]]*
- [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]: Claude Code の Agent Skills として「Progressive Workflow」が公開されました。LLMの注意力分散による回答精度の低下を解決するため、複…
*発行: 2026-01-13 / [[ai-agent-claude-code-claude-agent-skills-ffbb8c]]*
- [[claude-code-claude-https-zenn-dev-pepabo-articles-claude-code-night-auto-46c5d9]]: Claude Codeを夜間に自走させ、朝に効率よく成果を確認するための「入口（自動化・実行）」と「出口（カンバンによる可視化・管理）」を統合した運用設計について解説しています。
*発行: 2026-04-16 / [[claude-code-claude-https-zenn-dev-pepabo-articles-claude-code-night-auto-46c5d9]]*
- [[claude-code-git-claude-skills-https-2f1a7a]]: Claude Codeの「Skills（カスタムワークフロー）」をヘッドレスモード（`-p`オプション）で実行し、Task Schedulerやcronと組み合わせることで、**…
*発行: 2025-12-29 / [[claude-code-git-claude-skills-https-2f1a7a]]*
- [[claude-code-git-claude-ai-https-0cd21e]]: GitリポジトリとClaude Codeを組み合わせ、自身の思考やプロジェクト管理を「第二の脳（Second Brain）」として構築・自動運用する方法を解説した実践録です。No…
*発行: 2026-03-01 / [[claude-code-git-claude-ai-https-0cd21e]]*
- `Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話-2` でも、brain / project 分離と Git ベース運用を前提に、AI が整理・判断・実行まで担う構成が整理されている。
- `あなたのClaude CodeのWebFetch、実はWebをちゃんと読んでいない` は、外部取得の成功判定を厳密化しないと「読めたつもり」が発生するという運用上の失敗パターンを示す。
- `既存コードから仕様書を逆生成するClaude Codeスキル cc-rsg を作ってみた` は、Claude Code で逆仕様生成を行う際に、トレーサビリティ・未確定事項の明示・機械的カバレッジ検証を重視すべきことを示す。
- [[ai-agent-claude-code-claude-agent-skills-7696df]]: Claude Codeで作業の中断・再開をスムーズにするための、Markdownベースの個人用記憶領域「agent-memory」スキルの導入方法と利点について解説しています。
*発行: 2026-01-05 / [[ai-agent-claude-code-claude-agent-skills-7696df]]*
- [[claude-code-claude-skills-https-zenn-dev-shintaroamaike-articles-df3ecc0-a805cd]]: Claude Codeのコーディングルール管理を自動化するスキル「AutoHarness」の紹介記事です。プロジェクト固有の規約を自動生成・適用することで、AIによるコード品質の…
*発行: 2026-04-01 / [[claude-code-claude-skills-https-zenn-dev-shintaroamaike-articles-df3ecc0-a805cd]]*
- [[claude-code-claude-loop-pdca-autoresearch-bb3806]]: Andre Karpathy氏が公開したAI自律改善リポジトリ「autoresearch」の概念を応用し、RailsコントローラーのパフォーマンスチューニングをAIが自律的に行う…
*発行: 2026-03-30 / [[claude-code-claude-loop-pdca-autoresearch-bb3806]]*
- [[claude-code-claude-ai-mckinsey-https-481f78]]: Claude Codeのエージェント機能を活用し、McKinsey/BCG流の思考フレームワーク（空・雨・傘）を組み込んだ「AIコンサルタント」の構築・運用方法を解説する記事です。
*発行: 2026-04-10 / [[claude-code-claude-ai-mckinsey-https-481f78]]*
- [[ai-agent-claude-code-claude-cli-agent-e8cd76]]: 「generating-skills-from-logs」は、Claude Codeの操作履歴やターミナルのCLIコマンド履歴を分析し、ユーザーの繰り返している作業を抽出して「A…
*発行: 2026-02-11 / [[ai-agent-claude-code-claude-cli-agent-e8cd76]]*
- [[claude-code-git-claude-https-zenn-dev-genda-e53a2b]]: Claude Codeの拡張機能（Agent, Command, Hooks, Skills, Plugin）を駆使し、Git worktreeとtmuxを組み合わせて**大規模…
*発行: 2026-01-06 / [[claude-code-git-claude-https-zenn-dev-genda-e53a2b]]*
- [[claude-code-performance-claude-windows-mac-264600]]: 本記事は、マルチデバイス（Windows/Mac）環境でClaude Codeの「長期記憶」を同期するための自作システムについての解説です。SQLiteをローカルキャッシュ、JS…
*発行: 2026-03-24 / [[claude-code-performance-claude-windows-mac-264600]]*
- [[claude-code-claude-codex-gemini-markdown-bf6987]]: 本記事は、Claude Code、Codex、Geminiといった複数のAIツールの会話ログを自動的に集約・整形し、振り返りやすいMarkdown形式で保存する運用手法の解説です…
*発行: 2026-03-08 / [[claude-code-claude-codex-gemini-markdown-bf6987]]*
- [[claude-code-aws-cloudformation-rain-fmt-15db66]]: AWS CloudFormationテンプレートの品質担保に向け、コーディング規約の策定と、それを自動的に守るためのツール環境（rain, cfn-lint, Claude Co…
*発行: 2026-03-24 / [[claude-code-aws-cloudformation-rain-fmt-15db66]]*
- [[claude-code-performance-karpathy-llm-knowledge-31f701]]: Andrej Karpathy氏が提唱した「LLM Knowledge Base」という概念を紹介し、生のドキュメントをLLMに構造化・コンパイルさせることで、永続的なナレッジベ…
*発行: 2026-04-05 / [[claude-code-performance-karpathy-llm-knowledge-31f701]]*
- [[claude-code-performance-llm-https-zenn-dev-j-5efbfc]]: Claude Codeに、人間の脳の仕組み（情動、忘却、再構成など）を模倣した長期記憶システムをPythonで実装した事例。単なるデータベース検索ではなく、時間帯や気分、文脈に応…
*発行: 2026-03-10 / [[claude-code-performance-llm-https-zenn-dev-j-5efbfc]]*
- [[claude-code-mcp-markdown-contextlint-https-b7c780]]: `contextlint` は、AI 活用型開発（仕様駆動開発：SDD）において、Markdown ドキュメント間の整合性を自動検証する静的解析ツールです。
*発行: 2026-03-07 / [[claude-code-mcp-markdown-contextlint-https-b7c780]]*
- [[claude-code-obsidian-obsidian-cli-claude-5c90af]]: Obsidian CLI 無料開放とClaude Code用スキルセットアップ
*発行: 2026-03-27 / [[claude-code-obsidian-obsidian-cli-claude-5c90af]]*
- [[claude-code-obsidian-obsidian-x-ai-845ca8]]: Qiita記事「Obsidian x AIで執筆革命！」要約
*発行: 2025-07-07 / [[claude-code-obsidian-obsidian-x-ai-845ca8]]*
- [[claude-code-mcp-obsidian-claude-https-df38b1]]: Obsidian × Claude Code による情報整理
*発行: 2025-12-11 / [[claude-code-mcp-obsidian-claude-https-df38b1]]*
- [[ai-agent-claude-code-obsidian-ai-claude-658516]]: Obsidian Agent Client Plugin: AIエージェントとチャット
*発行: 2026-02-25 / [[ai-agent-claude-code-obsidian-ai-claude-658516]]*
- [[claude-code-obsidian-obsidian-codex-cli-408535]]: この記事では、ObsidianのノートをCodex CLIと組み合わせてレポートを作成する手順と、その応用例について解説しています。
*発行: 2025-09-14 / [[claude-code-obsidian-obsidian-codex-cli-408535]]*
- [[claude-code-git-skill-seekers-url-7451d2]]: 「Skill Seekers」は、URL、GitHubリポジトリ、ローカルファイルなど多様なソースから「Claude Code Skills」を自動生成・管理するPythonツー…
*発行: 2026-04-07 / [[claude-code-git-skill-seekers-url-7451d2]]*
- [[claude-code-docker-skills-rag-https-fd7de4]]: 軽量パーソナルRAG「workspace-rag」の概要
*発行: 2026-03-01 / [[claude-code-docker-skills-rag-https-fd7de4]]*
- [[claude-code-takt-claude-https-zenn-dev-kok1eeeee-articles-o-m-cc-takt-in-280922]]: AIエージェントの「指示に従わない」「脱線する」といった課題に対し、外部エンジンを用いたツール「TAKT」と、Claude Codeのプラグインとして独自開発された「o-m-cc…
*発行: 2026-02-18 / [[claude-code-takt-claude-https-zenn-dev-kok1eeeee-articles-o-m-cc-takt-in-280922]]*
- [[claude-code-git-git-commit-claude-4cfdea]]: AIエージェントへの実装丸投げによる「コード理解度の低下」を防ぐため、Gitの`pre-commit`フックを利用して「実装内容の自己確認」を自動化した取り組みについての記事です。
*発行: 2026-01-17 / [[claude-code-git-git-commit-claude-4cfdea]]*
- [[ai-agent-claude-code-skills-50-agent-3668e6]]: 本記事では、50個以上の「Agent Skills」を運用する中で直面した管理コスト増大の課題に対し、著者が見出した**CI・テスト・品質管理の具体的な設計手法**を解説していま…
*発行: 2026-04-03 / [[ai-agent-claude-code-skills-50-agent-3668e6]]*
- [[claude-code-obsidian-llm-wiki-obsidian-3c6281]]: 本記事では、Karpathy氏が提唱する「LLM Wiki」の概念をClaude Codeのスキルとして実装し、Obsidianと連携して運用する方法について解説しています。
*発行: 2026-04-14 / [[claude-code-obsidian-llm-wiki-obsidian-3c6281]]*
- [[claude-code-code-review-claude-https-zenn-dev-oreguchi-articles-bf6ef30d-fcf3c9]]: Claude Codeなどの既存AIスキルを、言語・ロケール・実行エージェントといった3つの軸で、意図した通りの仕様に正確に変換するプラグイン「skill-conversion」…
*発行: 2026-04-28 / [[claude-code-code-review-claude-https-zenn-dev-oreguchi-articles-bf6ef30d-fcf3c9]]*
- [[claude-code-agency-agents-5-https-qiita-com-nogataka-items-d4ad685c7901f-b4b470]]: 本記事は、OSSプロジェクト「agency-agents」のガイドラインを基に、高品質なAIエージェントを設計するための5つの原則とテンプレートを解説しています。汎用的なアシスタ…
*発行: 2026-03-14 / [[claude-code-agency-agents-5-https-qiita-com-nogataka-items-d4ad685c7901f-b4b470]]*
- [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]: Microsoft製ツール「APM (Agent Package Manager)」の解説とハンズオン
*発行: 2026-04-25 / [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]*
- [[claude-code-git-claude-https-zenn-dev-shinpr-948812]]: 本記事は、プロンプトの改善効果を可視化・検証できるClaude Codeプラグイン「Rashomon」の紹介です。プロンプトエンジニアリングの試行錯誤を自動化し、改善が及ぼす影響…
  *発行: 2026-01-15 / [[claude-code-git-claude-https-zenn-dev-shinpr-948812]]*

## 関連

- [[claude-code-code-review-3-30pr-claude-4218c0]]
- [[ai-agent]]
- [[code-review]]
- [[mcp]]
- [[ai-agent-claude-code-agent-skills-claude-43aee6]]
- [[ai-agent-claude-code-agent-skills-https-b4ead4]]
- [[claude-code-performance-boris-cherny-claude-md-bdfa7a]]
- [[claude-code-obsidian-claude-hooks-markitdown-86362e]]
- [[claude-code-aws-claude-obsidian-vault-5c1a30]]
- [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]

## 出典

- `../60_Resources/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話.md`
- https://zenn.dev/tokium_dev/articles/pr-review-workflow-with-claude-code-skills
- `../../60_Resources/Agent Skills (Claude Code Skills) の公式ガイドに沿って、CVE 脆弱性情報収集用の Skill を作ってみた.md`
- https://dev.classmethod.jp/articles/claude-code-skills-cve-report/
- `../60_Resources/Agent Skillsを行動評価する.md`
- https://zenn.dev/levtech/articles/3d066a9e59785d
- `../60_Resources/Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する.md`
- https://qiita.com/uno_ha07/items/5820d195510861b5be71
- `../60_Resources/Claude Code Hooks × markitdown で非MDファイルを透過的にMarkdown変換する.md`
- https://zenn.dev/tuzuminami/articles/e487adfd650289
- `../60_Resources/Claude Code × Obsidian Vault で作る「何でも相談」プロジェクト ― フォルダ構成・CLAUDE.md・MCP設定まで全公開.md`
- https://qiita.com/htani0817/items/0cb5e8f91fa64fb9ba8c
- `../60_Resources/Claude Code に Codex の対立レビューを挟むと見えるもの — codex-plugin-cc で始めるセカンドオピニオン駆動開発.md`
- https://qiita.com/nogataka/items/52dcdb315c54dddede01
- `../60_Resources/Claude Code の Skills でエラー調査を自動化！初動対応を 3 分に短縮する方法.md`
- https://zenn.dev/babyjob/articles/claude-code-mcp-error-analyze
- `../60_Resources/Claude Code の集中力を保つ Agent Skills を作った.md`
- https://zenn.dev/cureapp/articles/c5016035a7d53d
- `../60_Resources/Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口.md`
- https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop
- `../60_Resources/Claude CodeでSkillsを定期実行で自動化する方法.md`
- https://zenn.dev/tenormusica/articles/claude-code-headless-subscription-discovery-2025
- `../60_Resources/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md`
- https://qiita.com/yamapiiii/items/cc2450f410b64329d275
- `../60_Resources/Claude Codeで記憶領域を持つための独自のAgent Skillsを使っている.md`
- https://zenn.dev/yamadashy/articles/claude-code-agent-skills-agent-memory
- `../60_Resources/Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する.md`
- https://zenn.dev/shintaroamaike/articles/df3ecc0ddee047
- `../60_Resources/Claude Codeのloopで自律的にパフォーマンスチューニングのPDCAを回させる仕組みを作った【autoresearch】.md`
- https://zenn.dev/dely_jp/articles/3117e590465e38
- `../60_Resources/Claude CodeのエージェントでAIコンサルタントを構築する｜McKinsey流フレームワークの実装方法.md`
- https://qiita.com/rcomcpgm-cyber/items/901344b211a6a3e7dda7
- `../60_Resources/Claude Codeのセッション履歴とCLIの実行履歴から Agent Skill を自動生成する.md`
- https://zenn.dev/takiko/articles/claude-code-skill-from-logs
- `../60_Resources/Claude Codeの拡張機能を活用した並列開発プラグインの設計と実装.md`
- https://zenn.dev/genda_jp/articles/b268146f3d5392
- `../60_Resources/Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った.md`
- https://zenn.dev/aoi_umigishi/articles/fc877d2d7d3e38
- `../60_Resources/Claude Code・Codex・Gemini の会話ログを日次Markdownとして自動整理する ― chat_logs から LLM_history を自動生成する仕組み.md`
- https://qiita.com/rxg03350/items/9bd822a2be5549b17878
- `../60_Resources/CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた.md`
- https://dev.classmethod.jp/articles/cfn-coding-guidelines/
- `../60_Resources/Karpathy 氏が言語化した「LLM Knowledge Base」というパターン.md`
- https://dev.classmethod.jp/articles/karpathy-llm-knowledge-base/
- `../60_Resources/LLMに長期記憶を実装する.md`
- https://zenn.dev/j_m/articles/efcc4f224cc8ca
- `../60_Resources/Markdown ドキュメント間の整合性を検証する contextlint を作っている話.md`
- https://zenn.dev/nozomi_cobo/articles/contextlint-introduction
- `../60_Resources/Obsidian CLI が全ユーザーに無料開放されたので Claude Code 用スキルと一緒にセットアップした.md`
- https://zenn.dev/kairininja/articles/zenn-obsidian-cli-agent-skills-setup
- `../../60_Resources/Obsidian x AIで執筆革命！Windows(WSL2)でClaude CodeとGemini CLIを連携させる最強ガイド.md`
- https://qiita.com/toki_mwc/items/c1c448344a2ecb810eb1
- `../60_Resources/Obsidian × Claude Codeで情報整理を緩くやってみたけど、想像以上によかった話.md`
- https://zenn.dev/stafes_blog/articles/d7457519a2daec
- `../../60_Resources/ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応).md`
- https://zenn.dev/tokium_dev/articles/2fc1fa15407efe
- `../60_Resources/ObsidianとCodex CLIの使い道.md`
- https://roompine.com/obsidian-codex-cli-use-cases-1/
- `../60_Resources/Skill SeekersでURLやローカルドキュメントからClaude Codeのスキルを生成してみる.md`
- https://dev.classmethod.jp/articles/skill-seekers-claude-code-skills/
- `../60_Resources/Skillsで実現する軽量パーソナルRAG.md`
- https://zenn.dev/karaage0703/articles/d7eaf62437185d
- `../60_Resources/TAKT を調べて気づいた、Claude Code ネイティブでも同じ課題を解けるということ.md`
- https://zenn.dev/kok1eeeee/articles/o-m-cc-takt-inspired-update
- `../60_Resources/git commit 時に実装を理解しているのか claude code に質問させる.md`
- https://zenn.dev/buno15/articles/bf8c2c7c5a137b
- `../60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md`
- https://qiita.com/nogataka/items/61365a15677fb62aa41a
- `../60_Resources/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md`
- https://zenn.dev/dely_jp/articles/8b55114cc0b958
- `../60_Resources/あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った.md`
- https://zenn.dev/oreguchi/articles/bf6ef30d916552
- `../60_Resources/コピペで使えるエージェント設計テンプレート ── agency-agentsの5原則から学ぶ「良いエージェント」の作り方.md`
- https://qiita.com/nogataka/items/d4ad685c7901f2056c6f
- `../60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md`
- https://zenn.dev/microsoft/articles/agent-package-manager-handson
- `../60_Resources/プロンプトの改善効果を可視化するClaude Codeプラグインを作った.md`
- https://zenn.dev/shinpr_p/articles/d0e6b387558e97
