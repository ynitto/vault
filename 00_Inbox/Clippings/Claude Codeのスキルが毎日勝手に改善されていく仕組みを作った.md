---
title: "Claude Codeのスキルが毎日勝手に改善されていく仕組みを作った"
source: "https://zenn.dev/sonicgarden/articles/claude-code-self-improving-loop"
author:
published: 2026-05-24
created: 2026-05-31
description:
tags:
  - "clippings"
---
### 要約
Claude Codeの「Routines」機能を活用し、開発ワークフローを自動的に改善する自己循環型システムの構築事例。会話履歴から課題（Signal）を抽出し、自動でIssue起票・修正・PR作成までを行うことで、継続的なスキル改善を実現している。

### 自動改善ループの仕組み
1. **発見 (Discovery)**
   - ローカルでの開発終了後、会話履歴（jsonl）から「うまくいかなかったSignal」を抽出。
   - 課題をGitHub Issuesへ自動起票。

2. **判定・適用 (Triage)**
   - 別途用意した「dev-workflow-triage」スキルがIssueを精査。
   - 承認された場合、スキル定義書（SKILL.md）を修正しPRを作成。

3. **無人運転 (Routines)**
   - 上記のTriageプロセスを1日1回実行し、CI/CD的な自己改善フローを構築。

### 運用のポイント
- **品質ゲートの設置**: 以下の3段構えで安全性を担保。
  - **verify-diff**: 意図通りに変更されたかの検証。
  - **skill-review**: ベストプラクティスに基づく記述の最適化。
  - **publicity-review**: 情報漏洩（クレデンシャル等）の防止。
- **人間による最終確認**: PRレビュー・マージは人間が行い、意図しない自動コミットを防ぐ。
- **ハマりどころの克服**: サブスキルが完結扱いされる問題への対応（JSONでの応答など）や、無人環境特有のツール制限への対策が重要。
