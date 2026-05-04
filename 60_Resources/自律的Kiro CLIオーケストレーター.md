---
title: "自律的Kiro CLIオーケストレーター"
source: "https://www.reddit.com/r/kiroIDE/comments/1r4qv0k/autonomous_kiro_cli_orchestrator/?solution=bb2de1f292d514b8bb2de1f292d514b8&js_challenge=1&token=bbbe4bf1c9a2b5160829c4be34da586187f4db90805a814afb9ec8d4fb6199fd&jsc_orig_r=&tl=ja"
author:
  - "[[Humblebragger369]]"
published: 2026-02-15
created: 2026-05-03
original_source: 00_Inbox/Clippings/自律的Kiro CLIオーケストレーター.md
copied_at: 2026-05-03T19:37:17
tags: [resource/clipping, kiro, cli, orchestrator, autonomous, ai-agent, 2026-05]
---
### 自律的Kiro CLIオーケストレーターについて

投稿者は、以前紹介した自律的なCLIオーケストレーターをオープンソース化しました。

#### 主な特徴
- **仕様優先のアプローチ**: 従来のKiroの仕様重視の設計と、Claudeの自律的な機能を統合。
- **拡張性**: ローカルでの小規模タスク実行に加え、大規模仕様（60以上のタスク）にはEC2上での並列実行にも対応。
- **リポジトリ**: [GitHub - Bob-The-Builder](https://github.com/joshuakatt/Bob-The-Builder)

#### コミュニティの反応
- **高評価**: 実際に使用したユーザーから「バグを自動修正できた」など非常にポジティブなフィードバックを得ている。
- **改善案**: クレジット消費を抑えるために、レビュー頻度の調整や使用モデルの最適化（Haiku, Sonnet, Opusの使い分け）が提案されている。
