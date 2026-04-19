---
title: ObsidianとClaudeではじめる日々のタスク管理と振り返り術
source: https://qiita.com/inamuu/items/d9b013b54a31a78e9c13
author:
- '[[inamuu]]'
published: 2025-12-20
created: 2026-04-19
description: はじめに みなさん、生成AI使ってますか？ 私ももちろん使っています。 コードの調査やちょっとしたサマリーを出して概要を掴んだり、今までネットサーフィンして培ってきたあのGoogle先生との対話力が今や不要な能力となりつつあります。
  そんななか、生成AIはとても便利ですが...
tags:
- resource/web
- obsidian
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/ObsidianとClaudeではじめる日々のタスク管理と振り返り術 1.md
copied_at: 2026-04-19 10:51:13+09:00
---
# ObsidianとClaudeCodeによるタスク管理と振り返り術

## 概要
ObsidianとClaudeCodeを連携させ、日々のタスク管理と週次・半期の振り返りを効率化する方法を解説。

## 使用ツール
*   **Obsidian**
    *   デイリーノート、テンプレート機能
    *   KANBANプラグイン (Backlog, InProgress, InReview, Doneレーン)
*   **ClaudeCode**
    *   カスタムコマンド

## 準備と設定
1.  **Obsidianデイリーノート**: `02.Daily/`に日次ファイルを作成。`Daily.md`テンプレートでメタデータを設定。
2.  **KANBANプラグイン**: ToDoの投入場所として活用。
3.  **タグ管理**: タスクに`#pj_プロジェクト名`のようなタグを付与し、プロジェクトフォルダと紐付けてタスクを分類。

## 日々のワークフロー
1.  朝、KANBANのBacklogから今日のタスクをInProgressに移動。
2.  ClaudeCodeのカスタムコマンド `/list-tasks` を実行し、Dailyノートにタスクをプロジェクトごとにまとめて出力。
3.  タスクはMarkdownの拡張チェックボックス (`-[x]`, `-[R]`, `-[ ]`) でステータスを管理。

## 振り返り
*   **週次**: ClaudeCodeカスタムコマンド `/summary-weeks` で週のタスクをサマリー。
*   **半期**: ClaudeCodeに期間を指定して、完了タスクをサマリーさせ、目標結果の参考に利用。

## メリット
*   コンテキストスイッチの削減
*   効率的なタスク管理
*   振り返り作業の簡素化