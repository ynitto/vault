---
title: "CloudWatch EventでCodeBuildを定時実行する"
type: "topic"
tags:
  - "aws"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/CloudWatch EventでCodeBuildを定時実行する.md"
summary: "CloudWatch Eventを使用して、AWS CodeBuildのビルド処理を定時実行する方法を解説しています。"
---

# CloudWatch EventでCodeBuildを定時実行する

## 概要

CloudWatch Eventを使用して、AWS CodeBuildのビルド処理を定時実行する方法を解説しています。

## 主要なトピック

- [[aws]]
- [[cloudwatch]]

## 詳細

- CloudWatch Eventを使用して、AWS CodeBuildのビルド処理を定時実行する方法を解説しています。
- 手順の要点
- **CodeBuildの設定**: コンソールで対象プロジェクトのログ設定を確認し、CloudWatch Logsとサービスロールのアクセス許可を有効化する。
- **イベントルールの作成**: CloudWatch Eventコンソールで「ルールを作成」し、イベントソースに「スケジュール」を選択して実行間隔を設定する。
- **ターゲットの設定**: ターゲットに「CodeBuild プロジェクト」を指定し、対象のプロジェクトARNを入力する。
- **IAMロールの適用**: 必要に応じて新しいロールを作成・設定し、ルールを有効化して完了する。

## 関連テーマ

- [[aws]]
- [[cloudwatch]]

## 出典

- `60_Resources/CloudWatch EventでCodeBuildを定時実行する.md`
- https://www.hacknotes.jp/blog/codebuild-cloudwatchevent-scheduled-execution/
