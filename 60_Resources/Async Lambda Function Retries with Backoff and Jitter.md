---
title: "Async Lambda Function Retries with Backoff and Jitter"
source: "https://lucvandonkersgoed.com/2022/02/07/async-lambda-function-retries-with-backoff-and-jitter/"
author:
published: 2022-02-07
created: 2026-05-01
description: "In this post we'll implement a custom async Lambda retry handler with exponential backoff, full jitter, and delays up to 12 hours."
tags:
  - "clippings"
---
### 記事の要約
AWS Lambdaの標準機能では不十分な非同期処理の再試行回数（最大2回）を補うため、SQSの可視性タイムアウトを利用して最大24時間の指数バックオフとジッター付き再試行を実現する手法を解説した記事です。

### 要点
- **背景と課題**
    - Lambdaの標準的な非同期再試行は最大2回までであり、外部システムの長時間停止に対応できない。
    - 指数バックオフとジッターを組み合わせることで、システムの負荷を分散しつつ成功率を高める必要がある。

- **解決策の仕組み**
    - **SQSの活用**: 失敗したメッセージをSQSキューに送り、再試行ハンドラーを通じて可視性タイムアウト（最大12時間）を調整しながら再試行を繰り返す。
    - **再試行エンベロープ**: 元のデータに試行回数などのメタデータを付与し、ハンドラーが正しいバックオフ時間を計算できるようにする。

- **主要機能**
    - **指数バックオフ**: 再試行ごとに待ち時間を倍増させる。
    - **フルジッター**: 乱数を用いて再試行タイミングを分散し、ターゲットへの集中負荷を回避する。

- **注意点・限界**
    - **精度**: 低トラフィック環境ではSQSのポーリング遅延により、期待より長い待ち時間が発生する可能性がある。
    - **制約**: SQSのインフライトメッセージ制限（120,000件）や、再試行期間の上限（最大14日）がある。
    - **代替案**: より高い精度や長期間の再試行が必要な場合は、AWS Step Functionsの使用が推奨される。