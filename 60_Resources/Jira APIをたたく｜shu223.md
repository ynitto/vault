---
title: "Jira APIをたたく｜shu223"
source: "https://note.com/shu223/n/n392136487ee9"
author:
  - "[[shu223]]"
published: 2022-07-05
created: 2026-04-30
description: "Jiraでのあれこれを自動化したく、APIの扱い方について調べたメモ。  ドキュメント  https://developer.atlassian.com/  には次のように何種類もJiraなんとかがあり、それぞれにREST APIsがある。（さらにいえばクラウド以外にもServerシリーズも存在する）  ググると  Jira Cloud Platform or Jira Software Cloud ?Hello, I want to use the JIRA API to access the burndown charcommunity.atlassian.com"
tags:
  - "clippings"
---
### 要約
Jiraの各種タスクを自動化するために、Jira APIを利用するための準備・手順をまとめた技術メモです。

### 要点
- **APIの種類**
  - **Cloud Platform**: issuesやプロジェクトの検索用。
  - **Software Cloud**: Board, Sprint, Epic等の情報取得用。
- **APIトークンの取得**
  - Atlassianのアカウント管理画面から発行可能。
- **認証とリクエスト方法**
  - 基本認証（Basic Auth）を利用。
  - `メールアドレス:APIトークン` をBase64エンコードし、`Authorization` ヘッダに設定して送信。
- **ツール活用**
  - Pythonを使用する場合は `atlassian-python-api` ライブラリの利用が推奨されている。
