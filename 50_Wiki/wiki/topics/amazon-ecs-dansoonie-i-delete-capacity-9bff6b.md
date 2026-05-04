---
title: "How can I delete a capacity provider that is not associated with a cluster but claims to be associated to one when attempting to delete?"
type: "topic"
tags:
  - "amazon-ecs"
  - "dansoonie"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How can I delete a capacity provider that is not associated with a cluster but claims to be associated to one when attempting to delete.md"
summary: "ECSキャパシティプロバイダ削除エラーの解決策要約"
---

# How can I delete a capacity provider that is not associated with a cluster but claims to be associated to one when attempting to delete?

## 概要

ECSキャパシティプロバイダ削除エラーの解決策要約

*発行: 2024-01-10 / [[amazon-ecs-dansoonie-i-delete-capacity-9bff6b]]*

## 主要なトピック

- [[amazon-ecs]]
- [[dansoonie]]

## 詳細

- ECSのキャパシティプロバイダが「クラスターに紐付いている」と認識され削除できない問題に対し、以下の方法で解決可能です。
- 問題の核心
- AWSの管理画面やCLIで紐付けが確認できなくても、内部的にはクラスターに関連付けられている状態。
- 特にTerraform等で自動構成している場合、隠れた関連付けが解除されていないことが多い。
- 解決手順（推奨）
- 1. **関連付けの再定義**: `PutClusterCapacityProviders` APIを使用して、削除したいプロバイダを明示的に含めて更新を試みる。
- 2. **デフォルトの考慮**: `FARGATE` や `FARGATE_SPOT` など、デフォルトで存在するプロバイダもAPI呼び出し時に含める必要がある（省略すると関連付けが外れない場合がある）。
- 3. **関連付けの解除**: プロバイダをAPIでクラスターに再登録し、その後改めて構成を修正することで、正常に「関連付け解除（＝削除可能状態）」へ遷移させる。
- 注意事項

*発行: 2024-01-10 / [[amazon-ecs-dansoonie-i-delete-capacity-9bff6b]]*

## 関連テーマ

- [[amazon-ecs]]
- [[dansoonie]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How can I delete a capacity provider that is not associated with a cluster but claims to be associated to one when attempting to delete.md`
- https://repost.aws/questions/QUl46YGJi5TqOAtVWerPGsHA/how-can-i-delete-a-capacity-provider-that-is-not-associated-with-a-cluster-but-claims-to-be-associated-to-one-when-attempting-to-delete
