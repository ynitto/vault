---
task_id: 2026-05-06-spec-kit Runtime View テンプレート設計
title: spec-kit Runtime View テンプレート設計
created: 2026-05-06T07:24:46+09:00
status: none
urgency: 中
priority: 高
effort: M
tags: [task, spec-kit, runtime-view, workflow, ticket-driven, design]
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

# spec-kit Runtime View テンプレート設計

## 背景・目的
Plan から Tasks に直接落とすだけでは、画面遷移・コンポーネント連携・外部境界の責務が抜けやすい。`Runtime View` を 1 ステップ追加し、粗いシーケンス図や責務表をテンプレート化することで、ticket-driven な AI 実装フローの抜け漏れを減らす。

## 条件
### 前提条件
- 現在使っている plan / task breakdown の流れを見直せること
- Runtime View をテキストまたは簡易図で表現するテンプレートを置けること
- 既存の `spec-kit` 記事の運用知見を参照できること

### 制約条件
- 重い設計ドキュメントにはせず、1タスクごとに短時間で書ける粒度に抑える
- 既存の Daily → Tasks フローを壊さず、途中に挟める形式にする
- 図の作成手段は Markdown / Mermaid / PlantUML など扱いやすいものを優先する

## やること（ステップ）

- [ ] ステップ1: 現在の Plan / Task 詳細テンプレートで抜けやすい情報を棚卸しする
- [ ] ステップ2: Runtime View に最低限必要な項目（主体、イベント、境界、データの流れ、検証観点）を定義する
- [ ] ステップ3: 1ページで書けるテンプレート案を作る
- [ ] ステップ4: 既存タスクを1件選び、Runtime View を試し書きして不足項目を調整する
- [ ] ステップ5: plan / task breakdown フローのどこで Runtime View を必須にするか決める

## リポジトリ
```git-manager
show: all
```

## 完了条件
- [ ] Runtime View のテンプレートが1つ定義されている
- [ ] テンプレートの利用タイミングが Plan / Tasks フロー内で決まっている
- [ ] 既存タスク1件に適用して、抜け漏れ削減に効くことを確認できる

## 参考情報・出典
- [[30_Notes/AIエージェント設計フレームワーク]]
- [[60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる]]
- [[60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った]]

## メモ・懸念点
- 図を重くしすぎると spec-kit の軽量さを損なうので、文章 + 最小図の折衷が現実的
- Claude 系で Plan、GPT 系でレビューという役割分担も含めて型に落とすと再利用しやすい
