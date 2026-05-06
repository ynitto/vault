---
title: "reviewdog🐶を飼ってGitLab-CI上で静的解析しませんか？"
type: "topic"
tags:
  - "git"
  - "parupappa2929"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/reviewdog🐶を飼ってGitLab-CI上で静的解析しませんか？.md"
summary: "GitLab CI環境において、静的コード解析ツール「reviewdog」を導入し、解析結果をマージリクエスト（MR）に自動コメントさせるための手順を解説…"
---

# reviewdog🐶を飼ってGitLab-CI上で静的解析しませんか？

## 概要

GitLab CI環境において、静的コード解析ツール「reviewdog」を導入し、解析結果をマージリクエスト（MR）に自動コメントさせるための手順を解説した記事です。

*発行: 2023-04-02 / [[git-parupappa2929-reviewdog-gitlab-ci-https-1b0f89]]*

## 主要なトピック

- [[git]]
- [[parupappa2929]]

## 詳細

- GitLab CI環境において、静的コード解析ツール「reviewdog」を導入し、解析結果をマージリクエスト（MR）に自動コメントさせるための手順を解説した記事です。
- 要点まとめ
- **reviewdogとは**
- ツールで検出されたリンターの指摘を、MRの該当箇所に直接コメントとして表示するGo言語製のOSS。
- **導入の主要ステップ**
- 1. **GitLabユーザー作成**: reviewdog用に専用ユーザーを作成し、APIアクセストークンを発行。
- 2. **Runnerの設定**: パイプライン実行用のGitLab Runnerを登録し、タグ（reviewdog等）を付与。
- 3. **`.gitlab-ci.yml`の構成**: `reviewdog`ステージを定義し、各リンター（textlint, ESLint, RuboCop）の実行コマンドを記述。
- 4. **パイプライン連携**: `reviewdog`コマンドへ各リンターの結果をパイプ（`|`）で渡し、`reporter=gitlab-mr-discussion`オプションでMRにコメントさせる。

*発行: 2023-04-02 / [[git-parupappa2929-reviewdog-gitlab-ci-https-1b0f89]]*

## 関連テーマ

- [[git]]
- [[parupappa2929]]

## 出典

- `60_Resources/reviewdog🐶を飼ってGitLab-CI上で静的解析しませんか？.md`
- https://qiita.com/parupappa2929/items/b1071c716cfe937b2210
