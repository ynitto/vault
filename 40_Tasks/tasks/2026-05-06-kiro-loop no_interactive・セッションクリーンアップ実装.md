---
task_id: 2026-05-06-kiro-loop no_interactive・セッションクリーンアップ実装
title: kiro-loop no_interactive・セッションクリーンアップ実装
created: 2026-05-06T07:24:46+09:00
status: none
urgency: 高
priority: 高
effort: M
tags: [task, kiro-loop, kiro-cli, tmux, harness, reliability]
source_daily: [[10_Daily/2026-05-06]]
---

```button
name 🤵 Task Assistant
type command
action Shell commands: Execute: Breakdown Task
color blue
```
```button
name 📝 Post Issue
type command
action Shell commands: Execute: Post Issue
color blue
```
```button
name 🤖 Send to Kiro
type command
action Shell commands: Execute: Send to Kiro
color blue
```

# kiro-loop no_interactive・セッションクリーンアップ実装

## 背景・目的
`kiro-loop` は並列実行や長時間運用の方向性が見えてきた一方、非インタラクティブ実行とセッションの後始末が未整理で、壊れた tmux / Kiro セッションが残りやすい。`no_interactive` と定期クリーンアップを実装し、セッション終了・削除・再生成の流れを固定することで、長時間実行ハーネスとしての安定性を上げる。

## 条件
### 前提条件
- `kiro-loop` の設定ファイルと tmux / kiro-cli の起動フローを確認できること
- `kiro-cli` のセッション保存・終了・削除コマンドの挙動を把握できること
- 既存の `kiro-loop` 設計メモを参照できること

### 制約条件
- ユーザーの対話セッションを誤って終了しないよう、異常終了時と明示的 quit を区別する
- `kiro-cli` v1 / v2 のセッション ID 差異に対応する
- 設定追加は既存 YAML と後方互換を保つ

## やること（ステップ）

- [ ] ステップ1: 現在の `kiro-loop` 起動・再起動・送信フローを確認し、`no_interactive` とクリーンアップの差し込み位置を整理する
- [ ] ステップ2: `kiro-loop.yaml` に `kiro_options.no_interactive` と `clean_session_window` の仕様を追加する
- [ ] ステップ3: 定期実行前にセッション保存 → `/quit` → session ID 抽出 → `chat --delete-session` → tmux 再生成の処理を実装する
- [ ] ステップ4: 異常終了時だけ再起動ロジックが発火する条件分岐を入れ、明示的 quit / no_interactive 正常終了 / クリーンアップ起因終了を除外する
- [ ] ステップ5: tmux ログ採取や session cleanup の確認手順を README / example config に追記する

## リポジトリ
```git-manager
show: all
```

## 完了条件
- [ ] `no_interactive=true` で `--no-interactive` が正しく付与される
- [ ] `clean_session_window` の値に応じてクリーンアップ有無を切り替えられる
- [ ] セッション保存・削除・再生成の一連処理が異常時以外に暴発しない
- [ ] 運用手順が README または設定例に残り、再現できる

## 参考情報・出典
- [[30_Notes/kiro-loop]]
- [[30_Notes/kiro-loop 並列実行と操作性改善]]
- [[60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた]]
- [[60_Resources/tmuxのpipe-paneを利用してリモートサーバでの作業ログをローカルに記録する]]

## メモ・懸念点
- セッション削除 API の挙動差分（v1 / v2）を先に確認しないと cleanup 部分でハマる可能性がある
- ログ取得を同時に入れると、クリーンアップ失敗時の原因追跡が楽になる
