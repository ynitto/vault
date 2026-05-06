---
title: "Kiro stopフック"
type: concept
tags: [kiro-cli, hooks, notification, productivity]
created: 2026-05-05
updated: 2026-05-05
sources:
  - "../60_Resources/Kiro CLIのstopフックで作業完了時に通知音を鳴らす.md"
summary: "Kiro CLIのエージェント応答完了時に自動実行されるhooks.stopを使った通知実装パターン。"
---

# Kiro stopフック

## 概要

Kiro CLIの `hooks.stop` フィールドに任意のスクリプトを指定することで、エージェントの応答完了時に確実に通知を実行できる仕組み。LLMの判断に依存せず、承認不要で動作する。

*発行: 2026-02-06*

## 詳細

### 3つのアプローチ比較

| アプローチ | 確実性 | 設定の柔軟性 |
|---|---|---|
| 組み込み通知 | 高 | 低（OS通知と混在） |
| steeringファイル | 低（LLM依存） | 中 |
| **stopフック（推奨）** | **高** | **高** |

### 実装手順（macOS）

1. 通知音スクリプト `notify.sh` を作成:
   ```bash
   #!/bin/bash
   afplay /System/Library/Sounds/Glass.aiff
   ```
2. Kiro設定ファイルの `hooks.stop` に指定:
   ```json
   { "hooks": { "stop": "/path/to/notify.sh" } }
   ```
3. スクリプト1箇所を変更するだけで全エージェントに反映される

### 活用場面

- 長時間タスク（kiro-loopの自律実行など）の完了検知
- 複数エージェント並列実行時の完了通知

## 関連

- [[ai-agent]]

## 出典

- `../60_Resources/Kiro CLIのstopフックで作業完了時に通知音を鳴らす.md`
