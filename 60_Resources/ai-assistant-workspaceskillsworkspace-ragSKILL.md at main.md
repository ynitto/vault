---
original_source: 00_Inbox/Clippings/ai-assistant-workspaceskillsworkspace-ragSKILL.md at main.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, 2026-04]
---

---
title: "ai-assistant-workspace/skills/workspace-rag/SKILL.md at main"
source: "https://github.com/karaage0703/ai-assistant-workspace/blob/main/skills/workspace-rag/SKILL.md"
author:
published:
created: 2026-04-19
description: "Contribute to karaage0703/ai-assistant-workspace development by creating an account on GitHub."
tags:
  - "clippings"
---
### 概要
`workspace-rag`は、ワークスペース内のファイルをベクトル検索するための軽量なスキルです。SQLiteと`multilingual-e5`モデルを組み合わせ、高速な検索と関連度スコア付きの回答生成（R²AG簡易版）を実現します。

### 主な特徴
- **軽量設計**: SQLiteを使用し、外部DB不要で単一ファイルで管理。
- **インデックス機能**: 差分更新により、変更のあったファイルのみを効率的に処理。
- **高度な検索**: ベクトル検索とFTS5（キーワード検索）のハイブリッド構成。
- **R²AG対応**: 検索結果に関連度スコアを付与し、LLMが重要性を判断しやすい形式で出力。

### 利用のポイント
- **実行フロー**: セットアップ後にインデックスを作成し、サーバーまたはCLIから検索を行う。
- **検索モード**: 用途に応じて`hybrid`（デフォルト）、`vector`（意味重視）、`keyword`（単語重視）を使い分ける。
- **運用・管理**: 常駐HTTPサーバー（ポート7891）経由が推奨され、`pm2`による自動起動にも対応。
- **報告ルール**: 検索結果を報告する際は、ヒット件数、ファイルパス、関連度スコアを必ず明示する。