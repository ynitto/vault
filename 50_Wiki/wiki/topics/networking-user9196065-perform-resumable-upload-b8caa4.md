---
title: "How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API"
type: "topic"
tags:
  - "networking"
  - "user9196065"
  - "marc-78888-silver-badges1515"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API.md"
summary: "Microsoft Graph API でのSharePointへのレジューム可能なアップロード方法"
---

# How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API

## 概要

Microsoft Graph API でのSharePointへのレジューム可能なアップロード方法

*発行: 2020-02-26 / [[networking-user9196065-perform-resumable-upload-b8caa4]]*

## 主要なトピック

- [[networking]]
- [[user9196065]]
- [[marc-78888-silver-badges1515]]

## 詳細

- SharePoint上の特定のフォルダーに対して、MS Graph APIでレジューム可能なアップロードを行う方法についてのQ&Aです。
- 要点
- **問題点**: フォルダー自体に対してアップロードセッションを作成しようとするとエラーが発生します（フォルダーはファイルではないため）。
- **解決策**: フォルダーに対してではなく、**フォルダー内のファイルパス**を指定してアップロードセッションを作成する必要があります。
- 推奨APIエンドポイント
- 以下のいずれかの形式でリクエストを送信してください。
- **フォルダーIDを使用する場合**:
- `POST /sites/{siteId}/drives/{driveId}/items/{folderId}:/{fileName}:/createUploadSession`
- **フォルダー名を使用する場合**:

*発行: 2020-02-26 / [[networking-user9196065-perform-resumable-upload-b8caa4]]*

## 関連テーマ

- [[networking]]
- [[user9196065]]
- [[marc-78888-silver-badges1515]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API.md`
- https://stackoverflow.com/questions/60402838/how-to-perform-a-resumable-upload-to-a-sharepoint-site-not-root-subfolder-usin
