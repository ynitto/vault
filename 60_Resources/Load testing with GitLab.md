---
title: "Load testing with GitLab"
source: "https://grafana.com/blog/load-testing-with-gitlab/"
author:
  - "[[Mostafa Moradian]]"
published: 2020-09-28
created: 2026-05-01
description: "In this tutorial, we walk through how to integrate performance testing into your development process with GitLab and Grafana k6."
tags:
  - "clippings"
---
### GitLabでのロードテスト自動化：要約
本記事は、Grafana k6を用いてGitLab CI/CDパイプラインにパフォーマンステストを統合し、リリース前に安定性を確保する方法を解説しています。

### 主要なポイント
* **k6の基本セットアップ**
    * スクリプトを作成し、テストの実行条件（VU数や持続時間）を定義します。
* **閾値（Thresholds）の設定**
    * サービスレベル目標（SLO）をパス/フェイルの基準として設定することで、パフォーマンス低下を自動的に検知します。
* **GitLab CIへの統合**
    * `.gitlab-ci.yml`で`grafana/k6`イメージを使用し、ビルドやデプロイ後の工程で自動的にロードテストを実行します。
* **クラウド実行の活用**
    * `k6 cloud`を利用し、地理的に分散した負荷生成や、CI環境のリソース制限を超える大規模なテストを実施可能です。
* **定期実行の自動化**
    * GitLabのパイプラインスケジュール機能を使用し、深夜などのトラフィックが少ない時間帯に定期的なパフォーマンスレポートを作成します。