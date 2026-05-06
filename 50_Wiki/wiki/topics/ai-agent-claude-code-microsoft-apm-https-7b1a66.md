---
title: "ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン"
type: "topic"
tags:
  - "ai-agent"
  - "claude-code"
  - "git"
  - "ci-cd"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md"
summary: "Microsoft製ツール「APM (Agent Package Manager)」の解説とハンズオン"
---

# ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン

## 概要

Microsoft製ツール「APM (Agent Package Manager)」の解説とハンズオン

*発行: 2026-04-25 / [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]*

## 主要なトピック

- [[ai-agent]]
- [[claude-code]]
- [[git]]
- [[ci-cd]]

## 詳細

- 本記事では、AIエージェントのプロンプトや設定ファイル（指示書）を効率的に管理・配布するOSS「APM」について解説しています。
- *APMの主な特徴**
- **AIエージェント版の package.json**: プロジェクトごとにエージェント設定を依存関係として管理可能。
- **再現性の保証**: `apm.lock.yaml`に40桁のフルコミットハッシュを記録し、チーム開発での設定差分を排除。
- **マルチハーネス対応**: Copilot, Claude Code, Cursorなど、主要な開発ツールの設定を`apm install`コマンド一つで一括配置。
- *開発者が得られるメリット**
- **高速オンボーディング**: 新メンバーは`apm install`を実行するだけで、チーム共通のAIエージェント設定が完結。
- **ルールの組織伝搬**: 規約の更新がGitの歴史として管理され、全員にスムーズに適用される。
- **拡張性**: 将来的に利用するツール（ハーネス）が増えても、設定を変換・再配置する手間が不要。

*発行: 2026-04-25 / [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]*

## 関連テーマ

- [[ai-agent]]
- [[claude-code]]
- [[git]]
- [[ci-cd]]

## 出典

- `../60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md`
- https://zenn.dev/microsoft/articles/agent-package-manager-handson
