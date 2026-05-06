---
title: "Amazon ECRにプッシュしたコンテナイメージのタグを変更してみた"
type: "topic"
tags:
  - "aws"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Amazon ECRにプッシュしたコンテナイメージのタグを変更してみた.md"
summary: "Amazon ECRにおけるコンテナイメージのタグ付け替え手順"
---

# Amazon ECRにプッシュしたコンテナイメージのタグを変更してみた

## 概要

Amazon ECRにおけるコンテナイメージのタグ付け替え手順

*発行: 2026-05-20 / [[aws-amazon-ecr-https-dev-classmethod-jp-articles-change-ecr-image-tag-0c63c9]]*

## 主要なトピック

- [[aws]]

## 詳細

- 本記事は、AWS ECR上でプッシュ済みのコンテナイメージに対して、CLIを使用してタグを付け替える方法を解説しています。
- 重要なポイント
- **基本操作**: マネジメントコンソールでは不可。AWS CLIを使用。
- **手順の考え方**: 直接的な名前変更ではなく、「新しいタグを付与」した後に「元のタグを削除」する2段階で実行。
- **注意点**: 削除の際、対象イメージに付いている最後のタグを消すとイメージ自体が削除されるため注意が必要。
- 作業の流れ
- 1. **タグ付与**: `batch-get-image`でマニフェストを取得し、`put-image`で別名タグを付与。
- 2. **タグ削除**: `batch-delete-image`で不要になった古いタグを削除。
- 補足情報

*発行: 2026-05-20 / [[aws-amazon-ecr-https-dev-classmethod-jp-articles-change-ecr-image-tag-0c63c9]]*

## 関連テーマ

- [[aws]]

## 出典

- `60_Resources/Amazon ECRにプッシュしたコンテナイメージのタグを変更してみた.md`
- https://dev.classmethod.jp/articles/change-ecr-image-tag/
