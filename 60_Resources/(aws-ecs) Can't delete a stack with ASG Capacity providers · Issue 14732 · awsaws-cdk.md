---
title: "(aws-ecs): Can't delete a stack with ASG Capacity providers · Issue #14732 · aws/aws-cdk"
source: "https://github.com/aws/aws-cdk/issues/14732"
author:
  - "[[hnrc]]"
published: 2021-05-17
created: 2026-05-01
description: "It seem to not be possible to gracefully uninstall an ECS cluster that is associated with an ASG Capacity Provider. CF hangs and never reall"
tags:
  - "clippings"
---
### 概要
AWS CDKでECSのASGキャパシティプロバイダを使用している際、CloudFormationスタックの削除が「DELETE_IN_PROGRESS」でスタックし、完了できない問題についての報告です。

### 原因
ASGキャパシティプロバイダのデフォルト設定である**「マネージド終了保護（Managed Termination Protection）」**が有効になっているため、CloudFormationがASGを削除できず処理が停止します。

### 回避策
以下のいずれかの方法で解消可能です。

*   **設定変更**: CDKの`AsgCapacityProvider`で `enableManagedTerminationProtection` を `false` に設定する。
*   **手動削除**: スタック削除時にスタックがスタックした場合、AWSコンソールまたはCLIからASGを先に手動削除する。

### 推奨される解決策（上級者向け）
Nathan Peck氏が提供する[カスタムASGデストロイヤー](https://containersonaws.com/pattern/ecs-ec2-capacity-provider-scaling)を使用し、スタック削除時に強制的にASGを削除する仕組みを実装することが推奨されています。
