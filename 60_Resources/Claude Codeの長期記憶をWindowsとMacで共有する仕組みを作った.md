---
original_source: 00_Inbox/Clippings/Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, windows, 2026-04]
---

---
title: "Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った"
source: "https://zenn.dev/aoi_umigishi/articles/fc877d2d7d3e38"
author:
published: 2026-03-24
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 要約
本記事は、マルチデバイス（Windows/Mac）環境でClaude Codeの「長期記憶」を同期するための自作システムについての解説です。SQLiteをローカルキャッシュ、JSONLをGit管理の正本とすることで、マシン間でのメモリ同期と競合回避を実現しています。

### 主要なポイント
- **課題:** マシン間でClaude Codeの会話文脈（設計判断など）を共有できない効率の悪さを解消したい。
- **設計思想:**
  - **SQLite + JSONL:** SQLiteはローカルキャッシュとし、実体はGitで管理するマシン別のJSONLファイルとする。
  - **競合回避:** マシンごとにJSONLファイルを分けることで、Gitのコンフリクトを完全に回避。
  - **高速化:** 埋め込みベクトルをJSONLに保存し、セッション開始時のモデルロードを不要にする。
- **検索エンジン:**
  - FTS5（キーワード）とベクトル検索をRRF（Reciprocal Rank Fusion）で統合。
  - 時間減衰（半減期30日）を適用し、直近の文脈を優先。
- **運用:**
  - Claude CodeのHook（SessionStart/Stop）を活用し、自動保存・自動同期を実現。
  - 必要な時だけ「Skill」として過去の記憶を検索・注入することでトークンを節約。