---
title: "ECRはイミュータブルにしておくと安全"
type: "topic"
tags:
  - "aws"
  - "testing"
  - "amazon-ecr"
  - "cloudformation"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/ECRはイミュータブルにしておくと安全.md"
summary: "本記事では、AWS ECRのコンテナイメージを「イミュータブル（不変）」に設定することによるセキュリティと運用のメリットを解説しています。"
---

# ECRはイミュータブルにしておくと安全

## 概要

本記事では、AWS ECRのコンテナイメージを「イミュータブル（不変）」に設定することによるセキュリティと運用のメリットを解説しています。

*発行: 2024-10-08 / [[aws-testing-ecr-https-zenn-dev-levtech-articles-8feb6330f7c767-656f8f]]*

## 主要なトピック

- [[aws]]
- [[testing]]
- [[amazon-ecr]]
- [[cloudformation]]

## 詳細

- 本記事では、AWS ECRのコンテナイメージを「イミュータブル（不変）」に設定することによるセキュリティと運用のメリットを解説しています。
- ミュータブル（可変）設定の弊害
- **セキュリティリスク**: イメージの上書きが可能であるため、悪意のある変更や意図しない改ざんを防げない。
- **運用上の問題**: `latest`タグなどの使い回しにより、不具合発生時の安全な切り戻しが困難になる。
- イミュータブルにするメリット
- **保護の強化**: 一度プッシュしたタグの変更が不可能なため、悪意のある改ざんを防止できる。
- **一貫性の保証**: イメージとタグの対応が固定されるため、トラブル発生時に旧バージョンへ確実に切り戻せる。
- 設定方法の概要
- **Terraform**: `image_tag_mutability = "IMMUTABLE"`を指定。

*発行: 2024-10-08 / [[aws-testing-ecr-https-zenn-dev-levtech-articles-8feb6330f7c767-656f8f]]*

## 関連テーマ

- [[aws]]
- [[testing]]
- [[amazon-ecr]]
- [[cloudformation]]

## 出典

- `../60_Resources/ECRはイミュータブルにしておくと安全.md`
- https://zenn.dev/levtech/articles/8feb6330f7c767
