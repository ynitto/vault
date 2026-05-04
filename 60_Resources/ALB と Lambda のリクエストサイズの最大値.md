---
title: "ALB と Lambda のリクエストサイズの最大値"
source: "https://yohei-a.hatenablog.jp/entry/20210115/1610705961"
author:
  - "[[yohei-a]]"
published: 2021-01-15
created: 2026-05-01
description: "Lambda の呼び出しペイロードは最大 6MB（同期の場合） ALB はターゲットが Lambda の場合にリクエストボディは最大 1MB 参考 リソース Quota 呼び出しペイロード (リクエストとレスポンス) 6 MB (同期)256 KB (非同期) AWS Lambda のクォータ - AWS Lambda HTTP 413: Payload too large ターゲットは Lambda 関数で、リクエストボディが 1 MB を超えています。 Application Load Balancer のトラブルシューティング - Elastic Load Balancing"
tags:
  - "clippings"
---
### 要約
AWS LambdaとApplication Load Balancer（ALB）を連携させる際の、リクエストペイロード制限に関する技術情報のまとめです。

### 要点
- **Lambdaのペイロード制限**
  - 同期呼び出し: 最大 6MB
  - 非同期呼び出し: 最大 256KB
- **ALB経由の制限**
  - Lambdaをターゲットとする場合、リクエストボディは最大 **1MB** に制限されます。
- **トラブルシューティング**
  - リクエストボディが1MBを超えると「HTTP 413: Payload too large」エラーが発生します。