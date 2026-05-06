---
title: "Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口"
type: "topic"
tags:
  - "claude-code"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口.md"
summary: "Claude Codeを夜間に自走させ、朝に効率よく成果を確認するための「入口（自動化・実行）」と「出口（カンバンによる可視化・管理）」を統合した運用設計…"
---

# Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口

## 概要

Claude Codeを夜間に自走させ、朝に効率よく成果を確認するための「入口（自動化・実行）」と「出口（カンバンによる可視化・管理）」を統合した運用設計について解説しています。

*発行: 2026-04-16 / [[claude-code-claude-https-zenn-dev-pepabo-articles-claude-code-night-auto-46c5d9]]*

## 主要なトピック

- [[claude-code]]

## 詳細

- Claude Codeを夜間に自走させ、朝に効率よく成果を確認するための「入口（自動化・実行）」と「出口（カンバンによる可視化・管理）」を統合した運用設計について解説しています。
- 自動化の要点
- **入口の設計（インフラ）**:
- cronと `cmux` を活用し、並列でClaude Codeを起動。
- スリープ防止設定や、ダイアログ・パーミッション設定を自動化して対話UIの壁を突破する。
- リポジトリごとに設定を管理し、安定性を優先する。
- **出口の設計（UX）**:
- NotionからSQLiteへ移行し、自身のみが書き込めるセキュアな構成を採用。
- タスクの状態（未着手・実行中・完了・待機中）をカンバンで管理。

*発行: 2026-04-16 / [[claude-code-claude-https-zenn-dev-pepabo-articles-claude-code-night-auto-46c5d9]]*

## 関連テーマ

- [[claude-code]]

## 出典

- `../60_Resources/Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口.md`
- https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop
