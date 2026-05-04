---
title: "ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定"
source: "https://qiita.com/Ichi0124/items/b93e2ae4309e10b348c6"
author:
  - "[[ot12]]"
published: 2019-12-24
created: 2026-05-01
description: "この記事はZOZOテクノロジーズ #2 Advent Calendar 2019 24日目の記事になります。 昨日は、@tsurumiiiさんの「変更データ（CDC）を利用したデータ同期検討」でした。 また、今年は全部で5つのAdvent Calendarが公開されています..."
tags:
  - "clippings"
---
### 概要
NLBとECS Fargate（Nginx + gRPC）構成において、gRPCの死活監視を適切に行うためのヘルスチェック設定に関する技術解説です。

### 要点
- **課題**: gRPCの平文通信環境では、NLBの標準機能（TCP/HTTP）だけではアプリケーションレベルの死活監視が困難。
- **解決策**: ECSの「HEALTHCHECK」機能と`grpc-health-probe`を組み合わせる。
- **実装のポイント**:
    - Nginxコンテナ内に`grpc-health-probe`を導入し、ECSの`HealthCheck`コマンドで定期実行する。
    - ECSのタスクヘルスチェックとNLBのTCPポート監視を連携させる。
- **ヘルスチェックの挙動**:
    1. アプリケーションが応答不能になる。
    2. Nginxのヘルスチェック失敗により、ECSタスクがUnhealthyとなる。
    3. NLBのTCPヘルスチェックが失敗し、該当タスクが切り離される。
    4. 新規タスクが起動し、サービスが復旧する。
