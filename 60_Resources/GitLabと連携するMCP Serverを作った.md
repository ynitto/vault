---
title: GitLabと連携するMCP Serverを作った
source: https://zenn.dev/owayo/articles/e4c4496e6d79e7
author: null
published: 2025-03-20
created: 2026-04-19
description: null
tags:
- resource/web
- git
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/GitLabと連携するMCP Serverを作った.md
copied_at: 2026-04-19 10:51:13+09:00
---
### 概要
GitLabとAIアシスタント（Cursor/Claude）を連携させ、開発効率を向上させるための「GitLab MCP Server」の開発・導入方法を紹介する記事です。

### 主要機能
- **パイプライン修正**: 失敗したジョブのログを取得し、AIが原因分析・修正を行う。
- **MR指摘対応**: 未解決のMRコメントを取得し、修正をサポートする。
- **MRレビュー**: ローカルの最新状況（未コミット含む）とリモートの差分を比較し、AIがレビューを行う。

### 導入のポイント
- **ツール**: Python（uv）で動作。
- **準備**: GitLabアクセストークン（read_api権限）が必要。
- **設定**: Claude DesktopまたはCursorのMCP設定ファイルに接続情報を記述。

### 今後の課題
- ユーザーの意図に合わせて特定の機能だけを呼び出せるよう、実行制御を最適化したい。