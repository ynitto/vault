---
title: "vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた"
source: "https://qiita.com/hirai-11/items/f16b326061956fb85c9c"
author:
  - "[[hirai-11]]"
published: 2022-11-15
created: 2026-05-01
description: "はじめに LambdaからLambdaを呼ぶ時、以下のパターンでアクセス可能かどうか検証しました。 vpc 内の public 内にいる Lambda が呼ぶ / 呼ばれる vpc 内の public 内にいる Lambda が呼ぶ / 呼ばれる (vpc endpoi..."
tags:
  - "clippings"
---
### 記事の要約
VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技術解説記事です。

### 検証の要点
- **結論**: VPC内のLambda（パブリック/プライベート問わず）は、標準設定ではインターネット経由でAWS APIを呼び出せないため、Lambda同士の直接的なinvokeに失敗する。
- **解決策**: VPCエンドポイント（Interface型）を設置することで、VPC内からAWSサービスへのアクセスが可能となり、Lambdaの呼び出しが成功する。
- **構成要素**: 
  - 呼び出し元と呼び出し先のLambda関数を作成
  - 適切なIAMロール（`AWSLambdaVPCAccessExecutionRole`等）の付与
  - VPCエンドポイントの適切なセキュリティグループ設定

### 検証結果のまとめ
- **VPC外のLambda**: インターネット経由で呼び出し可能（成功）。
- **VPC内（パブリック/プライベート）**: 
  - **エンドポイントなし**: 呼び出し不可（失敗）。
  - **エンドポイントあり**: 呼び出し可能（成功）。