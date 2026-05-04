---
title: "【レポート】Amazon ECS deployment circuit breaker を使った自動ロールバック #AWSSummit"
source: "https://dev.classmethod.jp/articles/awssummit2021-ecs-deployment-circuit-breaker/"
author:
  - "[[岩田智哉]]"
published: 2026-05-20
created: 2026-05-01
description: "ECS deployment circuit breakerについてデモ動画を交えつつ20分程度でサクっと学べるセッションです ECS初心者の方にオススメです"
tags:
  - "clippings"
---
### Amazon ECS deployment circuit breaker 概要
ECSのローリングアップデート時に異常が発生した際、正常に動作していた直近のバージョンへ自動的にロールバックを行う機能です。

### 主なポイント
* **課題の解決**
    * 従来はデプロイ失敗時にタスク起動が繰り返され、リソースとコストが無駄になっていました。
    * CloudFormationスタックが「詰まる」問題を解消します。
* **判定の仕組み（2ステージ）**
    * **ステージ1:** タスクがRUNNING状態に遷移せず停止する場合（イメージURLの誤りなど）。
    * **ステージ2:** タスクは起動したが、ヘルスチェックに合格しない場合（アプリのバグなど）。
* **主な仕様**
    * 「ローリングアップデート」デプロイタイプで利用可能。
    * 失敗判定のしきい値は「10〜200」の間で自動計算され、現時点では固定値です。
    * 新規・既存サービス問わず、CLI、マネコン、CloudFormationから設定可能です。