---
title: "(aws-ecs): Can't delete a stack with ASG Capacity providers · Issue #14732 · aws/aws-cdk"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ec2"
  - "cloudformation"
  - "hnrc"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/(aws-ecs) Can't delete a stack with ASG Capacity providers · Issue 14732 · awsaws-cdk.md"
summary: "AWS CDKでECSのASGキャパシティプロバイダを使用している際、CloudFormationスタックの削除が「DELETE_IN_PROGRESS」…"
---

# (aws-ecs): Can't delete a stack with ASG Capacity providers · Issue #14732 · aws/aws-cdk

## 概要

AWS CDKでECSのASGキャパシティプロバイダを使用している際、CloudFormationスタックの削除が「DELETE_IN_PROGRESS」でスタックし、完了できない問題についての報告です。

*発行: 2021-05-17 / [[aws-amazon-ecs-aws-ecs-t-delete-516697]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[cloudformation]]
- [[hnrc]]

## 詳細

- AWS CDKでECSのASGキャパシティプロバイダを使用している際、CloudFormationスタックの削除が「DELETE_IN_PROGRESS」でスタックし、完了できない問題についての報告です。
- 原因
- ASGキャパシティプロバイダのデフォルト設定である**「マネージド終了保護（Managed Termination Protection）」**が有効になっているため、CloudFormationがASGを削除できず処理が停止します。
- 回避策
- 以下のいずれかの方法で解消可能です。
- **設定変更**: CDKの`AsgCapacityProvider`で `enableManagedTerminationProtection` を `false` に設定する。
- **手動削除**: スタック削除時にスタックがスタックした場合、AWSコンソールまたはCLIからASGを先に手動削除する。
- 推奨される解決策（上級者向け）
- Nathan Peck氏が提供する[カスタムASGデストロイヤー](https://containersonaws.com/pattern/ecs-ec2-capacity-provider-scaling)を使用し、スタック削除時に強制的にASGを削除する仕組みを実装することが推奨されています。

*発行: 2021-05-17 / [[aws-amazon-ecs-aws-ecs-t-delete-516697]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ec2]]
- [[cloudformation]]
- [[hnrc]]

## 出典

- `60_Resources/(aws-ecs) Can't delete a stack with ASG Capacity providers · Issue 14732 · awsaws-cdk.md`
- https://github.com/aws/aws-cdk/issues/14732
