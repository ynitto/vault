---
title: "【レポート】Amazon ECS deployment circuit breaker を使った自動ロールバック #AWSSummit"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "cloudformation"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/【レポート】Amazon ECS deployment circuit breaker を使った自動ロールバック AWSSummit.md"
summary: "Amazon ECS deployment circuit breaker 概要"
---

# 【レポート】Amazon ECS deployment circuit breaker を使った自動ロールバック #AWSSummit

## 概要

Amazon ECS deployment circuit breaker 概要

*発行: 2026-05-20 / [[aws-amazon-ecs-amazon-ecs-deployment-7a2e9f]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[cloudformation]]

## 詳細

- ECSのローリングアップデート時に異常が発生した際、正常に動作していた直近のバージョンへ自動的にロールバックを行う機能です。
- 主なポイント
- **課題の解決**
- 従来はデプロイ失敗時にタスク起動が繰り返され、リソースとコストが無駄になっていました。
- CloudFormationスタックが「詰まる」問題を解消します。
- **判定の仕組み（2ステージ）**
- **ステージ1:** タスクがRUNNING状態に遷移せず停止する場合（イメージURLの誤りなど）。
- **ステージ2:** タスクは起動したが、ヘルスチェックに合格しない場合（アプリのバグなど）。
- **主な仕様**

*発行: 2026-05-20 / [[aws-amazon-ecs-amazon-ecs-deployment-7a2e9f]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[cloudformation]]

## 出典

- `60_Resources/【レポート】Amazon ECS deployment circuit breaker を使った自動ロールバック AWSSummit.md`
- https://dev.classmethod.jp/articles/awssummit2021-ecs-deployment-circuit-breaker/
