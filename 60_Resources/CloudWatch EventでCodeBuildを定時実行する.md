---
title: "CloudWatch EventでCodeBuildを定時実行する"
source: "https://www.hacknotes.jp/blog/codebuild-cloudwatchevent-scheduled-execution/"
author:
published:
created: 2026-05-01
description: "この記事ではCloudWatchEventを使用してCodeBuildを定時ビルドする方法を解説していきます。CodeBuildを定時実行させる方法が分からない人、AWS認定試験を受けようとしている方必見です！"
tags:
  - "clippings"
---
### 概要
CloudWatch Eventを使用して、AWS CodeBuildのビルド処理を定時実行する方法を解説しています。

### 手順の要点
- **CodeBuildの設定**: コンソールで対象プロジェクトのログ設定を確認し、CloudWatch Logsとサービスロールのアクセス許可を有効化する。
- **イベントルールの作成**: CloudWatch Eventコンソールで「ルールを作成」し、イベントソースに「スケジュール」を選択して実行間隔を設定する。
- **ターゲットの設定**: ターゲットに「CodeBuild プロジェクト」を指定し、対象のプロジェクトARNを入力する。
- **IAMロールの適用**: 必要に応じて新しいロールを作成・設定し、ルールを有効化して完了する。
