---
task_id: 2026-05-05-statemachine-use連携実例検証
title: statemachine-use連携実例検証
created: 2026-05-05T07:32:51
status: none
urgency: 中
priority: 高
effort: M
tags: [task, kiro-cli, statemachine-use, gitlab, jenkins, ai-agent]
source_daily: [[10_Daily/2026-05-05]]
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

# statemachine-use連携実例検証

## 背景・目的
`statemachine-use` スキルの実用性を確認するため、実際のワークフロー（GitLab Issue取得 → チケット解析 → Jenkins実行 → ログ解析 → GitLab Issue更新）を動作させる。2026-05-01のデイリーノートで未完了として記録されており、kiro-loopの分散動作設計とも密接に関連する。

## 条件
### 前提条件
- `statemachine-use` スキルがインストール済み（確認済み）
- GitLab・Jenkins の接続情報が設定済みであること
- `gitlab-idd`・`jenkins-use` スキルが利用可能であること

### 制約条件
- 本番環境のGitLab/Jenkinsへの影響を避けるため、テスト用プロジェクト・ジョブで実施する
- スコープ: 動作確認のみ（本番運用への組み込みは別タスク）

## やること（ステップ）

- [ ] ステップ1: `statemachine-use` の SKILL.md を読み込み、YAML定義の書き方を確認する
- [ ] ステップ2: テスト用ワークフローYAMLを作成する（GitLab Issue取得 → チケット解析 → Jenkins実行 → ログ解析 → Issue更新）
- [ ] ステップ3: GitLab・Jenkins の接続情報を確認・設定する
- [ ] ステップ4: `statemachine-use` でYAMLを実行し、各ステートの遷移を確認する
- [ ] ステップ5: 実行ログを確認し、エラーがあれば修正する
- [ ] ステップ6: 動作確認結果を `30_Notes/` に記録する

## リポジトリ
```git-manager
show: all
```

## 完了条件
- [ ] YAMLワークフローが最後まで実行され、GitLab Issueが更新されること
- [ ] 各ステートの遷移ログが確認できること
- [ ] 動作確認メモが `30_Notes/` に追記されていること

## 参考情報・出典
- [[60_Resources/自律的Kiro CLIオーケストレーター（2026-05-05）]]
- [[30_Notes/AIエージェント設計フレームワーク]]

## メモ・懸念点
- kiro-loopのグローバルスケジューリングと組み合わせると、より強力な自律実行基盤になる可能性がある
- Jenkins接続情報が未設定の場合は `jenkins-use` スキルの設定から始める必要がある

<!-- ❓ 質問: GitLab・Jenkinsのテスト環境は用意されているか？
     推測値: 既存の開発環境を流用
     理由: 接続情報の有無が不明 -->
