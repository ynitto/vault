---
title: "REST Resource: files  |  Google Drive"
source: "https://developers.google.com/workspace/drive/api/reference/rest/v3/files?hl=ja"
author:
published:
created: 2026-05-01
description:
tags:
  - "clippings"
---
### Google Drive API v3: files リソース概要
本ページは、Google Drive APIにおける「ファイル（File）」リソースの定義と、それに関連するメソッドの詳細をまとめたドキュメントです。

#### 主なリソース構成
- **File**: ファイルのメタデータ（名前、種類、権限、共有状況、サムネイル、画像/動画メタデータなど）を保持します。
- **ContentRestriction**: ファイルの編集やコメント制限などのアクセス制限設定。
- **DownloadRestrictionsMetadata / DownloadRestriction**: ファイルのダウンロードやコピーに関する制限ルール。

#### 主要なメソッド
- **作成・取得・管理**: `create`, `get`, `list`, `copy`, `update`
- **削除・整理**: `delete`, `emptyTrash`, `generateIds`
- **コンテンツ操作**: `download`, `export`
- **権限・ラベル**: `listLabels`, `modifyLabels`
- **監視**: `watch` (変更通知の受け取り)

#### 重要なポイント
- ファイルの操作には `fileId` が必要であり、`files.list` でIDの取得が可能です。
- ショートカットや共有ドライブのアイテムには、固有の制約やフィールド（`shortcutDetails`など）が適用されます。
- 各種メタデータ（`capabilities`など）を通じて、現在のユーザーがそのファイルに対して実行可能なアクションを判定できます。