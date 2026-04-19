---
title: "Claude CodeでSkillsを定期実行で自動化する方法"
source: "https://zenn.dev/tenormusica/articles/claude-code-headless-subscription-discovery-2025"
author:
published: 2025-12-29
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 記事要約
Claude Codeの「Skills（カスタムワークフロー）」をヘッドレスモード（`-p`オプション）で実行し、Task Schedulerやcronと組み合わせることで、**AIによる自律的な定期タスク実行を実現する方法**を解説した記事です。

### 要点まとめ
- **自動化の革新**: 従来の固定的なスクリプトと異なり、AIが状況を判断してツールを選択・実行するため、エラー発生時の柔軟な対応（リトライ、調査、報告）が可能。
- **Claude Codeの利点**:
  - API課金なし（サブスク認証を利用可能）。
  - ローカルファイル操作やリポジトリ全体へのアクセスが可能。
  - プロンプト定義のみで高度なタスクを短時間で作成可能。
- **活用シーン**:
  - サイドプロジェクトの健康維持（脆弱性確認、リポジトリ整理）。
  - 放置状態のプロジェクトのコンテキスト復旧。
  - 複数ツール（Slack、GitHub、Notion等）を横断する業務タスクの自動化。
- **技術的な実装**:
  - 環境変数 `ANTHROPIC_API_KEY` を空にしてサブスク認証を優先。
  - `claude -p` コマンドをバックグラウンドで実行。
- **注意点**:
  - 公式文書化されていない機能であり、SLAや保証はない。
  - PC常時起動が必要で、あくまで個人利用向けのハックである点に留意が必要。