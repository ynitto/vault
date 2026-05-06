---
title: "describe-key-value-store — AWS CLI 2.34.32 Command Reference"
type: "topic"
tags:
  - "aws"
  - "cloudfront"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/describe-key-value-store — AWS CLI 2.34.32 Command Reference.md"
summary: "AWS CLI: describe-key-value-store"
---

# describe-key-value-store — AWS CLI 2.34.32 Command Reference

## 概要

AWS CLI: describe-key-value-store

## 主要なトピック

- [[aws]]
- [[cloudfront]]

## 詳細

- このコマンドは、指定したCloudFront Key Value Storeのメタデータ情報を取得するために使用します。
- 主な機能
- **目的**: Key Value Storeのステータスやサイズなどの詳細情報を確認する。
- **必須引数**: `--kvs-arn` (対象のKey Value StoreのARN)
- 取得可能な情報（出力項目）
- **状態**: `Status`, `FailureReason`, `ETag`
- **容量**: `ItemCount` (項目数), `TotalSizeInBytes` (合計サイズ)
- **タイムスタンプ**: `Created` (作成日時), `LastModified` (最終更新日時)

## 関連テーマ

- [[aws]]
- [[cloudfront]]

## 出典

- `60_Resources/describe-key-value-store — AWS CLI 2.34.32 Command Reference.md`
- https://docs.aws.amazon.com/cli/latest/reference/cloudfront-keyvaluestore/describe-key-value-store.html
