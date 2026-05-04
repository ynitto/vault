---
title: "Javascript/html in gitlab wiki page?"
source: "https://stackoverflow.com/questions/59203694/javascript-html-in-gitlab-wiki-page"
author:
  - "[[sw_buddy 12511 silver badge99 bronze badges]]"
  - "[[blex – blex]]"
  - "[[Ulysse BN – Ulysse BN]]"
  - "[[blex 25.7k66 gold badges4949 silver badges7878 bronze badges]]"
  - "[[sw_buddy sw_buddy Over a year ago]]"
  - "[[blex blex Over a year ago]]"
published: 2019-12-06
created: 2026-05-01
description: "I'm afraid I don't really have an idea how to do this - I want to use variables in a Gitlab Wiki page. is this possible at all using html? Can I run scripts on a page? For example, this question on"
tags:
  - "clippings"
---
### Gitlab WikiでのJavaScript利用に関する回答の要約

GitlabのWikiページでは、セキュリティ上の理由から直接的なJavaScriptの実行は制限されています。動的なコンテンツを実現するには、Gitlab CIを活用し、外部でページを生成してWiki APIで更新する方法が推奨されています。

### 重要なポイント

- **直接的な制限**: GitlabはWikiのHTMLをサニタイズ（無害化）するため、`<script>`タグ等は機能しません。
- **解決策**:
    - **自動生成**: プロジェクトのビルドパイプラインでWikiページ（Markdown等）を動的に生成します。
    - **テンプレート**: Mustacheなどのテンプレートエンジンを使用してデータを流し込みます。
    - **API活用**: GitlabのWiki APIを使用して、生成したページを自動でアップロード・更新します。
- **実装手順の概要**:
    1. プロジェクト内にWiki用テンプレートとビルドスクリプトを用意する。
    2. API用のアクセストークン（WIKI_DEPLOY_TOKEN）をプロジェクトのCI変数に設定する。
    3. `.gitlab-ci.yml`でパイプラインを定義し、プッシュ時にWikiを自動更新するワークフローを構築する。