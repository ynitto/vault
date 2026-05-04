---
title: "GitLab rulesを理解してCI/CD Jobの起動を制御する"
type: "topic"
tags:
  - "git"
  - "ci-cd"
  - "fy0323"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLab rulesを理解してCICD Jobの起動を制御する.md"
summary: "GitLab CI/CDにおける `rules` の要約"
---

# GitLab rulesを理解してCI/CD Jobの起動を制御する

## 概要

GitLab CI/CDにおける `rules` の要約

*発行: 2024-05-03 / [[git-ci-cd-gitlab-rules-ci-cd-599977]]*

## 主要なトピック

- [[git]]
- [[ci-cd]]
- [[fy0323]]

## 詳細

- `rules` は、GitLab CI/CDにおいてJobやWorkflowを実行する条件（いつ、どの条件下で実行するか）を定義する重要なキーワードです。パイプライン作成時に評価され、条件に合致した場合のみJobが実行されます。
- 主なキーワード
- **if**: 変数（ブランチ名、ソース、タグなど）に基づいて実行を制御。
- **changes**: 特定のファイルの変更検知に基づいて実行を制御。
- **exists**: 特定のファイルの存在に基づいて実行を制御。
- **when**: ジョブの実行タイミングや動作を定義（`on_success`, `manual`, `always`, `never`, `delayed` など）。
- **allow_failure**: ジョブ失敗時にパイプラインを停止するかどうかを制御。
- **needs**: ジョブ間の依存関係を明示し、実行順序を最適化。
- 重要なポイント

*発行: 2024-05-03 / [[git-ci-cd-gitlab-rules-ci-cd-599977]]*

## 関連テーマ

- [[git]]
- [[ci-cd]]
- [[fy0323]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLab rulesを理解してCICD Jobの起動を制御する.md`
- https://techblog.ap-com.co.jp/entry/2024/05/03/120929
