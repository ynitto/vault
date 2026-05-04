---
title: "Amazon ECS でのコンテナデプロイの高速化"
source: "https://toris.io/2021/04/speeding-up-amazon-ecs-container-deployments/"
author:
  - "[[toricls]]"
published: 2021-04-19
created: 2026-05-01
description: "Amazon ECS でデプロイされる ECS サービスのデプロイ速度の高速化を目指す際に見直すことが推奨されるデフォルト設定値とその考え方やテクニックについて紹介しています. 記事前半で主に Web サービスを前提とした項目を、後半ではローリングアップデートを利用する際のデプロイ設定を見ていきます."
tags:
  - "clippings"
---
### Amazon ECSのデプロイ速度を改善する手法
本記事は、デフォルトで設定されている「安全性を過度に重視した設定」を見直すことで、Amazon ECSのコンテナデプロイを高速化する具体的なテクニックを紹介しています。

#### 主な高速化のポイント
- **ロードバランサのヘルスチェック設定の最適化**
  - デフォルトの待ち時間は長い（約2分30秒）。`HealthCheckIntervalSeconds` を5秒、`HealthyThresholdCount` を2回に短縮することで、Healthy判定までの時間を10秒程度まで短縮可能。
- **コネクションドレイン（登録解除の遅延）の短縮**
  - デフォルトの300秒を5秒程度に短縮。ただし、長時間の通信が必要なアプリでは注意が必要。
- **コンテナ終了までの待ち時間 (SIGTERM) の調整**
  - `ECS_CONTAINER_STOP_TIMEOUT` をデフォルトの30秒から短縮（例: 2秒）。アプリ側で適切にSIGTERMを受け取り、終了処理を行う実装が理想。
- **コンテナイメージpullの挙動変更**
  - `ECS_IMAGE_PULL_BEHAVIOR` を `prefer-cached` に設定し、EC2ホスト上のキャッシュを利用してダウンロード時間を削減する。
- **ローリングデプロイ設定の最適化**
  - `minimumHealthyPercent` を調整（例: 50%）し、新旧タスクの入れ替えステップ数を減らすことでデプロイ全体の所要時間を短縮する。