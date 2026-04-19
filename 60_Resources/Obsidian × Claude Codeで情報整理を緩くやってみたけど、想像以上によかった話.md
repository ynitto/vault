---
original_source: 00_Inbox/Clippings/Obsidian × Claude Codeで情報整理を緩くやってみたけど、想像以上によかった話.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, obsidian, ai-agent, 2026-04]
---

---
title: "Obsidian × Claude Codeで情報整理を緩くやってみたけど、想像以上によかった話"
source: "https://zenn.dev/stafes_blog/articles/d7457519a2daec"
author:
published: 2025-12-11
created: 2026-04-19
description:
tags:
  - "clippings"
---
# Obsidian × Claude Code による情報整理

## 概要
日々の散らばったタスクや情報の整理を改善するため、ObsidianとClaude Codeを連携させた情報整理システムを導入。思った以上の効果を実感。

## 背景
*   組織横断プロジェクトや多数のタスクにより、情報が散らばり、既存のタスク管理が機能しなくなっていた。
*   ゆるくタスク管理と情報整理ができる仕組みを求めていた。

## 導入システム
### 全体像
Obsidian、Notion、GoogleカレンダーのデータをClaude Codeが連携・整理する。

### 各ツールの役割
*   **Obsidian**: メモツール。
    *   Thinoプラグインで小さなタスクや感情メモを気軽に記録。
    *   TerminalプラグインでClaude Codeを実行。
*   **Claude Code**: AIアシスタント。
    *   Notion MCP、Googleカレンダー MCPと連携し、データにアクセス。
    *   Obsidianのファイルも直接参照。
    *   情報整理、タスク化、サマリー作成などを担当。
*   **Notion**: タスク管理ツール。
    *   カンバン方式（未着手、進行中、完了、ペンディング）。
    *   Slackと連携し、タスクをボードに追加。

## 活用方法
1.  **毎朝のタスク整理**: 
    *   Claude Codeコマンド一発で、Googleカレンダーの予定、Notionの優先タスク、前日のObsidianメモから「今日のノート」を自動生成。
    *   前日のサマリーも含まれ、振り返りながらタスクに取り組める。
2.  **週末の週報作成**: 
    *   週の最後にClaude Codeがデイリーノートを基に週報を自動生成。
    *   内容を自身で調整し、週初めに読み返すことで振り返りと行動整理に活用。

## 振り返り
*   **脳の負担軽減**: 必要な情報が自動的にまとまるため、認知負荷が大幅に減少。
*   **習慣化のしやすさ**: 簡単な指示で実行でき、継続しやすい。
*   **メモのハードル低下**: 体裁やタグ整理をAIに任せられるため、メモを書く行為自体の負担が減り、情報蓄積が進む。
*   AIの活用により、日々の業務がより楽に効率的になったことを実感。