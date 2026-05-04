---
title: "ECSに必要なVPCエンドポイントまとめ（2022年版）"
type: "topic"
tags:
  - "amazon-ecs"
  - "amazon-ecr"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSに必要なVPCエンドポイントまとめ（2022年版）.md"
summary: "プライベートサブネット内のECS（特にFargate）から、NAT Gatewayを経由せずにAWS各サービスへ接続するために必要なVPCエンドポイントの…"
---

# ECSに必要なVPCエンドポイントまとめ（2022年版）

## 概要

プライベートサブネット内のECS（特にFargate）から、NAT Gatewayを経由せずにAWS各サービスへ接続するために必要なVPCエンドポイントの構成を解説しています。

*発行: 2026-05-20 / [[amazon-ecs-amazon-ecr-ecs-vpc-2022-f366a5]]*

## 主要なトピック

- [[amazon-ecs]]
- [[amazon-ecr]]
- [[cloudwatch]]

## 詳細

- プライベートサブネット内のECS（特にFargate）から、NAT Gatewayを経由せずにAWS各サービスへ接続するために必要なVPCエンドポイントの構成を解説しています。
- 要点まとめ
- 1. ECS用エンドポイントの要否
- **EC2利用時**: `ecs-agent`, `ecs-telemetry`, `ecs` の各エンドポイントが必須。
- **Fargate利用時**: 上記エンドポイントは**不要**。
- 2. ECR用エンドポイントの要否
- **必須**: `ecr.dkr`, `s3`（ゲートウェイ型）は全構成で必要。
- **追加条件**: `ecr.api` はEC2、Fargate Linux 1.4.0以降、Windows 1.0.0で必要。
- 3. 構成に応じて追加が必要なエンドポイント

*発行: 2026-05-20 / [[amazon-ecs-amazon-ecr-ecs-vpc-2022-f366a5]]*

## 関連テーマ

- [[amazon-ecs]]
- [[amazon-ecr]]
- [[cloudwatch]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSに必要なVPCエンドポイントまとめ（2022年版）.md`
- https://dev.classmethod.jp/articles/vpc-endpoints-for-ecs-2022/
