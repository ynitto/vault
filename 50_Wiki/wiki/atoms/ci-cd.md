---
title: "CI/CD"
type: "concept"
tags:
  - "ci-cd"
  - "automation"
created: "2026-05-02"
updated: "2026-05-06"
sources:
  - "60_Resources/GitLab rulesを理解してCICD Jobの起動を制御する.md"
  - "60_Resources/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md"
  - "60_Resources/GitLab CICDのCode QualityでCheckstyleのレポートを表示する.md"
  - "60_Resources/How to implement Post-Build stage using Jenkins Pipeline plug-in.md"
  - "60_Resources/Jenkins Pipeline プラグインのベストプラクティス トップ10  CloudBeesテクマトリックス.md"
  - "60_Resources/Jenkins のパイプラインでマスターで実行するタスクを node ブロックで囲む意味 - あらしおブログ.md"
  - "60_Resources/Load testing with GitLab.md"
  - "60_Resources/Performance Test Running and Reporting for Jenkins CI.md"
  - "60_Resources/ruleschanges always evaluates as true in MR pipeline.md"
  - "60_Resources/uv （pythonパッケージマネージャー）の使い方　詳細版.md"
  - "60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md"
  - "60_Resources/【GitHub Actions】PRが来たら自動でJSONスキーマを検証する.md"
  - "60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md"
summary: "継続的インテグレーションとデリバリーの知識を扱うページ。"
---

# CI/CD

## 概要














CI/CD はビルド・テスト・デプロイの自動化を通じて変更の安全性を高める。














## 詳細

- Git / レビュー / デプロイ自動化をつなぐ基盤として運用される。
- [[claude-code-git-claude-ai-https-0cd21e]]: GitリポジトリとClaude Codeを組み合わせ、自身の思考やプロジェクト管理を「第二の脳（Second Brain）」として構築・自動運用する方法を解説した実践録です。No…
*発行: 2026-03-01 / [[claude-code-git-claude-ai-https-0cd21e]]*
- [[git-ci-cd-gitlab-ci-cd-quality-a8d340]]: GitLab CI/CD上でCheckstyleの静的解析結果を「Code Quality」機能として可視化し、マージリクエスト画面で確認できるようにする手順の解説。
*発行: 2022-03-21 / [[git-ci-cd-gitlab-ci-cd-quality-a8d340]]*
- [[git-ci-cd-gitlab-rules-ci-cd-599977]]: GitLab CI/CDにおける `rules` の要約
*発行: 2024-05-03 / [[git-ci-cd-gitlab-rules-ci-cd-599977]]*
- [[ci-cd-luka5z-7-implement-post-build-stage-c5a71f]]: Jenkins Pipelineにおける「Post-Build（ビルド後処理）」の実装方法に関する技術的な質問と、それに対するコミュニティからの回答まとめです。
*発行: 2016-04-16 / [[ci-cd-luka5z-7-implement-post-build-stage-c5a71f]]*
- [[ci-cd-techmatrix-jenkins-pipeline-10-a251b6]]: 提供された内容を簡潔にまとめ、重要なポイントを可視化します。
*発行: 2021-06-15 / [[ci-cd-techmatrix-jenkins-pipeline-10-a251b6]]*
- [[ci-cd-arasio-jenkins-node-https-6dd61d]]: Jenkinsパイプラインにおいて、スクリプトを `node` ブロックで囲むかどうかの違いは、実行に使用される「エグゼキューター」の種類と役割にあります。
*発行: 2016-10-03 / [[ci-cd-arasio-jenkins-node-https-6dd61d]]*
- [[git-testing-load-testing-gitlab-13eb73]]: 本記事は、Grafana k6を用いてGitLab CI/CDパイプラインにパフォーマンステストを統合し、リリース前に安定性を確保する方法を解説しています。
*発行: 2020-09-28 / [[git-testing-load-testing-gitlab-13eb73]]*
- [[testing-ci-cd-performance-test-running-ab44d9]]: JenkinsのPerformance Pluginは、各種パフォーマンス・負荷テストツールの結果を自動収集し、トレンドグラフの生成やビルドステータスの判定（成功・不安定・失敗）…
- [[git-ci-cd-rules-changes-always-510794]]: GitLab CI/CDにおいて、`rules:changes`を使用しているにもかかわらず、MR（マージリクエスト）パイプラインで意図せず全ての子パイプラインがトリガーされてし…
*発行: 2021-12-28 / [[git-ci-cd-rules-changes-always-510794]]*
- [[git-ci-cd-uv-python-https-7774aa]]: uvは、Rustで記述された高速かつモダンなPythonプロジェクト・パッケージマネージャーです。pip、venv、poetry等の機能を統合し、単体でPythonバージョンの管…
*発行: 2024-11-02 / [[git-ci-cd-uv-python-https-7774aa]]*
- [[ai-agent-claude-code-skills-50-agent-3668e6]]: 本記事では、50個以上の「Agent Skills」を運用する中で直面した管理コスト増大の課題に対し、著者が見出した**CI・テスト・品質管理の具体的な設計手法**を解説していま…
*発行: 2026-04-03 / [[ai-agent-claude-code-skills-50-agent-3668e6]]*
- [[git-ci-cd-actions-pr-json-a8cf77]]: Pull Request時にJSONファイルの構造が規定のスキーマと一致しているか検証する、GitHub Actionsを利用したCI環境の構築手順です。
*発行: 2022-07-22 / [[git-ci-cd-actions-pr-json-a8cf77]]*
- [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]: Microsoft製ツール「APM (Agent Package Manager)」の解説とハンズオン
  *発行: 2026-04-25 / [[ai-agent-claude-code-microsoft-apm-https-7b1a66]]*

