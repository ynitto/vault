---
title: "task-01: 夜間自動化基盤の構築"
status: Done
tags: [task, ai-agent, automation]
related:
  - "[[AI分析/AI活用事例まとめ]]"
  - "[[AI分析/改善案・拡張要件リスト]]"
  - "[[AI分析/タスク/task-02-SQLiteタスクキュー]]"
---

# task-01: 夜間自動化基盤の構築

> **対応要件**: [[AI分析/改善案・拡張要件リスト#REQ-01]]
> **ステータス**: ✅ Done — `sandbox/tools/kiro-loop` にて実装済み

---

## 目的

Claude Code（または Kiro）を夜間に自動起動し、SQLite タスクキューに積まれたタスクを自律的に処理するパイプラインの基盤を構築する。人間が翌朝カンバンで結果を確認できる体制を整える。

---

## コンテキスト

- 参考実装: [GMOペパボの Claude Code 夜間自走パイプライン](https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop)
- 現在の状態: Kiro へのタスク送信は手動（Obsidian の Shell コマンドボタン経由）
- 目標: cron または Claude Code Routines で深夜 2〜4 時に自動実行
- 前提: [[AI分析/タスク/task-02-SQLiteタスクキュー]] が完了していること

---

## 実装指示

以下を `sandbox` リポジトリに実装してください。

### 1. ディレクトリ構造の作成

```
sandbox/
  automation/
    run_nightly.sh       # メイン実行スクリプト
    task_runner.py       # タスクキューからタスクを取得して実行
    config.yaml          # 設定ファイル（実行時間・最大タスク数など）
    logs/                # 実行ログ（.gitignore 対象）
```

### 2. `run_nightly.sh` の実装

```bash
#!/bin/bash
# SQLite タスクキューから Todo タスクを取得し claude/kiro に渡す
# 最大実行タスク数: config.yaml の max_tasks_per_run に従う
# ログは logs/YYYY-MM-DD.log に出力
# 失敗タスクは status=failed に更新してスキップ
```

### 3. cron 設定

```cron
0 2 * * * /path/to/sandbox/automation/run_nightly.sh >> /path/to/logs/cron.log 2>&1
```

### 4. config.yaml の実装

```yaml
schedule:
  hour: 2
  max_tasks_per_run: 10
  timeout_per_task_minutes: 30

sources:
  - obsidian_vault  # Obsidian カンバンからのタスク
  - github_issues   # GitHub Issues からのタスク

notifications:
  on_complete: true   # 完了時に SQLite に結果を書き込む
  on_failure: true
```

### 5. `task_runner.py` の実装

- SQLite から `status=todo` のタスクを優先度順に取得
- 1 タスクずつ claude/kiro CLI に渡して実行
- 実行結果（成功/失敗/スキップ）を SQLite に書き戻す
- タイムアウト（設定値）を超えたタスクは `failed` に設定
- 実行中は `status=in_progress` に更新

---

## 受け入れ条件

- [ ] `run_nightly.sh` を手動実行してタスクが処理されること
- [ ] 処理結果が SQLite に正しく反映されること
- [ ] ログファイルに実行詳細が記録されること
- [ ] cron で深夜に自動起動されること（動作確認は手動実行で代替可）
- [ ] タイムアウト・エラー時にもプロセスが止まらず次のタスクに進むこと

---

## 参考リンク

- [Claude Code を夜間に走らせ、朝カンバンで拾う](https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop)
- [Claude Code Routines 公式ドキュメント](https://code.claude.com/docs/en/routines)
- [[AI分析/タスク/task-02-SQLiteタスクキュー]]
- [[AI分析/タスク/task-03-カンバンWebUI]]
