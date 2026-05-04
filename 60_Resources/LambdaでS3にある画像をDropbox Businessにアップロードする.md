---
title: "LambdaでS3にある画像をDropbox Businessにアップロードする"
source: "https://qiita.com/nkmk1215/items/95e2d97e5bb89a8b904a"
author:
  - "[[nkmk1215]]"
published: 2021-09-20
created: 2026-05-01
description: "LambdaでS3にある画像をDropbox Businessにアップロードしたときの個人メモ 前提 LambdaでS3にある画像をDropboxにアップロードするができていること Dropbox Business APIの基礎知識を把握していること アクセストー..."
tags:
  - "clippings"
---
### 記事の概要
AWS Lambdaを利用し、S3上の画像をDropbox Businessの共有フォルダへアップロードするための実装手順に関する個人用メモです。

### 要点まとめ
* **事前準備**
    * Dropbox Business APIの知識とアクセストークンの準備が必要。
    * アプリ設定は「Full Dropbox」で作成する。
* **Root Namespace IDの取得**
    * `get_current_account` APIを実行し、チームスペースのルートフォルダIDを特定する。
* **ソースコードの修正**
    * Lambda関数のHTTPヘッダーに`Dropbox-API-Path-Root`を追加する。
    * `NAMESPACE_ID`を指定して通信を行う。
* **注意点**
    * 個人用Dropboxと異なり、Business版はルートフォルダの指定が必須。
    * エラー調査時は公式ドキュメント（特にAPIリファレンス）の熟読が推奨される。