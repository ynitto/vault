---
title: "task-07: GitHub Actions × Claude Code Action の設定"
status: Todo
tags: [task, ai-agent, github-actions, ci-cd]
related:
  - "[[AI分析/AI活用事例まとめ]]"
  - "[[AI分析/改善案・拡張要件リスト]]"
  - "[[AI分析/タスク/task-01-夜間自動化基盤]]"
  - "[[AI分析/タスク/task-02-SQLiteタスクキュー]]"
---

# task-07: GitHub Actions × Claude Code Action の設定

> **対応要件**: [[AI分析/改善案・拡張要件リスト#REQ-07]]

---

## 目的

GitHub Issues をトリガーに Claude Code が自動でコード改善・テスト追加・PR 作成を行うワークフローを構築する。深夜に Issue を自動作成するバッチも合わせて実装し、翌朝には PR がレビュー可能な状態になる体制を整える。

---

## コンテキスト

- 参考: [GMOペパボ — GitHub Actions × Claude Code Action](https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop)
- 参考: [Claude Code Action v1 移行ガイド](https://zenn.dev/pepabo/articles/eccb58b794176f)
- 対象リポジトリ: `sandbox`（または対象プロジェクトリポジトリ）
- 前提: Anthropic API キーが GitHub Secrets に設定されていること

---

## 実装指示

### 1. Claude Code Action ワークフロー `.github/workflows/claude-code.yml`

```yaml
name: Claude Code Action

on:
  issues:
    types: [labeled]

jobs:
  claude:
    if: contains(github.event.issue.labels.*.name, 'claude')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write

    steps:
      - uses: actions/checkout@v4

      - name: Run Claude Code Action
        uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # Issue の本文をタスクとして渡す
          prompt: |
            以下の Issue を解決してください。
            変更後は必ずテストを実行して通ることを確認してください。
            ${{ github.event.issue.body }}

      - name: Post result to Obsidian queue
        if: success()
        run: |
          # PR 作成後に SQLite タスクキューに完了通知を投入
          python sandbox/obsidian/notify_completion.py \
            --issue-number ${{ github.event.issue.number }} \
            --pr-url "${{ steps.claude.outputs.pr_url }}"
        env:
          TASK_QUEUE_DB: ${{ secrets.TASK_QUEUE_DB_PATH }}
```

### 2. 夜間 Issue 自動作成 `.github/workflows/nightly-issues.yml`

```yaml
name: Nightly Task Creation

on:
  schedule:
    - cron: '0 2 * * *'   # 毎日 深夜2時（JST 11時）
  workflow_dispatch:        # 手動実行も可能

jobs:
  create-issues:
    runs-on: ubuntu-latest
    permissions:
      issues: write

    steps:
      - uses: actions/checkout@v4

      - name: Create nightly improvement issues
        run: python .github/scripts/create_nightly_issues.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 3. Issue 自動作成スクリプト `.github/scripts/create_nightly_issues.py`

以下のタスクカテゴリから毎夜ランダム/ローテーションで Issue を作成してください:

```python
NIGHTLY_TASKS = [
    {
        "title": "[自動] テストカバレッジの改善",
        "body": "カバレッジが低いモジュールにユニットテストを追加してください。\n目標: カバレッジ 80% 以上",
        "labels": ["claude", "testing", "nightly"]
    },
    {
        "title": "[自動] 型ヒントの追加",
        "body": "型ヒントが不足している関数・メソッドに型アノテーションを追加してください。",
        "labels": ["claude", "refactoring", "nightly"]
    },
    {
        "title": "[自動] ドキュメント更新",
        "body": "最近変更されたモジュールの docstring を最新の実装に合わせて更新してください。",
        "labels": ["claude", "documentation", "nightly"]
    },
]

# 同じタスクが連続しないよう、直近7日の Issue タイトルを確認してスキップ
```

### 4. PR コメントテンプレート `.github/PULL_REQUEST_TEMPLATE/claude_code.md`

```markdown
## 🤖 Claude Code 自動実行レポート

**元 Issue**: #{{ issue_number }}
**実行時間**: {{ duration }}
**変更ファイル数**: {{ changed_files }}

### 変更サマリー
{{ summary }}

### テスト結果
{{ test_results }}

### レビューのポイント
{{ review_hints }}

---
> このPRは Claude Code Action によって自動生成されました。
> 内容を確認し、問題なければマージしてください。
```

---

## 受け入れ条件

- [ ] `claude` ラベルを付けた Issue で Claude Code Action が起動すること
- [ ] 実行後に PR が自動作成されること
- [ ] PR に実行サマリーコメントが投稿されること
- [ ] 夜間 cron で Issue が自動作成されること（UTC 2:00 = JST 11:00）
- [ ] 同一タスクが連続して作成されないこと
- [ ] 実行コスト（API 使用量）がログに記録されること
- [ ] 失敗時に Issue にエラーコメントが投稿されること

---

## 参考リンク

- [Claude Code を夜間に走らせ、朝カンバンで拾う](https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop)
- [Claude Code Action v1 移行ガイド](https://zenn.dev/pepabo/articles/eccb58b794176f)
- [Claude Code Action GitHub](https://github.com/anthropics/claude-code-action)
- [[AI分析/タスク/task-01-夜間自動化基盤]]
- [[AI分析/タスク/task-02-SQLiteタスクキュー]]
