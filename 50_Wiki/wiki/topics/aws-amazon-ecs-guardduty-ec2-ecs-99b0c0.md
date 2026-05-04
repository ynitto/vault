---
title: "[神アップデート]GuardDutyがEC2やECSのマルウェア検知時のスキャンに対応したので実際にスキャンさせてみた #reinforce"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/神アップデートGuardDutyがEC2やECSのマルウェア検知時のスキャンに対応したので実際にスキャンさせてみた reinforce.md"
summary: "Amazon GuardDuty Malware Protection 概要"
---

# [神アップデート]GuardDutyがEC2やECSのマルウェア検知時のスキャンに対応したので実際にスキャンさせてみた #reinforce

## 概要

Amazon GuardDuty Malware Protection 概要

*発行: 2022-07-26 / [[aws-amazon-ecs-guardduty-ec2-ecs-99b0c0]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]

## 詳細

- Amazon GuardDutyの機能拡充により、EC2およびコンテナ環境のEBSボリュームに対するマルウェアスキャンが可能になりました。
- 主なポイント
- **仕組み**: GuardDutyが特定の脅威を検知した際、対象EC2のスナップショットを自動取得し、エージェントレスでスキャンを実行。
- **特長**:
- **エージェント不要**: 既存のインスタンスに影響を与えず、スナップショットベースで安全にスキャン。
- **自動化**: 脅威検知をトリガーとして自動実行されるため、インシデント対応の迅速化が実現。
- **KMS対応**: 暗号化されたEBSボリュームも、適切な権限設定によりスキャン可能。
- **料金**: スキャンしたデータ容量（GB）に応じた従量課金。30日間の無料トライアルあり。
- **制限事項**:

*発行: 2022-07-26 / [[aws-amazon-ecs-guardduty-ec2-ecs-99b0c0]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/神アップデートGuardDutyがEC2やECSのマルウェア検知時のスキャンに対応したので実際にスキャンさせてみた reinforce.md`
- https://dev.classmethod.jp/articles/guardduty-support-malware-protection/
