---
title: spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる
source: https://zenn.dev/suusanex/articles/1bff51453b49ad
author: null
published: 2026-02-28
created: 2026-05-05
description: null
tags:
- clippings
- resource/web
- 2026-05
- copilot
- spec-kit
- workflow
original_source: 00_Inbox/Clippings/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 概要
AI開発支援ツール「spec-kit」において、「Plan（計画）」から「Tasks（実装タスク）」への移行時に発生しやすい実装漏れや設計の不整合を解消するため、両者の間に「粗いシーケンス図を作成するフェーズ」を追加する手法が提案されています。

### 要点
- **課題**: spec-kitのフローだけでは、ドメイン層の設計から実装への詳細化で、画面遷移やコンポーネント間の連携ロジックが抜け落ちやすい。
- **解決策**: 「arc42 Runtime View」と「C4モデル」の枠組みを導入し、PlanとTasksの間に「粗いシーケンス」を作る工程を挟む。
- **導入効果**:
    - AIの迷走や実装漏れが劇的に減少した。
    - ドキュメントが抽象的すぎず具体的すぎないため、人間によるコードレビューの精度が向上した。
- **実装方法**:
    - GitHub Copilot Agent（`runtime-evidence`）として定義し、既存のspec-kitのフロー（Plan → **Runtime View** → Tasks）に組み込む。
    - PlantUML等を用いて、全体像を可視化させる。
