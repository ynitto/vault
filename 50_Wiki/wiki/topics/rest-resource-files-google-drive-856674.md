---
title: "REST Resource: files  |  Google Drive"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/REST Resource files    Google Drive.md"
summary: "Google Drive API v3: files リソース概要"
---

# REST Resource: files  |  Google Drive

## 概要

Google Drive API v3: files リソース概要

## 主要なトピック


## 詳細

- 本ページは、Google Drive APIにおける「ファイル（File）」リソースの定義と、それに関連するメソッドの詳細をまとめたドキュメントです。
- 主なリソース構成
- **File**: ファイルのメタデータ（名前、種類、権限、共有状況、サムネイル、画像/動画メタデータなど）を保持します。
- **ContentRestriction**: ファイルの編集やコメント制限などのアクセス制限設定。
- **DownloadRestrictionsMetadata / DownloadRestriction**: ファイルのダウンロードやコピーに関する制限ルール。
- 主要なメソッド
- **作成・取得・管理**: `create`, `get`, `list`, `copy`, `update`
- **削除・整理**: `delete`, `emptyTrash`, `generateIds`
- **コンテンツ操作**: `download`, `export`

## 関連テーマ


## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/REST Resource files    Google Drive.md`
- https://developers.google.com/workspace/drive/api/reference/rest/v3/files?hl=ja
