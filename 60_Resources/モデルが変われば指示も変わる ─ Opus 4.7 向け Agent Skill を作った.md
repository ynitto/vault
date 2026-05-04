---
title: "モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った"
source: "https://zenn.dev/shinyay/articles/opus-4-7-prompt-design-copilot-skill"
author:
published: 2026-04-27
created: 2026-05-04
original_source: 00_Inbox/Clippings/モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った.md
copied_at: 2026-05-05T07:32:51
tags: [resource/web, ai-agent, claude, opus, prompt-engineering, agent-skill, 2026-05]
---
### 要約
この記事は、GitHub Copilot から「Claude Opus 4.7」を利用する際、モデルの特性に合わせて指示（プロンプト）の「型」を最適化し、最大限のパフォーマンスを引き出すための手法を解説しています。著者は「5スロットブリーフ」という構造化されたプロンプト形式を自動生成する Agent Skill を自作し、作業効率と品質を劇的に向上させました。

### 要点まとめ
- **モデルの特性とフロントローディングの重要性**
  - Claude Opus 4.7 は adaptive thinking への一本化やトークナイザーの変更により、4.6 とは最適な指示の仕方が異なる。
  - ターンごとにコストがかかるため、対話で詰めるのではなく、最初のターンに必要な情報をすべて詰め込む「フロントローディング」が最適解。

- **「5スロットブリーフ」という型**
  - プロンプトを以下の5つに整理することで、モデルへ意図を正確に伝達可能。
    1. **Goal**: 成功の定義
    2. **Constraints**: 制約条件（やってはいけないこと）
    3. **Acceptance criteria**: 完了条件
    4. **Context**: 文脈や関連情報
    5. **Validation**: 自己検証のためのテストやコマンド（最大の品質レバー）

- **Agent Skill（claude-prompt-optimizer）の活用**
  - ユーザーの数行の依頼を 80 行程度の最適化されたブリーフに自動変換するスキルを作成。
  - `generate`（生成）、`audit`（監査）、`route`（安価モデルから Opus へのエスカレーション制御）の3モードに対応。

- **コストと品質の最適化 (v2アップデート)**
  - ルーティング戦略（Haiku 4.5/Sonnet 4.5 → Opus 4.7）を導入し、タスクの難易度に応じてコストを制御。
  - 厳格な静的チェック（Linter）を組み込み、deprecated な構文やモデルの誤解を招く指示をCIレベルで排除。
