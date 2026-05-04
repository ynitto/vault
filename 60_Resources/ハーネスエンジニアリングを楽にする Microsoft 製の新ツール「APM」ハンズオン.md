---
title: "ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン"
source: "https://zenn.dev/microsoft/articles/agent-package-manager-handson"
author:
published: 2026-04-25
created: 2026-04-30
description:
tags:
  - "clippings"
---
### Microsoft製ツール「APM (Agent Package Manager)」の解説とハンズオン

本記事では、AIエージェントのプロンプトや設定ファイル（指示書）を効率的に管理・配布するOSS「APM」について解説しています。

#### **APMの主な特徴**
- **AIエージェント版の package.json**: プロジェクトごとにエージェント設定を依存関係として管理可能。
- **再現性の保証**: `apm.lock.yaml`に40桁のフルコミットハッシュを記録し、チーム開発での設定差分を排除。
- **マルチハーネス対応**: Copilot, Claude Code, Cursorなど、主要な開発ツールの設定を`apm install`コマンド一つで一括配置。

#### **開発者が得られるメリット**
- **高速オンボーディング**: 新メンバーは`apm install`を実行するだけで、チーム共通のAIエージェント設定が完結。
- **ルールの組織伝搬**: 規約の更新がGitの歴史として管理され、全員にスムーズに適用される。
- **拡張性**: 将来的に利用するツール（ハーネス）が増えても、設定を変換・再配置する手間が不要。

#### **セキュリティとガバナンス**
- **安全な設計**: 「File presence IS execution（ファイル配置＝実行）」という前提に基づき、配置前に不可視Unicode攻撃を自動ブロック。
- **組織ルール（`apm-policy.yml`）の強制**:
  - `apm audit`により、ローカルとCI環境の両方で不正なパッケージ利用を検知。
  - 違反時はインストールを自動ブロックし、GitHub Actions上でCode Scanning結果としてアラートを通知可能。

#### **導入のポイント**
- **構成**: 組織共通のポリシーリポジトリ（`.github/apm-policy.yml`）を用意することで、組織全体でのガバナンスを実現。
- **運用**: ネットワーク遮断時などに備え、`fetch_failure_default: block`を設定することで「ポリシーが取れない時は停止する」という厳格な運用も可能。
