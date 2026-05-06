---
title: "rules:changes always evaluates as true in MR pipeline"
type: "topic"
tags:
  - "git"
  - "ci-cd"
  - "moshe-6"
  - "4871919-gold-badges5757-silver"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ruleschanges always evaluates as true in MR pipeline.md"
summary: "GitLab CI/CDにおいて、`rules:changes`を使用しているにもかかわらず、MR（マージリクエスト）パイプラインで意図せず全ての子パイプ…"
---

# rules:changes always evaluates as true in MR pipeline

## 概要

GitLab CI/CDにおいて、`rules:changes`を使用しているにもかかわらず、MR（マージリクエスト）パイプラインで意図せず全ての子パイプラインがトリガーされてしまう問題に関するQ&A。

*発行: 2021-12-28 / [[git-ci-cd-rules-changes-always-510794]]*

## 主要なトピック

- [[git]]
- [[ci-cd]]
- [[moshe-6]]
- [[4871919-gold-badges5757-silver]]

## 詳細

- GitLab CI/CDにおいて、`rules:changes`を使用しているにもかかわらず、MR（マージリクエスト）パイプラインで意図せず全ての子パイプラインがトリガーされてしまう問題に関するQ&A。
- 要点
- **問題の原因**
- `rules`内で `if` と `changes` を別々の項目（ダッシュ付き）として定義しているため、条件が独立して評価され、`if`条件（MR判定）が真であれば `changes` を無視して実行されてしまう。
- **解決策**
- `changes`の前のハイフンを取り除き、`if`と同一のルールとして結合することで、条件を同時に評価させる。
- **補足・注意点**
- `rules:changes` はトリガーパイプラインとの組み合わせで期待通りに動作しない場合がある（GitLabの既知の課題）。
- その場合、トリガー元（親）のパイプラインから `changes` ルールを除去し、トリガー先（子）のパイプライン側で制御するのが有効。

*発行: 2021-12-28 / [[git-ci-cd-rules-changes-always-510794]]*

## 関連テーマ

- [[git]]
- [[ci-cd]]
- [[moshe-6]]
- [[4871919-gold-badges5757-silver]]

## 出典

- `60_Resources/ruleschanges always evaluates as true in MR pipeline.md`
- https://stackoverflow.com/questions/70498372/ruleschanges-always-evaluates-as-true-in-mr-pipeline
