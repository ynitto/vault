---
title: "How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API"
source: "https://stackoverflow.com/questions/60402838/how-to-perform-a-resumable-upload-to-a-sharepoint-site-not-root-subfolder-usin"
author:
  - "[[user9196065]]"
  - "[[Marc 78888 silver badges1515 bronze badges]]"
  - "[[Andy Andy Over a year ago]]"
  - "[[Marc Marc Over a year ago]]"
  - "[[Jatish Jatish Over a year ago]]"
published: 2020-02-26
created: 2026-05-01
description: "Documentation:https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0I am able to get the Drive ID of the sub site using the sites/domain/drives api. Using..."
tags:
  - "clippings"
---
### Microsoft Graph API でのSharePointへのレジューム可能なアップロード方法

SharePoint上の特定のフォルダーに対して、MS Graph APIでレジューム可能なアップロードを行う方法についてのQ&Aです。

#### 要点
* **問題点**: フォルダー自体に対してアップロードセッションを作成しようとするとエラーが発生します（フォルダーはファイルではないため）。
* **解決策**: フォルダーに対してではなく、**フォルダー内のファイルパス**を指定してアップロードセッションを作成する必要があります。

#### 推奨APIエンドポイント
以下のいずれかの形式でリクエストを送信してください。

* **フォルダーIDを使用する場合**:
  `POST /sites/{siteId}/drives/{driveId}/items/{folderId}:/{fileName}:/createUploadSession`
* **フォルダー名を使用する場合**:
  `POST /sites/{siteId}/drives/{driveId}/root:/{folderName}/{fileName}:/createUploadSession`

#### 補足
* 既存のドキュメントの更新ではなく、新しいファイルを作成する場合に有効な手法です。
* 言語ごとの実装については、Microsoftの公式ドキュメント（[Large file upload](https://learn.microsoft.com/en-us/graph/sdks/large-file-upload?tabs=java)）を参照してください。