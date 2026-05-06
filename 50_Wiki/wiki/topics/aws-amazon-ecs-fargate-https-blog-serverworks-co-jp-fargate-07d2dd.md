---
title: "Fargate利用時のヘルスチェックを理解する - サーバーワークスエンジニアブログ"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "networking"
  - "swx-yamamoto"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Fargate利用時のヘルスチェックを理解する - サーバーワークスエンジニアブログ.md"
summary: "AWS Fargate環境における、Application Load Balancer (ALB) および ECSタスク定義による2種類のヘルスチェックの…"
---

# Fargate利用時のヘルスチェックを理解する - サーバーワークスエンジニアブログ

## 概要

AWS Fargate環境における、Application Load Balancer (ALB) および ECSタスク定義による2種類のヘルスチェックの仕様と運用上の注意点を解説した記事です。

*発行: 2022-02-25 / [[aws-amazon-ecs-fargate-https-blog-serverworks-co-jp-fargate-07d2dd]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[networking]]
- [[swx-yamamoto]]

## 詳細

- AWS Fargate環境における、Application Load Balancer (ALB) および ECSタスク定義による2種類のヘルスチェックの仕様と運用上の注意点を解説した記事です。
- 要点まとめ
- **ALBによるヘルスチェック**
- HTTP/HTTPSリクエストによりターゲットの正常性を監視。
- 異常時はALBが通信を遮断し、ECSが該当タスクを自動停止・再起動する。
- 起動直後の誤判定を防ぐため、「ヘルスチェックの猶予期間」の設定が重要。
- **ECSサービスによるヘルスチェック**
- タスク定義内にコマンド（`CMD-SHELL`等）を記述し、コンテナ内部から監視。
- 異常時はECSがタスクのヘルスステータスを「異常」と判断し、タスクの入れ替えを行う。

*発行: 2022-02-25 / [[aws-amazon-ecs-fargate-https-blog-serverworks-co-jp-fargate-07d2dd]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[networking]]
- [[swx-yamamoto]]

## 出典

- `60_Resources/Fargate利用時のヘルスチェックを理解する - サーバーワークスエンジニアブログ.md`
- https://blog.serverworks.co.jp/fargate_healthcheck
