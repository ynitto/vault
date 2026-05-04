---
title: "Amazon ECSの新ネットワーク機能”Service Connect”をAWSマネジメントコンソールから設定してみた #reinvent"
source: "https://dev.classmethod.jp/articles/try-amazon-ecs-service-connect/"
author:
  - "[[とばち]]"
published: 2026-05-20
created: 2026-05-01
description:
tags:
  - "clippings"
---
### Amazon ECS Service Connect 概要
本記事では、AWS re:Invent 2022で発表された「Amazon ECS Service Connect」の概要と、コンソールを用いた設定手順を解説しています。本機能により、ELBやApp Meshを用いずに、ECSサービス間での容易な通信制御が可能になりました。

### 主な要点
- **Service Connectの仕組み**
    - AWS Cloud Mapを用いた名前解決をECSに統合。
    - Envoyベースのプロキシ（Service Connect agent）をサイドカーとして配置し、サービスメッシュのように通信を制御。

- **主な設定項目**
    - **クライアント/サーバーモード**: 役割に応じてクライアント側のみか、サーバー側も含めるかを選択。
    - **名前空間**: 通信を行うサービス群で同一のCloud Map名前空間を指定する必要がある。
    - **ログ出力**: EnvoyサイドカーのログをCloudWatch LogsやFireLens経由で出力可能。

- **実装のポイント**
    - **ポートマッピング**: サーバー側タスク定義では、ポートに「名前」を設定する必要がある（新UIまたはJSON編集で対応）。
    - **名前解決**: `discovery-name.namespace` の形式で通信可能。
    - **環境への影響**: 既存のELBやApp Meshに代わる手段として、通信のロギングやメトリクス取得が容易になり、運用負荷の低減が期待できる。