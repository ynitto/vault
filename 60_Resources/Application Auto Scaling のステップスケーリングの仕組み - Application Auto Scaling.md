---
title: "Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling"
source: "https://docs.aws.amazon.com/ja_jp/autoscaling/application/userguide/step-scaling-policy-overview.html"
author:
published:
created: 2026-04-30
description: "Application Auto Scaling がアプリケーションを事前定義された増分でスケーリングする方法について説明します。"
tags:
  - "clippings"
---
## Application Auto Scaling: ステップスケーリングの概要

ステップスケーリングは、CloudWatch アラームの違反状況に応じて、段階的に容量を増減させるスケーリングポリシーです。

### 主な仕組みとポイント
- **段階的な調整**: アラーム違反の程度に応じて、異なるスケーリング量（ステップ調整値）を定義可能。
- **調整タイプ**: 以下の3種類から選択可能。
  - `ChangeInCapacity`: 現在の容量を絶対値で増減。
  - `ExactCapacity`: 容量を指定の数値に直接変更。
  - `PercentChangeInCapacity`: 現在の容量に対する割合（%）で増減。
- **クールダウン期間**: 連続するスケーリングアクティビティの間隔を制御し、急激な変動や「フラッピング（過剰な増減の繰り返し）」を防止。
- **考慮事項**:
  - スケールアウトとスケールインのしきい値間に十分なマージンを設けること。
  - メトリクスと容量が比例関係にある場合は「ターゲット追跡スケーリング」の検討が推奨される。

### 管理方法
- **CLIコマンド**: `put-scaling-policy` や `describe-scaling-policies` などを使用して作成・管理を行います。
- **サポート**: 一部のリソースではAWSコンソール経由での設定も可能です。
