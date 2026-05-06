---
created: 2026-04-19T10:05:19+09:00
source: "[[60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話]]"
tags: [ナレッジ, AgentSkills, ClaudeCode, CI]
---

# Agent Skills運用と品質管理

## 概要
Agent Skills は作り始めよりも、増えた後の壊れ方を前提に設計した方が長く使える。今回の資料群は、Skill の作成手順だけでなく、構造テスト・副作用テスト・行動評価まで含めた運用設計を揃えていた。

## 詳細
### 壊れやすいポイント
- エージェント本体のアップデートで Hook や呼び出し挙動が変わる
- 依存ツールや MCP の仕様変更で Script が壊れる
- トリガーワードが競合して、意図しない Skill が発火する
- Workflow が変わり、古い Skill が陳腐化する

### 守るための枠組み
- **構造テスト**: ファイル構成やメタデータの妥当性を全件確認する
- **副作用テスト**: 実行結果として生成・更新されるファイルやディレクトリを点検する
- **トリガー精度テスト**: 肯定・否定例を使い、必要な場面だけで発火するかを見る
- **行動評価**: 出力そのものではなく、SKILL.md の手順・制約に従ったかで評価する

### 運用原則
- 「全 Skill を重くテストする」のではなく、構造テストは全件、精度テストは重要 Skill に絞る
- 利用頻度・依存健全性・ドキュメント・更新日の観点で、維持すべき Skill を見極める
- 新規 Skill 作成前に、最低限のレビュー・CI・棚卸しサイクルを決めておく

<!-- updated: 2026-04-19 -->
### Daily 運用への落とし込み
- 提案タスクは Daily に箇条書きするだけでなく、`40_Tasks/tasks/` の詳細ファイルへ落としておくと翌日以降も引き継ぎやすい
- 参照元が一時置き場に残ると再現性が落ちるため、Skill 設計の根拠記事は `60_Resources/` に固定しておく

## 関連リンク
- [[10_Daily/2026-04-19]]
- [[30_Notes/AIエージェント設計フレームワーク]]

## 出典・参照
- [[60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話]]
- [[60_Resources/Agent Skillsを行動評価する]]
- [[60_Resources/Claude Code の Skills でエラー調査を自動化！初動対応を 3 分に短縮する方法]]
- [[60_Resources/Claude CodeでSkillsを定期実行で自動化する方法]]
- [[60_Resources/AIエージェントのスキルを自己改善させるOSSを作った]]
- [[60_Resources/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話]]
<!-- updated: 2026-05-05 -->
## 追加で見えた実装ギャップ
- **Leader は仕様主導で、実行エンジンは未実装**: `leader.agent.md` はタスク分解、依存解決、`skill_candidates` / `skill_improvements` の扱いまで細かく定義されている一方、自動実行ロジック自体は見当たらなかった。
- **Skill Creator は create が強く、improve は中途半端**: `restful-api-design` や `data-validation` は完成度が高いが、improve 系はタスク定義や断片テンプレートが先行し、README/spec まで含めた統合は不明瞭だった。
- **YAML frontmatter 化は可読性改善に効く**: teammate agent を YAML frontmatter へ変換する作業は、Copilot 互換性と保守性を上げる実務的な整理として有効だった。

## 追加の出典・参照
- [[60_Resources/2026-02-11-claude-session-agent-a66b1d5.md]]
- [[60_Resources/2026-02-11-claude-session-agent-add5555.md]]
- [[60_Resources/2026-02-11-claude-session-agent-af2a2ae.md]]

## 長期記憶
<!-- ltm-saved: 2026-05-05T22:05:00+09:00 -->
- 保存済み（ltm-use）
