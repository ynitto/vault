---
title: "GitLab rulesを理解してCI/CD Jobの起動を制御する"
source: "https://techblog.ap-com.co.jp/entry/2024/05/03/120929"
author:
  - "[[FY0323]]"
published: 2024-05-03
created: 2026-04-30
description: "こんにちは、クラウド事業部 CI/CDサービスメニューチームの山路です。 今回はGitLab CI/CDを扱う上で重要なキーワードである rules について、その使い方を整理しました。 docs.gitlab.com 背景 rulesの紹介 前提 rules:if rules:changes rules:exists rules:when rules:allow_failure rules:needs rules:variables rules:interruptible 複数のキーワードを組み合わせる例 rulesを再利用する includeとの組み合わせ さいごに 背景 GitLabは …"
tags:
  - "clippings"
---
### GitLab CI/CDにおける `rules` の要約
`rules` は、GitLab CI/CDにおいてJobやWorkflowを実行する条件（いつ、どの条件下で実行するか）を定義する重要なキーワードです。パイプライン作成時に評価され、条件に合致した場合のみJobが実行されます。

### 主なキーワード
- **if**: 変数（ブランチ名、ソース、タグなど）に基づいて実行を制御。
- **changes**: 特定のファイルの変更検知に基づいて実行を制御。
- **exists**: 特定のファイルの存在に基づいて実行を制御。
- **when**: ジョブの実行タイミングや動作を定義（`on_success`, `manual`, `always`, `never`, `delayed` など）。
- **allow_failure**: ジョブ失敗時にパイプラインを停止するかどうかを制御。
- **needs**: ジョブ間の依存関係を明示し、実行順序を最適化。

### 重要なポイント
- **評価優先度**: 最初にマッチした条件が適用されます。
- **非併用**: `only`/`except` とは併用できません（現在 `only`/`except` は非推奨）。
- **再利用性**: `!reference` や `extends` を活用することで、`rules` の定義を複数のジョブ間で再利用可能です。
- **複雑な組み合わせ**: 複数の条件を組み合わせる際は、すべての条件を満たす必要があります（AND条件）。
