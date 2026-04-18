---
title: "task-03: 軽量カンバン Web UI の実装"
status: Todo
tags: [task, ai-agent, ui, python]
related:
  - "[[AI分析/AI活用事例まとめ]]"
  - "[[AI分析/改善案・拡張要件リスト]]"
  - "[[AI分析/タスク/task-02-SQLiteタスクキュー]]"
---

# task-03: 軽量カンバン Web UI の実装

> **対応要件**: [[AI分析/改善案・拡張要件リスト#REQ-03]]

---

## 目的

SQLite タスクキューの内容を可視化する**読み取り専用カンバンボード**を Python `http.server` で実装する。人間が翌朝ブラウザで確認し、状態変更のみ操作できる設計にする。

---

## コンテキスト

- 参考: [GMOペパボ — Python http.server + SQLite の軽量ダッシュボード](https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop)
- 外部依存を最小限に（Flask 不使用、標準ライブラリのみ）
- 読み取り専用（書き込みは状態変更 API のみ）
- 前提: [[AI分析/タスク/task-02-SQLiteタスクキュー]] が完了していること

---

## 実装指示

`sandbox/ui/` ディレクトリに以下を実装してください。

### 1. ファイル構成

```
sandbox/ui/
  server.py          # http.server サブクラス
  index.html         # カンバンボード（インライン CSS/JS）
  start.sh           # サーバー起動スクリプト
```

### 2. `server.py` の実装方針

- `http.server.BaseHTTPRequestHandler` を継承
- GET `/` → `index.html` を返す
- GET `/api/tasks` → SQLite から全タスクを JSON で返す（ステータス別）
- PATCH `/api/tasks/<id>/status` → `waiting` への変更のみ許可（Human-in-the-loop）
- PATCH `/api/tasks/<id>/priority` → 優先度変更のみ許可
- 上記以外の書き込みリクエストは `403 Forbidden`

### 3. `index.html` のカンバンレイアウト

```
┌─────────────┬──────────────┬──────────┬──────────┬──────────┐
│    Todo     │ In Progress  │  Done    │  Failed  │ Waiting  │
├─────────────┼──────────────┼──────────┼──────────┼──────────┤
│ [🔴高] タスクA│ [🟡中] タスクB│[✅] タスクC│[❌] タスクD│[⏸] タスクE│
│ source: gh  │ source: obs  │          │          │          │
│ [待機にする] │              │          │[再試行]  │[再開]    │
└─────────────┴──────────────┴──────────┴──────────┴──────────┘
```

**必要な表示要素**
- タスクタイトル・ソースバッジ（GitHub / Obsidian / cron）
- 優先度カラーリング（🔴1・🟠2・🟡3・🟢4・⚪5）
- `result` フィールドのサマリー表示（done/failed タスク）
- `skill_ref` がある場合はリンク表示
- 作成日時・完了日時

**操作ボタン（最小限）**
- 「待機にする」ボタン（todo/in_progress → waiting）
- 「優先度変更」ドロップダウン
- 「再試行」ボタン（failed → todo）

### 4. 自動リフレッシュ

```javascript
// 30秒ごとに /api/tasks をポーリングして DOM を更新
// 新規タスクが追加された場合にブラウザ通知（Notifications API）
```

### 5. `start.sh`

```bash
#!/bin/bash
PORT=${PORT:-8080}
echo "カンバンUI起動: http://localhost:$PORT"
cd "$(dirname "$0")" && python server.py $PORT
```

---

## 受け入れ条件

- [ ] `python ui/server.py` でサーバーが起動すること
- [ ] ブラウザでカンバンビューが表示されること
- [ ] ステータス別にカラムが分かれて表示されること
- [ ] ソースバッジ・優先度カラーが正しく表示されること
- [ ] 「待機にする」ボタンで SQLite が更新されること
- [ ] 許可外の書き込みリクエストが 403 を返すこと
- [ ] 30 秒ごとに自動更新されること
- [ ] 標準ライブラリのみ使用（`pip install` 不要）

---

## 参考リンク

- [Claude Code を夜間に走らせ、朝カンバンで拾う](https://zenn.dev/pepabo/articles/claude-code-night-autopilot-kanban-loop)
- [[AI分析/タスク/task-02-SQLiteタスクキュー]]
- [[AI分析/タスク/task-01-夜間自動化基盤]]
