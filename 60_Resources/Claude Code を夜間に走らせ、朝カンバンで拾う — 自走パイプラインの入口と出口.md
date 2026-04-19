---
title: Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口
source: https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop
author: null
published: 2026-04-16
created: 2026-04-19
description: null
tags:
- resource/web
- ai-agent
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口.md
copied_at: 2026-04-19 10:51:13+09:00
---
### 概要
Claude Codeを夜間に自走させ、朝に効率よく成果を確認するための「入口（自動化・実行）」と「出口（カンバンによる可視化・管理）」を統合した運用設計について解説しています。

### 自動化の要点
- **入口の設計（インフラ）**: 
  - cronと `cmux` を活用し、並列でClaude Codeを起動。
  - スリープ防止設定や、ダイアログ・パーミッション設定を自動化して対話UIの壁を突破する。
  - リポジトリごとに設定を管理し、安定性を優先する。
- **出口の設計（UX）**: 
  - NotionからSQLiteへ移行し、自身のみが書き込めるセキュアな構成を採用。
  - タスクの状態（未着手・実行中・完了・待機中）をカンバンで管理。
  - 「マージGo」カラムの導入や、タブ分割、エラーのフォールバック処理で朝のタスク処理を効率化。

### 運用のコツ
- **非対称の管理**: 入口は「安定性」を、出口は「UXの改善」を重視する。
- **段階的な育成**: 最初は最小限の機能から始め、運用を通じてカラムやボタンを柔軟に足していく。
- **役割分担**: 失敗通知はSlack、進行管理と確認はカンバン（Web UI）と使い分ける。