---
title: "mattpocock/skills完全ガイド｜Claude Code用スキル集で開発プロセスを自動化"
source: "https://ai-heartland.com/agent/mattpocock-skills/"
author:
  - "[[AI Heartland]]"
published: 2026-03-28
created: 2026-05-31
description: "mattpocock/skillsはClaude Code向けの実践スキル集。PRD作成・TDD・リファクタリング計画など18スキルをnpxコマンド1つで導入できる。14,500スター超の人気リポジトリの全スキルを日本語で徹底解説。"
tags:
  - "clippings"
---
### 概要
`mattpocock/skills`は、TypeScriptエキスパートのMatt Pocockが公開したClaude Code向けスキル集です。GitHubで14,500スター超を獲得しており、開発プロセスを「知識パッケージ」としてClaudeに学習させることで、AIによる開発自動化の質を大幅に向上させます。

### 要点まとめ
- **導入方法**: `npx skills@latest add [スキル名]`で必要なスキルだけを1行でインストール可能。
- **構造化された知識**: 単なるプロンプト集ではなく、`SKILL.md`を核にガイドラインや設計原則が同梱された「フォルダ構成」。Claudeは必要時にのみ参照するため、トークン消費を最適化できる。
- **主要カテゴリとスキル**:
    - **Planning & Design**: PRD自動生成や設計レビュー（`grill-me`）、並列サブエージェントによるインターフェース設計など。
    - **Development**: Vertical Sliceを強制する`tdd`や、Deep Moduleパターンに基づくアーキテクチャ改善など。
    - **Tooling & Setup**: Gitの破壊的コマンドをブロックするガードレールや、Husky等の環境構築を一括設定。
    - **Writing & Knowledge**: DDD用語集の自動生成や、Obsidianとの連携など。
- **差別化のポイント**: 開発者が独自に作るのではなく、体系化された「開発プロセス」をそのまま導入できるため、チームの品質標準化に最適。
- **実践的アプローチ**: 最初は`tdd`と`write-a-prd`の導入から始め、状況に応じてスキルを追加・カスタマイズする運用が推奨される。
