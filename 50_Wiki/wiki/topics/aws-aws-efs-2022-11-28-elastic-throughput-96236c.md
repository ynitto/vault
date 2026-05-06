---
title: "[AWS/EFS] 2022/11/28新機能のElastic Throughputの落とし穴"
type: "topic"
tags:
  - "aws"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/AWSEFS 20221128新機能のElastic Throughputの落とし穴.md"
summary: "AWS EFSの新機能「Elastic Throughput」を導入した際、想定外のコストが発生（6日間で約1,700ドル）した失敗談。スループット上限値…"
---

# [AWS/EFS] 2022/11/28新機能のElastic Throughputの落とし穴

## 概要

AWS EFSの新機能「Elastic Throughput」を導入した際、想定外のコストが発生（6日間で約1,700ドル）した失敗談。スループット上限値の変動ではなく、実際のデータ読み書き量に応じた課金体系であったことが原因。

*発行: 2022-12-18 / [[aws-aws-efs-2022-11-28-elastic-throughput-96236c]]*

## 主要なトピック

- [[aws]]

## 詳細

- AWS EFSの新機能「Elastic Throughput」を導入した際、想定外のコストが発生（6日間で約1,700ドル）した失敗談。スループット上限値の変動ではなく、実際のデータ読み書き量に応じた課金体系であったことが原因。
- 要点まとめ
- **コスト増の要因**
- Elastic Throughputは、設定した最大スループット値ではなく、実際のデータ転送量に対して課金される。
- 従来運用（バーストモード＋プロビジョニングモード）と比較し、高トラフィックな環境では大幅なコスト増につながる可能性がある。
- **学んだ教訓**
- 新機能の仕様（特に課金モデル）を正確に理解し、本番環境への適用前に十分な検証を行うことが不可欠。
- **コスト削減の代替案**
- **EFS IAの活用**: 低頻度アクセス用ストレージにデータを置き、サイズを擬似的に大きくすることで、ベースラインスループットを維持しバーストクレジットを節約する方法が有効。

*発行: 2022-12-18 / [[aws-aws-efs-2022-11-28-elastic-throughput-96236c]]*

## 関連テーマ

- [[aws]]

## 出典

- `60_Resources/AWSEFS 20221128新機能のElastic Throughputの落とし穴.md`
- https://zenn.dev/optfit_tech/articles/df6a552bf11a15
