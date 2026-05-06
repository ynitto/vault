---
title: "Load testing with GitLab"
type: "topic"
tags:
  - "git"
  - "testing"
  - "ci-cd"
  - "mostafa-moradian"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Load testing with GitLab.md"
summary: "本記事は、Grafana k6を用いてGitLab CI/CDパイプラインにパフォーマンステストを統合し、リリース前に安定性を確保する方法を解説しています。"
---

# Load testing with GitLab

## 概要

本記事は、Grafana k6を用いてGitLab CI/CDパイプラインにパフォーマンステストを統合し、リリース前に安定性を確保する方法を解説しています。

*発行: 2020-09-28 / [[git-testing-load-testing-gitlab-13eb73]]*

## 主要なトピック

- [[git]]
- [[testing]]
- [[ci-cd]]
- [[mostafa-moradian]]

## 詳細

- 本記事は、Grafana k6を用いてGitLab CI/CDパイプラインにパフォーマンステストを統合し、リリース前に安定性を確保する方法を解説しています。
- 主要なポイント
- **k6の基本セットアップ**
- スクリプトを作成し、テストの実行条件（VU数や持続時間）を定義します。
- **閾値（Thresholds）の設定**
- サービスレベル目標（SLO）をパス/フェイルの基準として設定することで、パフォーマンス低下を自動的に検知します。
- **GitLab CIへの統合**
- `../.gitlab-ci.yml`で`grafana/k6`イメージを使用し、ビルドやデプロイ後の工程で自動的にロードテストを実行します。
- **クラウド実行の活用**

*発行: 2020-09-28 / [[git-testing-load-testing-gitlab-13eb73]]*

## 関連テーマ

- [[git]]
- [[testing]]
- [[ci-cd]]
- [[mostafa-moradian]]

## 出典

- `../60_Resources/Load testing with GitLab.md`
- https://grafana.com/blog/load-testing-with-gitlab/
