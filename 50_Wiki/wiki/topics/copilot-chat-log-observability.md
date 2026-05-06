---
title: "Copilot Chat.log observability"
type: "topic"
tags:
  - "copilot"
  - "vscode"
  - "observability"
  - "resource-ingest"
created: "2026-05-05"
updated: "2026-05-06"
sources:
  - ".wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/2026-05-05-copilot-session-20260505t194454-window1.md"
  - ".wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/2026-05-05-copilot-session-20260505t194454-window2.md"
  - ".wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/2026-05-02-copilot-session-20260502t045136-window2.md"
  - ".wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/copilot-2026-05-06-cae269c6.md"
  - ".wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/copilot-2026-05-05-6aeba88b.md"
summary: "GitHub Copilot Chat.log は会話本文よりも、モデル呼び出し・接続障害・認証失敗を観測する運用ログとして有効である。"
---

# Copilot Chat.log observability

## 概要

GitHub Copilot の `GitHub Copilot Chat.log` は、会話本文の完全なトランスクリプトではなく、実行基盤の状態を観測するためのログである。

## 主要なトピック

- [[observability]]
- [[mcp]]
- [[git]]

## 詳細

- macOS の VS Code 環境では、Copilot Chat のログは `~/Library/Application Support/Code/logs/<timestamp>/window*/exthost/GitHub.copilot-chat/GitHub Copilot Chat.log` に保存される。
- ログには `panel/editAgent`、`healApplyPatch` などの処理種別と、`gpt-5.3-codex`、`gpt-4o-mini-2024-07-18` などのモデル利用情報が残る。
- `net::ERR_ADDRESS_UNREACHABLE`、`No repository properties found`、`enumDescriptions` 由来のスキーマ警告など、接続や統合の失敗要因を確認できる。
- 2026-05-06 取り込み分では `ERR_ADDRESS_UNREACHABLE` と `ENOTFOUND api../.github.com` により、トークン取得や `getAllSessions` が連鎖的に失敗していた。接続性の悪化を示す運用証跡として有用。
- 一方で、ユーザー/アシスタントの往復本文はこのログだけでは十分に復元できないため、経験抽出より運用トラブルの証跡向きである。

## 関連テーマ

- [[observability]]
- [[mcp]]
- [[git]]

## 出典

- `.wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/2026-05-05-copilot-session-20260505t194454-window1.md`
- `.wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/2026-05-05-copilot-session-20260505t194454-window2.md`
- `.wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/2026-05-02-copilot-session-20260502t045136-window2.md`
- `.wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/copilot-2026-05-06-cae269c6.md`
- `.wiki/topics/wiki/topicswiki/topics/wiki/topicswiki/topics/../60_Resources/copilot-2026-05-05-6aeba88b.md`
