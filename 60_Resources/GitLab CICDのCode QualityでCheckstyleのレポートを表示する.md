---
title: "GitLab CI/CDのCode QualityでCheckstyleのレポートを表示する"
source: "https://kiririmode.hatenablog.jp/entry/20220321/1647850144"
author:
  - "[[kiririmode (id:kiririmode)]]"
published: 2022-03-21
created: 2026-04-30
description: "何をするにも「わかりやすく表示する」というのは重要です。 Checkstyleについても、その結果をGitLabやGithubでわかりやすく表示できれば、「これは直さないと」とチーム内で共有できるでしょう。 GitLabでCheckstyleのレポートを表示できるようにする 実現に向けた、GitLabにおけるCode Qualityの基本知識 Checkstyleの問題をCode Climate形式に変換する Checkstyleの出力形式 Code Climate形式への変換 GitLab CI/CDへの組み込み Code Climate形式のファイルパスは相対パス Code Climate…"
tags:
  - "clippings"
---
### 概要
GitLab CI/CD上でCheckstyleの静的解析結果を「Code Quality」機能として可視化し、マージリクエスト画面で確認できるようにする手順の解説。

### 要点
* **目的**: 静的解析の結果をGitLab上に集約し、チーム内での指摘事項の共有を円滑にする。
* **仕組み**: 
    * CheckstyleのXMLレポートを`violations-maven-plugin`で「Code Climate形式（JSON）」に変換する。
    * GitLabの「Code Quality」機能を利用するため、変換後のファイルパスを相対パスに修正する。
    * CI/CDパイプラインの`artifacts:reports:codequality`にファイルを指定する。
* **実装手順**:
    1. `pom.xml`に`violations-maven-plugin`を追加し、解析結果をJSON形式で出力する設定を行う。
    2. `.gitlab-ci.yml`で`sed`コマンドを用いてJSON内のファイルパスを絶対パスから相対パスへ変換する。
    3. 同ファイルで変換後のレポートをGitLabのレポート機能へ渡す設定を追加する。
