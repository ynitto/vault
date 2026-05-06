---
title: "VPCエンドポイントとNAT Gatewayの比較"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/VPCエンドポイントとNAT Gatewayの比較.md"
summary: "VPCエンドポイントとNAT Gatewayの比較要約"
---

# VPCエンドポイントとNAT Gatewayの比較

## 概要

VPCエンドポイントとNAT Gatewayの比較要約

*発行: 2024-01-24 / [[vpc-nat-gateway-https-iret-media-91809-89411d]]*

## 主要なトピック


## 詳細

- 本記事では、AWSのVPC内からAWSサービスや外部へ通信する際、VPCエンドポイントとNAT Gatewayをセキュリティと費用の観点から比較しています。
- セキュリティ面のポイント
- **VPCエンドポイント**: AWSネットワーク内での直接通信が可能。ポリシーによる詳細なアクセス制御や、AWS外のSaaSとのセキュアな接続（PrivateLink）が可能。
- **NAT Gateway**: AWSグローバルネットワークを経由するため通信は暗号化されるが、VPCエンドポイントのような細かい制御は限定的。
- 費用面の比較・使い分け
- **ゲートウェイ型VPCエンドポイント（S3, DynamoDB）**: 無料のため導入を推奨。
- **インターフェイス型VPCエンドポイント**: 固定費・変動費が発生するため、以下のケースで検討が必要。
- 選定の判断基準
- **ケース1（NAT GW不要時）**: VPCエンドポイントの方がセキュアかつ低コスト。

*発行: 2024-01-24 / [[vpc-nat-gateway-https-iret-media-91809-89411d]]*

## 関連テーマ


## 出典

- `../60_Resources/VPCエンドポイントとNAT Gatewayの比較.md`
- https://iret.media/91809
