---
title: "Google Workspace と Google ドライブでサポートされている MIME タイプ  |  Google Drive"
source: "https://developers.google.com/workspace/drive/api/guides/mime-types?hl=ja"
author:
published:
created: 2026-05-01
description: "Google Workspace と Google ドライブ API でサポートされている MIME タイプのリストを確認する。"
tags:
  - "clippings"
---
### Google Workspace および Google ドライブの MIME タイプ概要

このページでは、Google Workspace および Google ドライブで使用される独自の MIME タイプについて解説しています。これらは主にAPIを通じたファイル検索や、Marketplaceでのアプリのインデックス登録時に利用されます。

### MIME タイプ活用のポイント
* **クエリのフィルタリング**: APIクエリにおいて特定のファイル形式のみを抽出する際に使用します。
* **アプリ連携**: 特定のファイル形式を開くことができるアプリとして、Marketplaceへ登録する際に必要となります。

### 主な Google Workspace MIME タイプ
* **ドキュメント系**: `application/vnd.google-apps.document` (Google ドキュメント), `application/vnd.google-apps.spreadsheet` (Google スプレッドシート), `application/vnd.google-apps.presentation` (Google スライド)
* **管理・コンテナ系**: `application/vnd.google-apps.folder` (フォルダ), `application/vnd.google-apps.shortcut` (ショートカット)
* **その他**: `application/vnd.google-apps.script` (Apps Script), `application/vnd.google-gemini.gem` (Gemini Gem) など。

### 関連情報
* Google Workspace ドキュメントのエクスポートに使用する変換用の MIME タイプについても別途ドキュメントが用意されています。