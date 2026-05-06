---
title: "Amazon ECS でのコンテナデプロイの高速化"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "performance"
  - "toricls"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Amazon ECS でのコンテナデプロイの高速化.md"
summary: "本記事は、デフォルトで設定されている「安全性を過度に重視した設定」を見直すことで、Amazon ECSのコンテナデプロイを高速化する具体的なテクニックを紹…"
---

# Amazon ECS でのコンテナデプロイの高速化

## 概要

本記事は、デフォルトで設定されている「安全性を過度に重視した設定」を見直すことで、Amazon ECSのコンテナデプロイを高速化する具体的なテクニックを紹介しています。

*発行: 2021-04-19 / [[aws-amazon-ecs-amazon-ecs-https-e68801]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[performance]]
- [[toricls]]

## 詳細

- 本記事は、デフォルトで設定されている「安全性を過度に重視した設定」を見直すことで、Amazon ECSのコンテナデプロイを高速化する具体的なテクニックを紹介しています。
- 主な高速化のポイント
- **ロードバランサのヘルスチェック設定の最適化**
- デフォルトの待ち時間は長い（約2分30秒）。`HealthCheckIntervalSeconds` を5秒、`HealthyThresholdCount` を2回に短縮することで、Healthy判定までの時間を10秒程度まで短縮可能。
- **コネクションドレイン（登録解除の遅延）の短縮**
- デフォルトの300秒を5秒程度に短縮。ただし、長時間の通信が必要なアプリでは注意が必要。
- **コンテナ終了までの待ち時間 (SIGTERM) の調整**
- `ECS_CONTAINER_STOP_TIMEOUT` をデフォルトの30秒から短縮（例: 2秒）。アプリ側で適切にSIGTERMを受け取り、終了処理を行う実装が理想。
- **コンテナイメージpullの挙動変更**

*発行: 2021-04-19 / [[aws-amazon-ecs-amazon-ecs-https-e68801]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[performance]]
- [[toricls]]

## 出典

- `../60_Resources/Amazon ECS でのコンテナデプロイの高速化.md`
- https://toris.io/2021/04/speeding-up-amazon-ecs-container-deployments/