## 関連

- [[git]]
- [[testing]]
- [[claude-code-git-claude-ai-https-0cd21e]]
- [[git-ci-cd-gitlab-ci-cd-quality-a8d340]]
- [[git-ci-cd-gitlab-rules-ci-cd-599977]]
- [[ci-cd-luka5z-7-implement-post-build-stage-c5a71f]]
- [[ci-cd-techmatrix-jenkins-pipeline-10-a251b6]]
- [[ci-cd-arasio-jenkins-node-https-6dd61d]]
- [[git-testing-load-testing-gitlab-13eb73]]
- [[testing-ci-cd-performance-test-running-ab44d9]]

## 出典

- `60_Resources/GitLab rulesを理解してCICD Jobの起動を制御する.md`
- `60_Resources/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md`
- https://qiita.com/yamapiiii/items/cc2450f410b64329d275
- `60_Resources/GitLab CICDのCode QualityでCheckstyleのレポートを表示する.md`
- https://kiririmode.hatenablog.jp/entry/20220321/1647850144
- https://techblog.ap-com.co.jp/entry/2024/05/03/120929
- `.50_Wiki/wiki/atoms/50_Wiki/wiki/atoms50_Wiki/wiki/atoms/50_Wiki/wiki/atoms50_Wiki/wiki/atoms/60_Resources/How to implement Post-Build stage using Jenkins Pipeline plug-in?.md`
- https://stackoverflow.com/questions/36651432/how-to-implement-post-build-stage-using-jenkins-pipeline-plug-in?newreg=6b81896e863c4576bdea84053d5c103f
- `60_Resources/Jenkins Pipeline プラグインのベストプラクティス トップ10  CloudBeesテクマトリックス.md`
- https://cloudbees.techmatrix.jp/blog/top-10-best-practices-jenkins-pipeline-plugin/
- `60_Resources/Jenkins のパイプラインでマスターで実行するタスクを node ブロックで囲む意味 - あらしおブログ.md`
- https://arasio.hatenablog.com/entry/2016/10/03/011513
- `60_Resources/Load testing with GitLab.md`
- https://grafana.com/blog/load-testing-with-gitlab/
- `60_Resources/Performance Test Running and Reporting for Jenkins CI.md`
- https://jenkinsci.github.io/performance-plugin/Reporting.html
- `60_Resources/ruleschanges always evaluates as true in MR pipeline.md`
- https://stackoverflow.com/questions/70498372/ruleschanges-always-evaluates-as-true-in-mr-pipeline
- `60_Resources/uv （pythonパッケージマネージャー）の使い方　詳細版.md`
- https://zenn.dev/tabayashi/articles/52389e0d6c353a
- `60_Resources/「Skillsを50個運用して気づいたパラドックス」の続き — Agent SkillsのCIテスト品質管理を設計した話.md`
- https://qiita.com/nogataka/items/61365a15677fb62aa41a
- `60_Resources/【GitHub Actions】PRが来たら自動でJSONスキーマを検証する.md`
- https://zenn.dev/fus1ondev/articles/858836b41f2c80
- `60_Resources/ハーネスエンジニアリングを楽にする Microsoft 製の新ツール「APM」ハンズオン.md`
- https://zenn.dev/microsoft/articles/agent-package-manager-handson
