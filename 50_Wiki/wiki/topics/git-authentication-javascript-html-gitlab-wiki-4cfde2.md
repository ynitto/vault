---
title: "Javascript/html in gitlab wiki page?"
type: "topic"
tags:
  - "git"
  - "authentication"
  - "javascript"
  - "sw-buddy-12511-silver"
  - "blex"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Javascripthtml in gitlab wiki page?.md"
summary: "Gitlab WikiでのJavaScript利用に関する回答の要約"
---

# Javascript/html in gitlab wiki page?

## 概要

Gitlab WikiでのJavaScript利用に関する回答の要約

*発行: 2019-12-06 / [[git-authentication-javascript-html-gitlab-wiki-4cfde2]]*

## 主要なトピック

- [[git]]
- [[authentication]]
- [[javascript]]
- [[sw-buddy-12511-silver]]
- [[blex]]

## 詳細

- GitlabのWikiページでは、セキュリティ上の理由から直接的なJavaScriptの実行は制限されています。動的なコンテンツを実現するには、Gitlab CIを活用し、外部でページを生成してWiki APIで更新する方法が推奨されています。
- 重要なポイント
- **直接的な制限**: GitlabはWikiのHTMLをサニタイズ（無害化）するため、`<script>`タグ等は機能しません。
- **解決策**:
- **自動生成**: プロジェクトのビルドパイプラインでWikiページ（Markdown等）を動的に生成します。
- **テンプレート**: Mustacheなどのテンプレートエンジンを使用してデータを流し込みます。
- **API活用**: GitlabのWiki APIを使用して、生成したページを自動でアップロード・更新します。
- **実装手順の概要**:
- 1. プロジェクト内にWiki用テンプレートとビルドスクリプトを用意する。

*発行: 2019-12-06 / [[git-authentication-javascript-html-gitlab-wiki-4cfde2]]*

## 関連テーマ

- [[git]]
- [[authentication]]
- [[javascript]]
- [[sw-buddy-12511-silver]]
- [[blex]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Javascripthtml in gitlab wiki page?.md`
- https://stackoverflow.com/questions/59203694/javascript-html-in-gitlab-wiki-page
