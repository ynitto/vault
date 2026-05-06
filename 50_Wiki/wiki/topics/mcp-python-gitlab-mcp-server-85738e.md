---
title: "GitLabと連携するMCP Serverを作った"
type: "topic"
tags:
  - "mcp"
  - "python"
  - "git"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/GitLabと連携するMCP Serverを作った.md"
summary: "GitLabとAIアシスタント（Cursor/Claude）を連携させ、開発効率を向上させるための「GitLab MCP Server」の開発・導入方法を…"
---

# GitLabと連携するMCP Serverを作った

## 概要

GitLabとAIアシスタント（Cursor/Claude）を連携させ、開発効率を向上させるための「GitLab MCP Server」の開発・導入方法を紹介する記事です。

*発行: 2025-03-20 / [[mcp-python-gitlab-mcp-server-85738e]]*

## 主要なトピック

- [[mcp]]
- [[python]]
- [[git]]
- [[code-review]]

## 詳細

- GitLabとAIアシスタント（Cursor/Claude）を連携させ、開発効率を向上させるための「GitLab MCP Server」の開発・導入方法を紹介する記事です。
- 主要機能
- **パイプライン修正**: 失敗したジョブのログを取得し、AIが原因分析・修正を行う。
- **MR指摘対応**: 未解決のMRコメントを取得し、修正をサポートする。
- **MRレビュー**: ローカルの最新状況（未コミット含む）とリモートの差分を比較し、AIがレビューを行う。
- 導入のポイント
- **ツール**: Python（uv）で動作。
- **準備**: GitLabアクセストークン（read_api権限）が必要。
- **設定**: Claude DesktopまたはCursorのMCP設定ファイルに接続情報を記述。

*発行: 2025-03-20 / [[mcp-python-gitlab-mcp-server-85738e]]*

## 関連テーマ

- [[mcp]]
- [[python]]
- [[git]]
- [[code-review]]

## 出典

- `60_Resources/GitLabと連携するMCP Serverを作った.md`
- https://zenn.dev/owayo/articles/e4c4496e6d79e7
