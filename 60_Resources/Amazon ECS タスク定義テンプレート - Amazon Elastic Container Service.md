---
title: "Amazon ECS タスク定義テンプレート - Amazon Elastic Container Service"
source: "https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task-definition-template.html"
author:
published:
created: 2026-05-01
description: "Amazon ECS タスク定義テンプレートを表示します。"
tags:
  - "clippings"
---
### Amazon ECS タスク定義テンプレートの概要
本ドキュメントは、Amazon ECS でタスクを定義する際に利用できる、空の JSON テンプレートを提供しています。このテンプレートを活用することで、コンソールへの入力や AWS CLI (`--cli-input-json`) での利用が効率化されます。

### 主要なポイント
- **テンプレートの種類**
  - **EC2 用:** オンプレミスや EC2 インスタンスで実行するタスク向けの設定項目が含まれます。
  - **Fargate 用:** サーバーレス環境である Fargate に特化した設定（`awsvpc` ネットワークモード等）が含まれます。
- **重要な設定項目**
  - `containerDefinitions`: コンテナイメージ、メモリ、CPU、ポートマッピング、環境変数などの定義。
  - `volumes`: データボリューム、EFS、FSx などのストレージ設定。
  - `runtimePlatform`: 実行環境のOS（Linux/Windows）やアーキテクチャの指定（Fargate では必須）。
- **生成方法**
  - 以下の AWS CLI コマンドを実行することで、最新のスケルトンを自動生成できます。
    `aws ecs register-task-definition --generate-cli-skeleton`