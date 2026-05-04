---
title: "ECSに必要なVPCエンドポイントまとめ（2022年版）"
source: "https://dev.classmethod.jp/articles/vpc-endpoints-for-ecs-2022/"
author:
  - "[[八木優成]]"
published: 2026-05-20
created: 2026-05-01
description: "ECSで必要なVPCエンドポイントをまとめました。NATを使わず、VPCエンドポイントのみで構成する場合は参考にしてください。"
tags:
  - "clippings"
---
### 記事の要約
プライベートサブネット内のECS（特にFargate）から、NAT Gatewayを経由せずにAWS各サービスへ接続するために必要なVPCエンドポイントの構成を解説しています。

### 要点まとめ

#### 1. ECS用エンドポイントの要否
* **EC2利用時**: `ecs-agent`, `ecs-telemetry`, `ecs` の各エンドポイントが必須。
* **Fargate利用時**: 上記エンドポイントは**不要**。

#### 2. ECR用エンドポイントの要否
* **必須**: `ecr.dkr`, `s3`（ゲートウェイ型）は全構成で必要。
* **追加条件**: `ecr.api` はEC2、Fargate Linux 1.4.0以降、Windows 1.0.0で必要。

#### 3. 構成に応じて追加が必要なエンドポイント
* **ログ収集**: `logs` (CloudWatch Logs)
* **シークレット管理**: `secretsmanager`
* **SSM連携・ECS Exec**: `ssm`, `ssmmessages`

#### 4. 運用上の注意点
* **エラーからの特定**: タスクの停止理由をコンソールで確認し、必要なエンドポイントを順次追加するアプローチが有効。
* **セキュリティ**: タスクロールには最小権限を付与し、本番環境でのAdministrator権限利用は避ける。
