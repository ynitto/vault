---
title: "Amazon ECR"
type: "product"
tags:
  - "aws"
  - "ecr"
  - "containers"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Amazon ECR でのライフサイクルポリシーを使用したイメージのクリーンアップの自動化.md"
  - "../60_Resources/ECR ライフサイクルポリシーを利用したImageの自動削除.md"
  - "../60_Resources/ECRはイミュータブルにしておくと安全.md"
  - "../60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md"
  - "../60_Resources/ECSに必要なVPCエンドポイントまとめ（2022年版）.md"
  - "../60_Resources/Fargate の起動時間が短縮される Seekable OCI を試してみた.md"
summary: "AWS のコンテナイメージレジストリ。"
---

# Amazon ECR

## 概要






Amazon ECR はコンテナイメージ保存・配布・クリーンアップを管理するサービス。






## 詳細

- [[aws-amazon-ecr-amazon-ecr-https-c5efc2]]: Amazon ECR ライフサイクルポリシーの概要
- [[aws-amazon-ecr-ecr-image-https-e7433d]]: AWS ECR（Elastic Container Registry）のストレージコストを削減するため、ライフサイクルポリシーを活用して古いDockerイメージを自動的に削除・世…
*発行: 2018-02-18 / [[aws-amazon-ecr-ecr-image-https-e7433d]]*
- [[aws-testing-ecr-https-zenn-dev-levtech-articles-8feb6330f7c767-656f8f]]: 本記事では、AWS ECRのコンテナイメージを「イミュータブル（不変）」に設定することによるセキュリティと運用のメリットを解説しています。
*発行: 2024-10-08 / [[aws-testing-ecr-https-zenn-dev-levtech-articles-8feb6330f7c767-656f8f]]*
- [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]: ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確認すべき項目を整理してい…
*発行: 2021-01-25 / [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]*
- [[amazon-ecs-amazon-ecr-ecs-vpc-2022-f366a5]]: プライベートサブネット内のECS（特にFargate）から、NAT Gatewayを経由せずにAWS各サービスへ接続するために必要なVPCエンドポイントの構成を解説しています。
*発行: 2026-05-20 / [[amazon-ecs-amazon-ecr-ecs-vpc-2022-f366a5]]*
- [[aws-amazon-ecs-fargate-seekable-oci-956bf5]]: Seekable OCI (SOCI) による Fargate 起動高速化の検証
  *発行: 2023-12-07 / [[aws-amazon-ecs-fargate-seekable-oci-956bf5]]*

## 関連

- [[aws-amazon-ecr-amazon-ecr-https-c5efc2]]
- [[docker]]
- [[amazon-ecs]]
- [[aws]]
- [[aws-amazon-ecr-ecr-image-https-e7433d]]
- [[aws-testing-ecr-https-zenn-dev-levtech-articles-8feb6330f7c767-656f8f]]
- [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]
- [[amazon-ecs-amazon-ecr-ecs-vpc-2022-f366a5]]
- [[aws-amazon-ecs-fargate-seekable-oci-956bf5]]

## 出典

- `../60_Resources/Amazon ECR でのライフサイクルポリシーを使用したイメージのクリーンアップの自動化.md`
- https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/LifecyclePolicies.html
- `../60_Resources/ECR ライフサイクルポリシーを利用したImageの自動削除.md`
- https://qiita.com/Jason/items/d12139b83643474b3666
- `../60_Resources/ECRはイミュータブルにしておくと安全.md`
- https://zenn.dev/levtech/articles/8feb6330f7c767
- `../60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md`
- https://qiita.com/x-color/items/8f986d01d6a6100b7d5b
- `../60_Resources/ECSに必要なVPCエンドポイントまとめ（2022年版）.md`
- https://dev.classmethod.jp/articles/vpc-endpoints-for-ecs-2022/
- `../60_Resources/Fargate の起動時間が短縮される Seekable OCI を試してみた.md`
- https://zenn.dev/lincwell_inc/articles/test_seekable_oci
