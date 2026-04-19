---
title: "task-06: Obsidian ↔ Kiro 連携の強化"
status: done
tags:
  - task
  - ai-agent
  - obsidian
  - kiro
  - integration
related:
  - "[[AI活用事例まとめ]]"
  - "[[改善案・拡張要件リスト]]"
  - "[[2026-04-18-SQLiteタスクキュー]]"
  - "[[2026-04-18-スキル記憶システム]]"
---

# task-06: Obsidian ↔ Kiro 連携の強化

> **対応要件**: [[改善案・拡張要件リスト#REQ-06]]

---

## 目的

現在の `kanban_task.md` テンプレートの「Send to Kiro」ボタンを起点に、**タスク自動分類・実行結果書き戻し・スキルリンク追加**までを一貫した連携フローとして強化する。

---

## コンテキスト

- 現状: Obsidian の Shell コマンドで Kiro にタスクを手動送信するだけ
- 参照: vault の `_Templates/kanban_task.md`（Kiro 送信ボタン実装済み）
- 目標: タスク作成 → 自動分類 → Kiro 実行 → 結果書き戻し → スキルリンク追加の自動化
- 前提: [[2026-04-18-SQLiteタスクキュー]] の TaskQueue が利用可能であること

---

## 実装指示

`sandbox/obsidian/` ディレクトリに以下を実装してください。

### 1. タスク自動分類スクリプト `classify_task.py`

Obsidian から送信されるタスクを LLM で分類し、SQLite に登録する。

```python
def classify_and_enqueue(task_file_path: str) -> str:
    """
    Obsidian の kanban_task.md を読み込み:
    1. タイトル・本文を抽出
    2. LLM でカテゴリ・優先度・タグを推定
    3. TaskQueue に登録（source='obsidian'）
    4. タスクファイルのフロントマターを更新（task_id, status, priority）
    5. タスク ID を返す
    """
```

**LLM 分類プロンプト** (`prompts/classify_task.md`):
```
タスクの内容からカテゴリと優先度を判断してください。
タイトル: {title}
内容: {body}

JSON で回答:
{
  "category": "code_review|refactoring|testing|deployment|research|other",
  "priority": 1-5,
  "tags": ["tag1", "tag2"],
  "suggested_skill": "適用可能な既存スキル名 or null"
}
```

### 2. 結果書き戻しスクリプト `write_back_result.py`

Kiro / Claude Code の実行完了後、結果を Obsidian ノートに書き戻す。

```python
def write_back_to_obsidian(task_id: str, vault_path: str):
    """
    SQLite から task_id の result, skill_ref, status を取得し:
    1. 対応する kanban_task.md の「## メモ」セクションに result を追記
    2. 受け入れ条件チェックボックスを LLM で自動評価・更新
    3. skill_ref があれば「## 参考スキル」セクションに [[wikiリンク]] を追加
    4. フロントマターの status を更新（Todo → Done）
    5. 完了タスクを Archive/ フォルダへ移動
    """
```

### 3. `kanban_task.md` テンプレートの更新

既存テンプレートを以下のように拡張してください（`_Templates/kanban_task.md` を更新）:

```markdown
---
title: <% tp.file.title %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
status: Todo
priority: 2
category:
task_id:
tags: [task]
---

```button
name 🤖 Send to Kiro
type command
action Shell commands: Send to Kiro
color blue
```

```button
name 📋 分類して登録
type command
action Shell commands: Classify and Enqueue
color green
```

## タスク概要
<% tp.system.prompt("タスク内容を入力") %>

## 受け入れ条件
- [ ] 

## 参考スキル
<!-- 自動追記: 関連スキルへの [[wikiリンク]] -->

## 実行結果
<!-- 自動追記: Kiro 実行後に write_back_result.py が追記 -->

## メモ

## Git情報
```git-manager
show: all
```
```

### 4. Shell コマンド設定（Obsidian Shell Commands プラグイン）

以下の 2 つのコマンドを追加してください:

```bash
# "Classify and Enqueue"
python /path/to/sandbox/obsidian/classify_task.py "{{file_path}}"

# "Sync Result from Queue"（結果書き戻し）
python /path/to/sandbox/obsidian/write_back_result.py "{{frontmatter:task_id}}" "{{vault_path}}"
```

---

## 受け入れ条件

- [ ] 「分類して登録」ボタンでタスクが SQLite に登録されること
- [ ] フロントマターの `task_id`, `priority`, `category` が自動更新されること
- [ ] 実行完了後に「## 実行結果」セクションに結果が書き戻されること
- [ ] 受け入れ条件チェックボックスが自動評価されること
- [ ] `skill_ref` があれば「## 参考スキル」に `[[wikiリンク]]` が追加されること
- [ ] 完了タスクが `Archive/` フォルダに移動されること
- [ ] テンプレートが Obsidian で正しく動作すること

---

## 参考リンク

- [ぼくの Obsidian](https://qiita.com/yaskitie/items/b48a064cb0c6e673bd42)
- [Kiro Autonomous Agent](https://kiro.dev/docs/autonomous-agent/github/)
- [[2026-04-18-SQLiteタスクキュー]]
- [[2026-04-18-スキル記憶システム]]
