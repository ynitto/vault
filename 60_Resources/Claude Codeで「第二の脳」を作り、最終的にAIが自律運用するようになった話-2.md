---
title: Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話
source: https://qiita.com/yamapiiii/items/cc2450f410b64329d275
author:
- '[[yamapiiii]]'
published: 2026-03-01
created: 2026-05-05
description: はじめに 自分の思考・知識・アイデアを全て外部に書き出し、検索可能にする——いわゆる「第二の脳（Second Brain）」。 Notion、Obsidianで実践している人は多いと思います。私はこれをGitリポジトリ
  + Claude Codeで構築しました。 最初は「...
tags:
- clippings
- resource/web
- 2026-05
- claude-code
- ai-agent
- second-brain
- memory
original_source: 00_Inbox/Clippings/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 要約
本記事は、Claude CodeとGitリポジトリを組み合わせて、AIが自律的に整理・判断・実行を行う「第二の脳（Second Brain）」を構築する手法を解説しています。従来のツール（Notion等）にはない、ファイルシステム直結による自動化とバージョン管理の強みを活かし、思考の構造化からプロジェクト運用までをAIに委譲する設計を紹介しています。

### 要点まとめ
- **Gitリポジトリを採用する理由**
  - Claude Codeが直接読み書き可能なため、APIやプラグインなしでAIとの連携が可能。
  - Gitのバージョン管理機能で思考プロセスを完全追跡できる。

- **設計思想（brain vs project）**
  - `brain`（思考の保存庫）：Why/What、意思決定ログ、Issueを一元管理。
  - `project`（実装環境）：コードやテストを管理。
  - これらを分けることで事実源を単一化し、AIの迷いを排除。

- **AI運用の自動化**
  - **コマンドによるワンコマンド化**：14のカスタムコマンドでタスク分解から実行までを制御。
  - **PM Layerの自動介入**：既存フローにPMの判断（優先度付け、ブロッカー検出など）を組み込む。
  - **3層アーキテクチャ**：実行(CLI)→判断(オーケストレータ)→常時稼働(GitHub Actions)の順で段階的に自動化。

- **自律運用のための「ガードレール」**
  - 暴走を防ぐため、1チェーンの処理上限や禁止アクションを定義し、安全な範囲でAIに自律性を付与。
