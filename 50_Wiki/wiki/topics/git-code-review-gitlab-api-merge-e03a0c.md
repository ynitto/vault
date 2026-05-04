---
title: "GitLab API で Merge Request のコメントを一括取得する方法"
type: "topic"
tags:
  - "git"
  - "code-review"
  - "akkie76"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLab API で Merge Request のコメントを一括取得する方法.md"
summary: "GitLab APIを活用し、チーム開発におけるコードレビューの質や量を定量化するための「Merge Request（MR）コメント集計ツール」の作成手法…"
---

# GitLab API で Merge Request のコメントを一括取得する方法

## 概要

GitLab APIを活用し、チーム開発におけるコードレビューの質や量を定量化するための「Merge Request（MR）コメント集計ツール」の作成手法を解説した記事です。

*発行: 2021-12-21 / [[git-code-review-gitlab-api-merge-e03a0c]]*

## 主要なトピック

- [[git]]
- [[code-review]]
- [[akkie76]]

## 詳細

- GitLab APIを活用し、チーム開発におけるコードレビューの質や量を定量化するための「Merge Request（MR）コメント集計ツール」の作成手法を解説した記事です。
- 要点
- **目的**: 若手メンバーのレビュー支援と、育成のための指標作成。
- **主な利用API**:
- **Merge Requests API**: 対象となるMR情報の取得。
- **Notes API**: 各MRのコメント取得（ただしDiscussionと重複が発生する点に注意）。
- **Discussions API**: コメント内容をスレッド単位で取得するために使用。
- **実装のポイント**:
- **Kotlinでの実装**: `fuel`を使用したHTTPリクエストと`Kotlinx.Serialization`によるデータパース。

*発行: 2021-12-21 / [[git-code-review-gitlab-api-merge-e03a0c]]*

## 関連テーマ

- [[git]]
- [[code-review]]
- [[akkie76]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitLab API で Merge Request のコメントを一括取得する方法.md`
- https://qiita.com/akkie76/items/2cc798e309b0e82f13fc
