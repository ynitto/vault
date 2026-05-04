---
title: "ECS service desire count get resets by Auto Scaling"
source: "https://stackoverflow.com/questions/63992903/ecs-service-desire-count-get-resets-by-auto-scaling"
author:
  - "[[farp332 78622 gold badges1515 silver badges3333 bronze badges]]"
  - "[[Brother_Andy 13144 bronze badges]]"
  - "[[Mark BThis user is first on the weekly AWS leaderboard. 204k2727 gold badges339339 silver badges332332 bronze badges]]"
  - "[[farp332 farp332 Over a year ago]]"
  - "[[Mark B Mark B Over a year ago]]"
published: 2020-09-21
created: 2026-05-01
description: "I want to stop my ECS Fargate test environment everyday, the best option to me is just to modify the ECS Service to have a desire count to zero as follows aws ecs update-service --cluster COOL --se..."
tags:
  - "clippings"
---
### ECSサービスの自動スケーリングに関する課題
AWS ECS Fargateで自動スケーリングを設定している環境において、CLIコマンドでDesired Countを0にしても、自動スケーリング設定がすぐに値を元に戻してしまい、タスクを完全に停止できないという問題。

### 解決のための重要なポイント
* **自動スケーリングの仕様**：自動スケーリングが有効な場合、ECSサービスの希望タスク数は自動スケーリングポリシーによって管理されるため、個別の`update-service`コマンドは上書きされます。
* **推奨される対応策**：
    * **ポリシーの調整**：スケーリングターゲットの`MinCapacity`と`MaxCapacity`を0に設定し、`SuspendedState`でスケーリングアクションを一時停止することで、意図的にスケールインさせます。
    * **構成の見直し**：自動スケーリング自体を利用しない構成に変更するか、タスク停止のスケジュールに合わせて自動スケーリング設定そのものを動的に更新（無効化）する必要があります。
