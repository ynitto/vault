---
title: "Observability"
type: "concept"
tags:
  - "observability"
  - "monitoring"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/AWS初心者がCloudWatch Logs Insightsを使ってみた.md"
  - "60_Resources/Amazon CloudWatch でのアラームの使用.md"
  - "60_Resources/Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling.md"
  - "60_Resources/Auto Scalingの段階スケーリングポリシーについて.md"
  - "60_Resources/Claude Codeの拡張機能を活用した並列開発プラグインの設計と実装.md"
  - "60_Resources/ECSタスクの異常終了をCloudFormationでメトリクスにして死活監視.md"
  - "60_Resources/t_wadaさんと「単体テストの使い方考え方」の疑問点についてディスカッションしました.md"
  - "60_Resources/え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾.md"
  - "60_Resources/スケジュールされたスケーリングとターゲット追跡スケーリングを組み合わせて万全のAutoScalingを実現する.md"
summary: "監視・ログ・メトリクス活用を整理するページ。"
---

# Observability

## 概要









Observability はシステムの内部状態を理解するためのログ・メトリクス・トレースの設計を扱う。









## 詳細

- [[cloudwatch-observability-aws-cloudwatch-logs-c2a219]]: CloudWatch Logs Insightsの要約
*発行: 2020-10-08 / [[cloudwatch-observability-aws-cloudwatch-logs-c2a219]]*
- [[aws-amazon-ec2-amazon-cloudwatch-https-50034e]]: Amazon CloudWatch アラームの概要
- [[amazon-ec2-cloudwatch-application-auto-scaling-59bb27]]: Application Auto Scaling: ステップスケーリングの概要
- [[aws-amazon-ec2-auto-scaling-https-0c2f00]]: 段階スケーリング（Step Scaling Policies）の概要
*発行: 2026-05-20 / [[aws-amazon-ec2-auto-scaling-https-0c2f00]]*
- [[claude-code-git-claude-https-zenn-dev-genda-e53a2b]]: Claude Codeの拡張機能（Agent, Command, Hooks, Skills, Plugin）を駆使し、Git worktreeとtmuxを組み合わせて**大規模…
*発行: 2026-01-06 / [[claude-code-git-claude-https-zenn-dev-genda-e53a2b]]*
- [[cloudformation-cloudwatch-ecs-cloudformation-https-cfee1c]]: ECSタスクの異常終了を可視化し、アラート通知を行うための構成についての解説です。CloudWatch LogsのメトリクスフィルターとEventBridgeを活用します。
*発行: 2022-02-03 / [[cloudformation-cloudwatch-ecs-cloudformation-https-cfee1c]]*
- [[testing-observability-t-wada-https-b7c007]]: SWETグループが書籍『単体テストの使い方/考え方』の輪読会で生じた疑問に対し、t_wada氏を招いて行ったディスカッションの記録です。テスト戦略、設計、テストダブルの使い所など…
*発行: 2023-11-13 / [[testing-observability-t-wada-https-b7c007]]*
- [[aws-lambda-aws-5-3-d83259]]: AWSの各サービスを利用する際に、意図せず高額なコストが発生してしまうリスクと、その対策方法を理論値ベースで解説した記事です。
*発行: 2020-02-28 / [[aws-lambda-aws-5-3-d83259]]*
- [[aws-amazon-ec2-autoscaling-https-zenn-dev-ryoyoshii-articles-442e9f85b84-908d1d]]: この記事は、特定のピークタイムを持つEC2スポットフリートに対し、「スケジュールされたスケーリング」と「ターゲット追跡スケーリング」を組み合わせることで、効率的かつ柔軟なAuto…
  *発行: 2023-11-01 / [[aws-amazon-ec2-autoscaling-https-zenn-dev-ryoyoshii-articles-442e9f85b84-908d1d]]*

## 関連

- [[cloudwatch-observability-aws-cloudwatch-logs-c2a219]]
- [[cloudwatch]]
- [[aws-amazon-ec2-amazon-cloudwatch-https-50034e]]
- [[amazon-ec2-cloudwatch-application-auto-scaling-59bb27]]
- [[aws-amazon-ec2-auto-scaling-https-0c2f00]]
- [[claude-code-git-claude-https-zenn-dev-genda-e53a2b]]
- [[cloudformation-cloudwatch-ecs-cloudformation-https-cfee1c]]
- [[testing-observability-t-wada-https-b7c007]]
- [[aws-lambda-aws-5-3-d83259]]
- [[aws-amazon-ec2-autoscaling-https-zenn-dev-ryoyoshii-articles-442e9f85b84-908d1d]]

## 出典

- `60_Resources/AWS初心者がCloudWatch Logs Insightsを使ってみた.md`
- https://qiita.com/suuu/items/8387df88f134348f22c7
- `60_Resources/Amazon CloudWatch でのアラームの使用.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html
- `60_Resources/Application Auto Scaling のステップスケーリングの仕組み - Application Auto Scaling.md`
- https://docs.aws.amazon.com/ja_jp/autoscaling/application/userguide/step-scaling-policy-overview.html
- `60_Resources/Auto Scalingの段階スケーリングポリシーについて.md`
- https://dev.classmethod.jp/articles/auto-scaling-steps/
- `60_Resources/Claude Codeの拡張機能を活用した並列開発プラグインの設計と実装.md`
- https://zenn.dev/genda_jp/articles/b268146f3d5392
- `60_Resources/ECSタスクの異常終了をCloudFormationでメトリクスにして死活監視.md`
- https://go-to-k.hatenablog.com/entry/2022/01/30/045205
- `60_Resources/t_wadaさんと「単体テストの使い方考え方」の疑問点についてディスカッションしました.md`
- https://swet.dena.com/entry/2023/11/13/170000
- `60_Resources/え、そんなに！？意外と知らないAWSでお金がかかるポイント5選！！第3弾.md`
- https://dev.classmethod.jp/articles/5-ways-to-spend-cost-on-aws-v3/
- `60_Resources/スケジュールされたスケーリングとターゲット追跡スケーリングを組み合わせて万全のAutoScalingを実現する.md`
- https://zenn.dev/ryoyoshii/articles/442e9f85b84196
