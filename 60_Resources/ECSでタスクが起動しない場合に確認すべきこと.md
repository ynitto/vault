---
title: "ECSでタスクが起動しない場合に確認すべきこと"
source: "https://qiita.com/x-color/items/8f986d01d6a6100b7d5b"
author:
  - "[[x-color]]"
published: 2021-01-25
created: 2026-05-01
description: "タスク起動に失敗する原因は主に下記ですが、ここでは上記２つに関する事象に対応するための確認事項を記載していこうと思います。 ネットワークエラー IAM権限不足 リソース不足 もし、ECSを利用してみたが、タスクが起動しなくて困っているなどあれば、下記の内容を見て実際の環..."
tags:
  - "clippings"
---
### 記事の要約
ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確認すべき項目を整理しています。

### チェックリスト

#### 1. エラー確認
- タスクのログを確認し、停止理由（`CannotPullContainer`, `ResourceInitializationError` 等）を特定する。
- アプリの挙動が原因の場合は、ログやヘルスチェックの設定を見直す。

#### 2. コンテナイメージの取得（ECR/S3）
- `CannotPullContainer` が出る場合：
  - ネットワーク環境（VPC, NAT Gateway, ルートテーブル等）の通信設定を確認。
  - ECR利用時はタスク実行ロールの権限とVPCエンドポイントの設定を検証。

#### 3. CloudWatch Logsへの権限
- `ResourceInitializationError` が出る場合：
  - タスク実行ロールに `logs:CreateLogGroup` 権限が付与されているか確認。

#### 4. セキュリティ・認証情報の権限
- KMS, SSM, Secrets Managerを使用する場合：
  - タスク実行ロールに必要な読み取り権限があるか確認。
  - VPCエンドポイント経由の場合はアクセス許可設定を見直す。
