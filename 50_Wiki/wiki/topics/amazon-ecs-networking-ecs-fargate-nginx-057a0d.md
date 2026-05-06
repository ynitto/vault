---
title: "ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定"
type: "topic"
tags:
  - "amazon-ecs"
  - "networking"
  - "ot12"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定.md"
summary: "NLBとECS Fargate（Nginx + gRPC）構成において、gRPCの死活監視を適切に行うためのヘルスチェック設定に関する技術解説です。"
---

# ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定

## 概要

NLBとECS Fargate（Nginx + gRPC）構成において、gRPCの死活監視を適切に行うためのヘルスチェック設定に関する技術解説です。

*発行: 2019-12-24 / [[amazon-ecs-networking-ecs-fargate-nginx-057a0d]]*

## 主要なトピック

- [[amazon-ecs]]
- [[networking]]
- [[ot12]]

## 詳細

- NLBとECS Fargate（Nginx + gRPC）構成において、gRPCの死活監視を適切に行うためのヘルスチェック設定に関する技術解説です。
- 要点
- **課題**: gRPCの平文通信環境では、NLBの標準機能（TCP/HTTP）だけではアプリケーションレベルの死活監視が困難。
- **解決策**: ECSの「HEALTHCHECK」機能と`grpc-health-probe`を組み合わせる。
- **実装のポイント**:
- Nginxコンテナ内に`grpc-health-probe`を導入し、ECSの`HealthCheck`コマンドで定期実行する。
- ECSのタスクヘルスチェックとNLBのTCPポート監視を連携させる。
- **ヘルスチェックの挙動**:
- 1. アプリケーションが応答不能になる。

*発行: 2019-12-24 / [[amazon-ecs-networking-ecs-fargate-nginx-057a0d]]*

## 関連テーマ

- [[amazon-ecs]]
- [[networking]]
- [[ot12]]

## 出典

- `../60_Resources/ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定.md`
- https://qiita.com/Ichi0124/items/b93e2ae4309e10b348c6
