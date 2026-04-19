---
created: 2026-04-19T10:05:19+09:00
source: 00_Inbox/Clippings/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md
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

## 関連リンク
- [[10_Daily/2026-04-19]]
- [[30_Notes/AIエージェント設計フレームワーク]]

## 出典・参照
- `00_Inbox/Clippings/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md`
- `00_Inbox/Clippings/Agent Skillsを行動評価する.md`
- `00_Inbox/Clippings/Claude Code の Skills でエラー調査を自動化！初動対応を 3 分に短縮する方法.md`
- `00_Inbox/Clippings/Claude CodeでSkillsを定期実行で自動化する方法.md`
- `00_Inbox/Clippings/AIエージェントのスキルを自己改善させるOSSを作った.md`
- `00_Inbox/Clippings/3人で週30PR、溺れかけた開発チームがClaude Codeスキルでレビューを回した話.md`
