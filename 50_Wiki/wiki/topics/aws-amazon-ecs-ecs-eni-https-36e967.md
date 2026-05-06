---
title: "ECSのENI上限引き上げ"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "docker"
  - "mumoshu"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ECSのENI上限引き上げ.md"
summary: "本記事では、Amazon ECSをEC2インスタンス（awsvpcネットワーキングモード）で運用する際に発生する、ENI（Elastic Network…"
---

# ECSのENI上限引き上げ

## 概要

本記事では、Amazon ECSをEC2インスタンス（awsvpcネットワーキングモード）で運用する際に発生する、ENI（Elastic Network Interface）の割り当て上限問題とその解決策について解説しています。

*発行: 2019-08-01 / [[aws-amazon-ecs-ecs-eni-https-36e967]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[docker]]
- [[mumoshu]]

## 詳細

- 本記事では、Amazon ECSをEC2インスタンス（awsvpcネットワーキングモード）で運用する際に発生する、ENI（Elastic Network Interface）の割り当て上限問題とその解決策について解説しています。
- 要点まとめ
- **課題：ENIの制限**
- VPCネットワーキング使用時、インスタンスごとのENI数に上限があり、そのままでは大規模なタスク運用が困難。
- **解決策：awsvpcTrunkingの有効化**
- `awsvpcTrunking`機能を有効にすることで、EC2インスタンスあたりのENI上限を大幅（約5倍）に緩和可能。
- **設定手順**
- AWS CLIを使用して、アカウント全体に対して以下のコマンドでデフォルト設定を有効化する：
- `aws ecs put-account-setting-default --name awsvpcTrunking --value enabled`

*発行: 2019-08-01 / [[aws-amazon-ecs-ecs-eni-https-36e967]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[docker]]
- [[mumoshu]]

## 出典

- `60_Resources/ECSのENI上限引き上げ.md`
- https://qiita.com/nysalor/items/a5a06013d1c37b096885
