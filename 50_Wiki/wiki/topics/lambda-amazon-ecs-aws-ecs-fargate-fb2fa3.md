---
title: "AWS側がしてきたECS / Fargate のスケーリング速度改善の話"
type: "topic"
tags:
  - "lambda"
  - "amazon-ecs"
  - "amazon-ec2"
  - "serverless"
  - "yoshii0110"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AWS側がしてきたECS  Fargate のスケーリング速度改善の話.md"
summary: "本記事は、2022年までにAWSが実施したAmazon ECSおよびAWS Fargateにおけるコンテナスケーリング速度の劇的な改善について解説していま…"
---

# AWS側がしてきたECS / Fargate のスケーリング速度改善の話

## 概要

本記事は、2022年までにAWSが実施したAmazon ECSおよびAWS Fargateにおけるコンテナスケーリング速度の劇的な改善について解説しています。

*発行: 2022-12-12 / [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]*

## 主要なトピック

- [[lambda]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[serverless]]
- [[yoshii0110]]

## 詳細

- 本記事は、2022年までにAWSが実施したAmazon ECSおよびAWS Fargateにおけるコンテナスケーリング速度の劇的な改善について解説しています。
- 要点まとめ
- **スケーリング速度の飛躍的向上**
- Fargateのスケーリング速度は、2020年から2022年にかけて、3,500個のコンテナ起動にかかる時間が「約60分」から「約5分」へと大幅に短縮されました。
- **レート制限の最適化**
- ECSはトークンバケットアルゴリズムを用いて起動レートを制限していますが、スケジューリングの最適化により、Fargateのデプロイ速度は以前より16倍向上しました。
- **データプレーンによる特性の違い**
- **Fargate**: 事前に準備されたタスクプールを利用するため、EC2よりもスケーリング開始が速く、単一サービスの展開に適しています。
- **EC2**: 既存インスタンスのリソース確保が必要なため、Fargateと比較してスケーリング開始までの準備に時間を要します。

*発行: 2022-12-12 / [[lambda-amazon-ecs-aws-ecs-fargate-fb2fa3]]*

## 関連テーマ

- [[lambda]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[serverless]]
- [[yoshii0110]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AWS側がしてきたECS  Fargate のスケーリング速度改善の話.md`
- https://qiita.com/yoshii0110/items/cbbfe797845dfa7e181d
