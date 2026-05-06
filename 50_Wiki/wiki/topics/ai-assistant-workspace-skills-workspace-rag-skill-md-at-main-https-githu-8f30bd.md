---
title: "ai-assistant-workspace/skills/workspace-rag/SKILL.md at main"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ai-assistant-workspaceskillsworkspace-ragSKILL.md at main.md"
summary: "`workspace-rag`は、ワークスペース内のファイルをベクトル検索するための軽量なスキルです。SQLiteと`multilingual-e5`モデ…"
---

# ai-assistant-workspace/skills/workspace-rag/SKILL.md at main

## 概要

`workspace-rag`は、ワークスペース内のファイルをベクトル検索するための軽量なスキルです。SQLiteと`multilingual-e5`モデルを組み合わせ、高速な検索と関連度スコア付きの回答生成（R²AG簡易版）を実現します。

## 主要なトピック


## 詳細

- `workspace-rag`は、ワークスペース内のファイルをベクトル検索するための軽量なスキルです。SQLiteと`multilingual-e5`モデルを組み合わせ、高速な検索と関連度スコア付きの回答生成（R²AG簡易版）を実現します。
- 主な特徴
- **軽量設計**: SQLiteを使用し、外部DB不要で単一ファイルで管理。
- **インデックス機能**: 差分更新により、変更のあったファイルのみを効率的に処理。
- **高度な検索**: ベクトル検索とFTS5（キーワード検索）のハイブリッド構成。
- **R²AG対応**: 検索結果に関連度スコアを付与し、LLMが重要性を判断しやすい形式で出力。
- 利用のポイント
- **実行フロー**: セットアップ後にインデックスを作成し、サーバーまたはCLIから検索を行う。
- **検索モード**: 用途に応じて`hybrid`（デフォルト）、`vector`（意味重視）、`keyword`（単語重視）を使い分ける。

## 関連テーマ


## 出典

- `60_Resources/ai-assistant-workspaceskillsworkspace-ragSKILL.md at main.md`
- https://github.com/karaage0703/ai-assistant-workspace/blob/main/skills/workspace-rag/SKILL.md
