---
title: "ECSのENI上限引き上げ"
source: "https://qiita.com/nysalor/items/a5a06013d1c37b096885"
author:
  - "[[mumoshu]]"
published: 2019-08-01
created: 2026-05-01
description: "ECS with awsvpc on EC2 10年ぶりくらいに書くので口調を忘れました。昔の記事と違ってたらすいません。 TL;DR ENI上限を引き上げるには デフォルトのawsvpcTrunkingをenabledにすれば良い EC2 vs Fargate EC..."
tags:
  - "clippings"
---
### ECSにおけるENI上限引き上げの要約
本記事では、Amazon ECSをEC2インスタンス（awsvpcネットワーキングモード）で運用する際に発生する、ENI（Elastic Network Interface）の割り当て上限問題とその解決策について解説しています。

### 要点まとめ

* **課題：ENIの制限**
    * VPCネットワーキング使用時、インスタンスごとのENI数に上限があり、そのままでは大規模なタスク運用が困難。
* **解決策：awsvpcTrunkingの有効化**
    * `awsvpcTrunking`機能を有効にすることで、EC2インスタンスあたりのENI上限を大幅（約5倍）に緩和可能。
* **設定手順**
    * AWS CLIを使用して、アカウント全体に対して以下のコマンドでデフォルト設定を有効化する：
      `aws ecs put-account-setting-default --name awsvpcTrunking --value enabled`
    * 有効化後、新規に起動したコンテナインスタンスから適用される。
* **運用のポイント**
    * EC2インスタンスを用いる利点として、Fargateと比較したコスト面や、ログドライバの選択肢（json-file, fluentd等）、Docker execによるコンテナ操作の容易さが挙げられている。