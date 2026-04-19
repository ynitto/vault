---
original_source: 00_Inbox/Clippings/AIエージェントのスキルを自己改善させるOSSを作った.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, misc, 2026-04]
---

---
title: "AIエージェントのスキルを自己改善させるOSSを作った"
source: "https://zenn.dev/adalocamp/articles/agent-skill-bus"
author:
published: 2026-03-20
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
AIエージェントの運用現場で直面する「スキルの劣化」「タスク競合」「自己改善の欠如」という課題を解決するため、開発者が作成したOSS『**agent-skill-bus**』の紹介記事。

### 要点
- **開発の背景**
  - 42個のAIエージェントを1年間本番運用する中で発生した、静かなスキル劣化（API変更やモデル変化による品質低下）や競合問題に対応するために開発。

- **agent-skill-bus の3つの主要機能**
  - **Prompt Request Bus**: JSONLベースのタスクキュー。ファイルレベルのロックと依存関係（DAG）解決機能を提供。
  - **Self-Improving Skills**: 品質モニタリングを通じた自己改善ループ。閾値割れを検知し、原因分析・修復案生成・適用までを自動化。
  - **Knowledge Watcher**: パッケージや外部APIの変更を監視し、変化があれば自動的に修復タスクをキューへ投入。

- **技術的こだわり**
  - **依存ゼロ**: 特定のフレームワークやインフラに縛られない設計。Node.js環境であれば、シェルスクリプトやPython製などあらゆるエージェントと連携可能。

- **実績・展望**
  - 公開3日で35スターを獲得。
  - 今後は型定義の強化や、既存フレームワーク（LangGraph/CrewAI/AutoGen）との比較情報の拡充を予定。