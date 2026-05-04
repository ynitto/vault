---
title: "全S3バケットのデータイベントをCloudTrailロギング対象にする設定の留意点"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/全S3バケットのデータイベントをCloudTrailロギング対象にする設定の留意点.md"
summary: "CloudTrailに、アカウント内の全S3バケットのデータイベントを一括で記録する機能が追加されました。ただし、設定時には既存のイベントセレクタ設定が上…"
---

# 全S3バケットのデータイベントをCloudTrailロギング対象にする設定の留意点

## 概要

CloudTrailに、アカウント内の全S3バケットのデータイベントを一括で記録する機能が追加されました。ただし、設定時には既存のイベントセレクタ設定が上書きされるため、意図しない設定変更にならないよう注意が必要です。

*発行: 2017-09-21 / [[s3-cloudtrail-https-dev-classmethod-jp-articles-cloudtrail-all-s3-bucket-27e509]]*

## 主要なトピック


## 詳細

- CloudTrailに、アカウント内の全S3バケットのデータイベントを一括で記録する機能が追加されました。ただし、設定時には既存のイベントセレクタ設定が上書きされるため、意図しない設定変更にならないよう注意が必要です。
- 要点
- **新機能の概要**
- 管理コンソールからワンクリックで全S3バケットのデータイベントをロギング可能。
- **留意点（重要）**
- **設定の上書き**: 全バケット対象の設定を追加すると、既存の「特定のバケット指定」や「読み書き権限（Read/WriteType）の設定」が上書きされます。
- **競合回避**: 既存の設定と全体設定が併用されるわけではなく、全体設定が優先されるため、既存の設定が意図せず無効化されるリスクがあります。
- **推奨アクション**
- 既にイベントセレクタ設定が存在するTrailに対して全体設定を追加する場合は、現在設定されている内容と本来の目的を十分に確認してから実施してください。

*発行: 2017-09-21 / [[s3-cloudtrail-https-dev-classmethod-jp-articles-cloudtrail-all-s3-bucket-27e509]]*

## 関連テーマ


## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/全S3バケットのデータイベントをCloudTrailロギング対象にする設定の留意点.md`
- https://dev.classmethod.jp/articles/cloudtrail-all-s3-bucket-setting/
