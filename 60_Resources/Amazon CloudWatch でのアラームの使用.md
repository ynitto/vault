---
title: "Amazon CloudWatch でのアラームの使用"
source: "https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html"
author:
published:
created: 2026-04-30
description: "アラームの状態が変わったときに Amazon SNS メッセージを送信するか、アクションを実行する Amazon CloudWatch のアラームを作成します。"
tags:
  - "clippings"
---
### Amazon CloudWatch アラームの概要
CloudWatch アラームは、メトリクスを監視し、しきい値超過時に通知送信やリソースの自動操作を行う機能です。

### 主なアラームの種類
- **メトリクスアラーム**: 単一または複数のメトリクス（数式を含む）を監視。
- **PromQL アラーム**: Prometheus クエリ言語を使用してメトリクスを監視。
- **複合アラーム**: 他のアラーム状態を組み合わせ、アラームノイズを低減。

### 特徴と運用のポイント
- **柔軟なアクション**: 通知（SNS）、EC2/Auto Scaling 操作、調査（Investigations）の開始などが可能。
- **タグ付け対応**: Metrics Insights クエリを使用し、リソースタグに基づいた動的な監視が可能。
- **状態管理**: INSUFFICIENT_DATA（データ不足）、ALARM（アラーム状態）、OKの3状態で管理。
- **履歴保存**: アラームの履歴は30日間保存されます。
- **制限事項**: 作成数に制限はありませんが、評価期間にはクォータが存在します。
- **欠落データの処理**: リソースがデータを送信しない場合の動作を個別に設定可能。
