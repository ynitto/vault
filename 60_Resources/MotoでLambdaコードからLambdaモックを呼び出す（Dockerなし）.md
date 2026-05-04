---
title: "MotoでLambdaコードからLambdaモックを呼び出す（Dockerなし）"
source: "https://zenn.dev/ncdc/articles/eaa3d113c27f28"
author:
published: 2025-02-05
created: 2026-04-30
description:
tags:
  - "clippings"
---
### 記事の要約
Motoを使用して、Lambda関数から別のLambda関数をboto3経由で呼び出す処理をテストする方法を解説しています。Dockerを使用しない軽量なテスト構成に焦点を当てています。

### 要点
*   **Motoの活用**: AWS SDK (boto3) をモック化し、実環境なしでLambdaの呼び出しテストが可能。
*   **Lambda呼び出しのコツ**
    *   Lambdaクライアント作成時、必ずリージョン名を指定すること（未指定だと`KeyError`が発生）。
*   **テストコードのポイント**
    *   `@mock_aws`デコレータを使用し、`config`で`{\"use_docker\": False}`を指定することでDockerなしのテストを実現。
    *   環境変数はインポート前に設定する必要がある。
*   **レスポンスの制御**
    *   MotoのAPIエンドポイント（`http://motoapi.amazonaws.com/moto-api/static/lambda-simple/response`）に対してPOSTリクエストを送ることで、呼び出し先のレスポンスを柔軟に設定可能。
    *   複数回の呼び出しに対する連続したレスポンス定義にも対応。
