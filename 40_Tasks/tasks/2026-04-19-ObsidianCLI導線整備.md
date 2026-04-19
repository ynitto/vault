---
task_id: 2026-04-19-ObsidianCLI導線整備
created: 2026-04-19T10:51:13+09:00
status: proposed
urgency: 高
priority: 高
effort: S
tags: [task, obsidian, cli]
source_daily: [[10_Daily/2026-04-19]]
---

# ObsidianCLI導線整備

## 背景・目的
Obsidian CLI を使える状態にすると、Daily / Tasks / Notes の更新を Vault 内で閉じて回せる。今回の Inbox では Obsidian CLI と Claude Code の連携が最も即効性の高い改善候補だった。

## やること（ステップ）
- [ ] Obsidian 本体で CLI が有効か確認し、Vault に対する基本コマンドが通る状態にする
- [ ] `daily:read` または `tasks` 相当の安全な読み取りコマンドを 1 本試す
- [ ] Daily / Kanban / Notes のどれから自動化を始めるかを 1 つ決める

## 参考情報・出典
- [[60_Resources/Obsidian CLI]]
- [[60_Resources/Obsidian CLI が全ユーザーに無料開放されたので Claude Code 用スキルと一緒にセットアップした]]
- [[60_Resources/Obsidian × Claude Codeで情報整理を緩くやってみたけど、想像以上によかった話]]

## 完了条件
CLI を有効化した上で、Vault に対する読み取り系コマンドが少なくとも 1 つ成功し、次に自動化する導線が 1 つ決まっている。

## メモ・懸念点
Obsidian 側が未起動だと CLI が失敗する可能性がある。最初は書き込みより読み取りで確認した方が安全。
