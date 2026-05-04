---
title: "ECSでタスクが起動しない場合に確認すべきこと"
type: "topic"
tags:
  - "amazon-ecr"
  - "authentication"
  - "cloudwatch"
  - "networking"
  - "x-color"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md"
summary: "ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確…"
---

# ECSでタスクが起動しない場合に確認すべきこと

## 概要

ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確認すべき項目を整理しています。

*発行: 2021-01-25 / [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]*

## 主要なトピック

- [[amazon-ecr]]
- [[authentication]]
- [[cloudwatch]]
- [[networking]]
- [[x-color]]

## 詳細

- ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確認すべき項目を整理しています。
- チェックリスト
- 1. エラー確認
- タスクのログを確認し、停止理由（`CannotPullContainer`, `ResourceInitializationError` 等）を特定する。
- アプリの挙動が原因の場合は、ログやヘルスチェックの設定を見直す。
- 2. コンテナイメージの取得（ECR/S3）
- `CannotPullContainer` が出る場合：
- ネットワーク環境（VPC, NAT Gateway, ルートテーブル等）の通信設定を確認。
- ECR利用時はタスク実行ロールの権限とVPCエンドポイントの設定を検証。

*発行: 2021-01-25 / [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]*

## 関連テーマ

- [[amazon-ecr]]
- [[authentication]]
- [[cloudwatch]]
- [[networking]]
- [[x-color]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md`
- https://qiita.com/x-color/items/8f986d01d6a6100b7d5b
