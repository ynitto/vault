---
title: "Fargate の起動時間が短縮される Seekable OCI を試してみた"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "amazon-ecr"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Fargate の起動時間が短縮される Seekable OCI を試してみた.md"
summary: "Seekable OCI (SOCI) による Fargate 起動高速化の検証"
---

# Fargate の起動時間が短縮される Seekable OCI を試してみた

## 概要

Seekable OCI (SOCI) による Fargate 起動高速化の検証

*発行: 2023-12-07 / [[aws-amazon-ecs-fargate-seekable-oci-956bf5]]*

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ecr]]
- [[performance]]

## 詳細

- 本記事は、AWS Fargate におけるコンテナ起動時間の短縮を目的として、SOCI インデックスの効果を検証した報告です。
- 検証結果の要点
- **起動時間の短縮効果**:
- ECS のタスク起動時間ベースで **48% 短縮**。
- アプリケーションが利用可能になるまでの時間ベースで **37% 短縮**。
- **実装方法**:
- Terraform を使用し、AWS 公式の `cfn-ecr-aws-soci-index-builder` をデプロイすることで、イメージプッシュ時に自動的にインデックスが作成される構成を採用。
- **注意点**:
- 2024年5月現在、SOCI 利用時に `CannotPullContainerError` が発生しやすくなるケースがあるため、バッチ処理など頻繁なタスク起動を行う環境では注意が必要。

*発行: 2023-12-07 / [[aws-amazon-ecs-fargate-seekable-oci-956bf5]]*

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[amazon-ecr]]
- [[performance]]

## 出典

- `60_Resources/Fargate の起動時間が短縮される Seekable OCI を試してみた.md`
- https://zenn.dev/lincwell_inc/articles/test_seekable_oci
