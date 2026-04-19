---
original_source: 00_Inbox/Clippings/Claude Code・Codex・Gemini の会話ログを日次Markdownとして自動整理する ― chat_logs から LLM_history を自動生成する仕組み.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, 2026-04]
---

---
title: "Claude Code・Codex・Gemini の会話ログを日次Markdownとして自動整理する ― chat_logs から LLM_history を自動生成する仕組み"
source: "https://qiita.com/rxg03350/items/9bd822a2be5549b17878"
author:
  - "[[rxg03350]]"
published: 2026-03-08
created: 2026-04-19
description: "はじめに Claude Code、Codex、Gemini を併用していると、あとから「あの日どのツールで何を相談したか」を追いたくなる場面が増えます。 ただし実際のログは、ツールごとに保存形式も保存場所も違います。 Codex は JSONL ベース Claude C..."
tags:
  - "clippings"
---
### 記事の要約
本記事は、Claude Code、Codex、Geminiといった複数のAIツールの会話ログを自動的に集約・整形し、振り返りやすいMarkdown形式で保存する運用手法の解説です。ログの散逸を防ぎ、日次での可読性を高めるための自動化システムを紹介しています。

### 重要なポイント
- **階層的なログ管理**: 生ログを保存する「chat_logs」と、人が閲覧するための「LLM_history」を分離し、柔軟性を確保。
- **SQLiteの活用**: ログの差分取り込み、正規化（不要イベント除外）、重複排除をSQLiteで一元管理することで、効率的な再生成を実現。
- **日次概要 + 詳細のハイブリッド構成**: 
    - `YYYY-MM-DD.md`: 1日の活動概要を俯瞰。
    - `YYYY-MM-DD.[ツール名].md`: 各ツールごとの詳細な会話記録を追跡。
- **自動化による運用**: cronを利用し、差分収集からMarkdown生成までを毎日自動実行することで、運用の手間を排除。
- **柔軟な拡張性**: 過去分の再生成（`--render-all`）や、週次サマリ、全文検索への拡張も視野に入れた設計。