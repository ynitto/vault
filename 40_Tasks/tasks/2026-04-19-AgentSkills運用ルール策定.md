---
task_id: 2026-04-19-AgentSkills運用ルール策定
created: 2026-04-19T10:51:13+09:00
status: Proposed
urgency: 高
priority: 高
effort: M
tags:
  - task
  - agent-skills
  - ci
source_daily:
  - - 10_Daily/2026-04-19
---

# AgentSkills運用ルール策定

## 背景・目的
Inbox の Skills 系記事は作成ノウハウより運用崩壊パターンの話が多く、先にルールを決める価値が高い。Skill を増やす前に、壊れ方・テスト範囲・棚卸し基準を決めておきたい。

## やること（ステップ）
- [ ] 構造テスト・副作用テスト・トリガー精度テストのどこまでを最低ラインにするか決める
- [ ] Skill を作る前に必ず書く項目（目的、入力、副作用、停止条件）を箇条書きにする
- [ ] 重要 Skill のみ精度テスト対象にするなど、運用コストを抑えるルールを 1 つ以上決める

## 参考情報・出典
- [[60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話]]
- [[60_Resources/Agent Skillsを行動評価する]]
- [[60_Resources/Claude Code の Skills でエラー調査を自動化！初動対応を 3 分に短縮する方法]]
- [[60_Resources/AIエージェントのスキルを自己改善させるOSSを作った]]

## 完了条件
新規 Skill を作る前提ルールが 1 枚にまとまり、最低限守る CI / テスト範囲が決まっている。

## メモ・懸念点
完璧なテスト設計を先に求めると進まない。まずは全件構造テストと重要 Skill のみ精度テストで十分。
