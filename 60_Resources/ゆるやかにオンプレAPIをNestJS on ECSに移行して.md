---
title: "ゆるやかにオンプレAPIをNestJS on ECSに移行して"
source: "https://qiita.com/y_okasuke/items/4523d91da69aae2b40db"
author:
  - "[[y_okasuke]]"
published: 2022-12-23
created: 2026-05-01
description: "この記事はアイスタイル Advent Calendar 2022 25日目の記事です。 はじめに じゃんたま 雀士★1になりました。 はじめまして、アイスタイルT&C部に所属しているokashitayというものです。 今回の記事では、こないだまでNestJSどころかNod..."
tags:
  - "clippings"
---
### 記事の要約
本記事は、既存のPHP/Go製APIをNestJSに統一し、AWS Fargate (ECS) へ移行した際の実体験と知見をまとめたものです。開発環境の刷新に伴う学びと、運用上のトラブルシューティングが共有されています。

### 主要なポイント
- **NestJS採用の背景**
    - 複数言語での運用負荷軽減と、メンテナンス性・可読性の向上のためNestJSへ統一。
    - TypeScriptによる品質維持と公式ドキュメントの充実が決め手。

- **開発における学び**
    - **ライブラリの内部コード確認**: ドキュメントにない挙動を理解するために、内部実装を直接読むことが有効。
    - **Graceful Shutdown**: `app.enableShutdownHooks()`の有効化が必須。

- **インフラ・運用面の注意点**
    - **Fargateリソース構成**: Node.jsのCPU/メモリ制限を考慮し、適切にスケールさせる必要がある。
    - **ALB 502エラー対策**: ALBのタイムアウト設定に対し、NestJS側（`keepAliveTimeout`）を長く設定することで解決可能。
