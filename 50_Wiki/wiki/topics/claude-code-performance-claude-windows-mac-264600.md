---
title: "Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った"
type: "topic"
tags:
  - "claude-code"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った.md"
summary: "本記事は、マルチデバイス（Windows/Mac）環境でClaude Codeの「長期記憶」を同期するための自作システムについての解説です。SQLiteを…"
---

# Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った

## 概要

本記事は、マルチデバイス（Windows/Mac）環境でClaude Codeの「長期記憶」を同期するための自作システムについての解説です。SQLiteをローカルキャッシュ、JSONLをGit管理の正本とすることで、マシン間でのメモリ同期と競合回避を実現しています。

*発行: 2026-03-24 / [[claude-code-performance-claude-windows-mac-264600]]*

## 主要なトピック

- [[claude-code]]
- [[performance]]

## 詳細

- 本記事は、マルチデバイス（Windows/Mac）環境でClaude Codeの「長期記憶」を同期するための自作システムについての解説です。SQLiteをローカルキャッシュ、JSONLをGit管理の正本とすることで、マシン間でのメモリ同期と競合回避を実現しています。
- 主要なポイント
- **課題:** マシン間でClaude Codeの会話文脈（設計判断など）を共有できない効率の悪さを解消したい。
- **設計思想:**
- **SQLite + JSONL:** SQLiteはローカルキャッシュとし、実体はGitで管理するマシン別のJSONLファイルとする。
- **競合回避:** マシンごとにJSONLファイルを分けることで、Gitのコンフリクトを完全に回避。
- **高速化:** 埋め込みベクトルをJSONLに保存し、セッション開始時のモデルロードを不要にする。
- **検索エンジン:**
- FTS5（キーワード）とベクトル検索をRRF（Reciprocal Rank Fusion）で統合。

*発行: 2026-03-24 / [[claude-code-performance-claude-windows-mac-264600]]*

## 関連テーマ

- [[claude-code]]
- [[performance]]

## 出典

- `60_Resources/Claude Codeの長期記憶をWindowsとMacで共有する仕組みを作った.md`
- https://zenn.dev/aoi_umigishi/articles/fc877d2d7d3e38
