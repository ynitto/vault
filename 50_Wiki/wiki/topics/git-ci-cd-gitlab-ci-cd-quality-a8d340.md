---
title: "GitLab CI/CDのCode QualityでCheckstyleのレポートを表示する"
type: "topic"
tags:
  - "git"
  - "ci-cd"
  - "kiririmode-id"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/GitLab CICDのCode QualityでCheckstyleのレポートを表示する.md"
summary: "GitLab CI/CD上でCheckstyleの静的解析結果を「Code Quality」機能として可視化し、マージリクエスト画面で確認できるようにする…"
---

# GitLab CI/CDのCode QualityでCheckstyleのレポートを表示する

## 概要

GitLab CI/CD上でCheckstyleの静的解析結果を「Code Quality」機能として可視化し、マージリクエスト画面で確認できるようにする手順の解説。

*発行: 2022-03-21 / [[git-ci-cd-gitlab-ci-cd-quality-a8d340]]*

## 主要なトピック

- [[git]]
- [[ci-cd]]
- [[kiririmode-id]]

## 詳細

- GitLab CI/CD上でCheckstyleの静的解析結果を「Code Quality」機能として可視化し、マージリクエスト画面で確認できるようにする手順の解説。
- 要点
- **目的**: 静的解析の結果をGitLab上に集約し、チーム内での指摘事項の共有を円滑にする。
- **仕組み**:
- CheckstyleのXMLレポートを`violations-maven-plugin`で「Code Climate形式（JSON）」に変換する。
- GitLabの「Code Quality」機能を利用するため、変換後のファイルパスを相対パスに修正する。
- CI/CDパイプラインの`artifacts:reports:codequality`にファイルを指定する。
- **実装手順**:
- 1. `pom.xml`に`violations-maven-plugin`を追加し、解析結果をJSON形式で出力する設定を行う。

*発行: 2022-03-21 / [[git-ci-cd-gitlab-ci-cd-quality-a8d340]]*

## 関連テーマ

- [[git]]
- [[ci-cd]]
- [[kiririmode-id]]

## 出典

- `../60_Resources/GitLab CICDのCode QualityでCheckstyleのレポートを表示する.md`
- https://kiririmode.hatenablog.jp/entry/20220321/1647850144
