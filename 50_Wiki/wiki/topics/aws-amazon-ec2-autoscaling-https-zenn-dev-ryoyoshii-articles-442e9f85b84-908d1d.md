---
title: "スケジュールされたスケーリングとターゲット追跡スケーリングを組み合わせて万全のAutoScalingを実現する"
type: "topic"
tags:
  - "aws"
  - "amazon-ec2"
  - "cloudwatch"
  - "observability"
  - "dev-classmethod-jp-author-yoshii-ryo"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/スケジュールされたスケーリングとターゲット追跡スケーリングを組み合わせて万全のAutoScalingを実現する.md"
summary: "この記事は、特定のピークタイムを持つEC2スポットフリートに対し、「スケジュールされたスケーリング」と「ターゲット追跡スケーリング」を組み合わせることで、…"
---

# スケジュールされたスケーリングとターゲット追跡スケーリングを組み合わせて万全のAutoScalingを実現する

## 概要

この記事は、特定のピークタイムを持つEC2スポットフリートに対し、「スケジュールされたスケーリング」と「ターゲット追跡スケーリング」を組み合わせることで、効率的かつ柔軟なAuto Scalingを実現する方法を解説しています。

*発行: 2023-11-01 / [[aws-amazon-ec2-autoscaling-https-zenn-dev-ryoyoshii-articles-442e9f85b84-908d1d]]*

## 主要なトピック

- [[aws]]
- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]
- [[dev-classmethod-jp-author-yoshii-ryo]]

## 詳細

- この記事は、特定のピークタイムを持つEC2スポットフリートに対し、「スケジュールされたスケーリング」と「ターゲット追跡スケーリング」を組み合わせることで、効率的かつ柔軟なAuto Scalingを実現する方法を解説しています。
- 要点
- **目的**: 決まった時間帯（10時〜14時）は8台、それ以外は通常2台、突発的な負荷増時には最大4台まで自動拡張する構成の構築。
- **使用サービス**: Application Auto Scaling（AWS CLIで設定）
- **実装手順**:
- 1. **スケーラブルターゲットへの登録**: 対象リソース（スポットフリート）をAuto Scalingの管理下に置く。
- 2. **スケジュール設定**: `put-scheduled-action`を使用し、時間帯に応じた最小/最大キャパシティを指定。
- 3. **ターゲット追跡の設定**: `put-scaling-policy`でCPU使用率に基づいた自動追従（しきい値50%）を設定。
- **運用時の注意点**:

*発行: 2023-11-01 / [[aws-amazon-ec2-autoscaling-https-zenn-dev-ryoyoshii-articles-442e9f85b84-908d1d]]*

## 関連テーマ

- [[aws]]
- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]
- [[dev-classmethod-jp-author-yoshii-ryo]]

## 出典

- `../60_Resources/スケジュールされたスケーリングとターゲット追跡スケーリングを組み合わせて万全のAutoScalingを実現する.md`
- https://zenn.dev/ryoyoshii/articles/442e9f85b84196
