---
title: "ECR ライフサイクルポリシーを利用したImageの自動削除"
type: "topic"
tags:
  - "aws"
  - "amazon-ecr"
  - "docker"
  - "shnagai"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ECR ライフサイクルポリシーを利用したImageの自動削除.md"
summary: "AWS ECR（Elastic Container Registry）のストレージコストを削減するため、ライフサイクルポリシーを活用して古いDockerイ…"
---

# ECR ライフサイクルポリシーを利用したImageの自動削除

## 概要

AWS ECR（Elastic Container Registry）のストレージコストを削減するため、ライフサイクルポリシーを活用して古いDockerイメージを自動的に削除・世代管理する方法を解説しています。

*発行: 2018-02-18 / [[aws-amazon-ecr-ecr-image-https-e7433d]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecr]]
- [[docker]]
- [[shnagai]]

## 詳細

- AWS ECR（Elastic Container Registry）のストレージコストを削減するため、ライフサイクルポリシーを活用して古いDockerイメージを自動的に削除・世代管理する方法を解説しています。
- 要点
- **目的**: 不要なイメージを削除し、ストレージ費用（0.10 USD/GB/月）を最適化する。
- **管理方法**: ライフサイクルポリシーを設定し、以下の条件で自動化が可能。
- **タグ付きイメージ**: 指定したタグ（プレフィックス）に基づき、世代数または経過日数で管理。
- **タグなしイメージ**: 未使用のイメージを日数または個数で一括削除。
- **注意点**: `tagPrefixList` を使用する場合、指定した全てのタグが付与されている必要があるため、プレフィックス単位での設定が推奨される。
- **確認手順**: ポリシー適用前に「Dry Run（ドライラン）」を実行し、意図したイメージが対象に含まれるか必ず確認する。

*発行: 2018-02-18 / [[aws-amazon-ecr-ecr-image-https-e7433d]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecr]]
- [[docker]]
- [[shnagai]]

## 出典

- `60_Resources/ECR ライフサイクルポリシーを利用したImageの自動削除.md`
- https://qiita.com/Jason/items/d12139b83643474b3666
