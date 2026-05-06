---
title: "Claude Code・Codex・Gemini の会話ログを日次Markdownとして自動整理する ― chat_logs から LLM_history を自動生成する仕組み"
source: "https://qiita.com/rxg03350/items/9bd822a2be5549b17878"
author:
  - "[[rxg03350]]"
published: 2026-03-08
created: 2026-05-07
description: "はじめに Claude Code、Codex、Gemini を併用していると、あとから「あの日どのツールで何を相談したか」を追いたくなる場面が増えます。 ただし実際のログは、ツールごとに保存形式も保存場所も違います。 Codex は JSONL ベース Claude C..."
tags:
  - "clippings"
---
### 概要
複数のAIツール（Claude Code, Codex, Gemini）の会話ログを自動収集し、日次およびツール別のMarkdown形式の履歴として整理する自動化システムの構築方法です。

### 要点
- **課題解決**: 各ツールのログ形式や保存場所が異なるため、集約・正規化・可読性向上を自動化した。
- **システム構成**:
  - **chat_logs**: 元ログの差分保管用。
  - **SQLite**: ログの正規化、重複排除、管理用に使用。
  - **LLM_history**: 人が読むための整形済みMarkdown出力用。
- **自動化フロー**:
  - `update_llm_history.sh` ラッパースクリプトが差分収集とMarkdown生成を制御。
  - `cron` を利用し、毎日UTC 04:05に自動実行。
- **工夫点**:
  - **日次概要 + LLM別詳細**: 全体像の把握と詳細確認を両立する構成。
  - **疎結合設計**: 閲覧ルールを変更しても、元ログからMarkdownを再生成可能。
  - **運用効率化**: 不要な進捗通知やシステム指示を除外し、読みやすさを優先。
