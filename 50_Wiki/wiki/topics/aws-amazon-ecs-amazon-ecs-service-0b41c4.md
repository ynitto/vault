---
title: "Amazon ECSの新ネットワーク機能”Service Connect”をAWSマネジメントコンソールから設定してみた #reinvent"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon ECSの新ネットワーク機能”Service Connect”をAWSマネジメントコンソールから設定してみた reinvent.md"
summary: "Amazon ECS Service Connect 概要"
---

# Amazon ECSの新ネットワーク機能”Service Connect”をAWSマネジメントコンソールから設定してみた #reinvent

## 概要

Amazon ECS Service Connect 概要

*発行: 2026-05-20 / [[aws-amazon-ecs-amazon-ecs-service-0b41c4]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[cloudwatch]]

## 詳細

- 本記事では、AWS re:Invent 2022で発表された「Amazon ECS Service Connect」の概要と、コンソールを用いた設定手順を解説しています。本機能により、ELBやApp Meshを用いずに、ECSサービス間での容易な通信制御が可能になりました。
- 主な要点
- **Service Connectの仕組み**
- AWS Cloud Mapを用いた名前解決をECSに統合。
- Envoyベースのプロキシ（Service Connect agent）をサイドカーとして配置し、サービスメッシュのように通信を制御。
- **主な設定項目**
- **クライアント/サーバーモード**: 役割に応じてクライアント側のみか、サーバー側も含めるかを選択。
- **名前空間**: 通信を行うサービス群で同一のCloud Map名前空間を指定する必要がある。
- **ログ出力**: EnvoyサイドカーのログをCloudWatch LogsやFireLens経由で出力可能。

*発行: 2026-05-20 / [[aws-amazon-ecs-amazon-ecs-service-0b41c4]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[cloudwatch]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon ECSの新ネットワーク機能”Service Connect”をAWSマネジメントコンソールから設定してみた reinvent.md`
- https://dev.classmethod.jp/articles/try-amazon-ecs-service-connect/
