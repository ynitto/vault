---
title: "Claude Code Hooks × markitdown で非MDファイルを透過的にMarkdown変換する"
type: "topic"
tags:
  - "claude-code"
  - "obsidian"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Claude Code Hooks × markitdown で非MDファイルを透過的にMarkdown変換する.md"
summary: "Claude Code の `PreToolUse Hook` と Microsoft の `markitdown` を活用し、PDFやOfficeファイ…"
---

# Claude Code Hooks × markitdown で非MDファイルを透過的にMarkdown変換する

## 概要

Claude Code の `PreToolUse Hook` と Microsoft の `markitdown` を活用し、PDFやOfficeファイルなどの非Markdownファイルを、AIの読み込み時に自動でMarkdownへ透過変換する仕組みの構築手法。

*発行: 2026-04-23 / [[claude-code-obsidian-claude-hooks-markitdown-86362e]]*

## 主要なトピック

- [[claude-code]]
- [[obsidian]]

## 詳細

- Claude Code の `PreToolUse Hook` と Microsoft の `markitdown` を活用し、PDFやOfficeファイルなどの非Markdownファイルを、AIの読み込み時に自動でMarkdownへ透過変換する仕組みの構築手法。
- 要点まとめ
- **透過的変換の仕組み**: `PreToolUse Hook` でファイルの読み込みをフックし、`updatedInput` を通じてファイルパスを変換後の `.md` ファイルへ書き換えることで、LLMは変換の有無を意識せずに内容を閲覧可能。
- **markitdownの活用**: `markitdown` CLIを使用してPDF、PPTX、XLSX、HTMLなどをMarkdownへ変換。
- **効率化**: 変換済みファイルと元のファイルの更新日時（mtime）を比較し、キャッシュを利用することで再変換を抑制。
- **実装のヒント**:
- **Windows対応**: 日本語ファイル名対策として `PYTHONUTF8=1` を環境変数に追加。
- **スキル連携**: `/wiki` コマンド等とシームレスに連携させるため、キャッシュファイルの除外ルールなどを設定。
- **成果**: 複雑な処理をアダプター層として隠蔽でき、ナレッジベース（Obsidian等）のインジェスト作業が大幅に効率化された。

*発行: 2026-04-23 / [[claude-code-obsidian-claude-hooks-markitdown-86362e]]*

## 関連テーマ

- [[claude-code]]
- [[obsidian]]

## 出典

- `../60_Resources/Claude Code Hooks × markitdown で非MDファイルを透過的にMarkdown変換する.md`
- https://zenn.dev/tuzuminami/articles/e487adfd650289
