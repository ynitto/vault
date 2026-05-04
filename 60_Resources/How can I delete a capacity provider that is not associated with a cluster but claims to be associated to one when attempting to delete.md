---
title: "How can I delete a capacity provider that is not associated with a cluster but claims to be associated to one when attempting to delete?"
source: "https://repost.aws/questions/QUl46YGJi5TqOAtVWerPGsHA/how-can-i-delete-a-capacity-provider-that-is-not-associated-with-a-cluster-but-claims-to-be-associated-to-one-when-attempting-to-delete"
author:
  - "[[dansoonie]]"
published: 2024-01-10
created: 2026-05-01
description: "Here is my situation in short* Capacity provider cannot be deleted because it is said to be associated with a cluster* The association to the cluster of the capacity provider cannot be confirmed..."
tags:
  - "clippings"
---
### ECSキャパシティプロバイダ削除エラーの解決策要約

ECSのキャパシティプロバイダが「クラスターに紐付いている」と認識され削除できない問題に対し、以下の方法で解決可能です。

#### 問題の核心
* AWSの管理画面やCLIで紐付けが確認できなくても、内部的にはクラスターに関連付けられている状態。
* 特にTerraform等で自動構成している場合、隠れた関連付けが解除されていないことが多い。

#### 解決手順（推奨）
1. **関連付けの再定義**: `PutClusterCapacityProviders` APIを使用して、削除したいプロバイダを明示的に含めて更新を試みる。
2. **デフォルトの考慮**: `FARGATE` や `FARGATE_SPOT` など、デフォルトで存在するプロバイダもAPI呼び出し時に含める必要がある（省略すると関連付けが外れない場合がある）。
3. **関連付けの解除**: プロバイダをAPIでクラスターに再登録し、その後改めて構成を修正することで、正常に「関連付け解除（＝削除可能状態）」へ遷移させる。

#### 注意事項
* 削除前に、そのプロバイダを使用している**すべてのECSサービスから設定を削除**（または代替へ切り替え）しておく必要があります。
* `ResourceInUseException` が発生する場合、上記の手順で一度強制的にクラスター構成を上書き適用するのが最も確実な対処法です。
