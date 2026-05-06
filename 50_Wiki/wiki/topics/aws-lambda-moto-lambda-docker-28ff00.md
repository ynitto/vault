---
title: "MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）"
type: "topic"
tags:
  - "aws"
  - "lambda"
  - "docker"
  - "serverless"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）.md"
summary: "Motoを使用して、Lambda関数から別のLambda関数をboto3経由で呼び出す処理をテストする方法を解説しています。Dockerを使用しない軽量な…"
---

# MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）

## 概要

Motoを使用して、Lambda関数から別のLambda関数をboto3経由で呼び出す処理をテストする方法を解説しています。Dockerを使用しない軽量なテスト構成に焦点を当てています。

*発行: 2025-02-05 / [[aws-lambda-moto-lambda-docker-28ff00]]*

## 主要なトピック

- [[aws]]
- [[lambda]]
- [[docker]]
- [[serverless]]

## 詳細

- Motoを使用して、Lambda関数から別のLambda関数をboto3経由で呼び出す処理をテストする方法を解説しています。Dockerを使用しない軽量なテスト構成に焦点を当てています。
- 要点
- **Motoの活用**: AWS SDK (boto3) をモック化し、実環境なしでLambdaの呼び出しテストが可能。
- **Lambda呼び出しのコツ**
- Lambdaクライアント作成時、必ずリージョン名を指定すること（未指定だと`KeyError`が発生）。
- **テストコードのポイント**
- `@mock_aws`デコレータを使用し、`config`で`{\"use_docker\": False}`を指定することでDockerなしのテストを実現。
- 環境変数はインポート前に設定する必要がある。
- **レスポンスの制御**

*発行: 2025-02-05 / [[aws-lambda-moto-lambda-docker-28ff00]]*

## 関連テーマ

- [[aws]]
- [[lambda]]
- [[docker]]
- [[serverless]]

## 出典

- `60_Resources/MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）.md`
- https://zenn.dev/ncdc/articles/eaa3d113c27f28
