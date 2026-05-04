---
title: "ECRのライフサイクルポリシーをCloudFormationで定義する方法とその設定指針"
source: "https://dev.classmethod.jp/articles/cfn-for-ecr-lifecyclepolicy/"
author:
  - "[[濱田孝治（ハマコー）]]"
published: 2019-02-15
created: 2026-05-01
description: "ECRの無駄を省くためのライフサイクルポリシーをCloudFormationから実施する方法の紹介です。"
tags:
  - "clippings"
---
### ECRライフサイクルポリシーのCloudFormationでの設定方法

本記事は、ECRのコンテナイメージによるストレージコスト増大を防ぐための「ライフサイクルポリシー」を、CloudFormationテンプレートで定義する方法について解説しています。

#### 要点まとめ
*   **ライフサイクルポリシーの必要性**
    *   コンテナイメージの蓄積によるコスト増加を抑制するため、不要なイメージを自動削除する設定が推奨されます。
*   **CloudFormation設定の注意点**
    *   `LifecyclePolicyText` プロパティは **JSON形式のみ** 対応しています。
    *   YAMLテンプレート内で指定する場合、可読性のために「リテラルスタイル（`|`）」を用いるのがおすすめです。
*   **効率的なポリシー作成方法**
    *   GUIで設定を試行し、AWS CLIの `get-lifecycle-policy` で出力されたJSONを取得して活用すると効率的です。
*   **運用中のリポジトリへの適用**
    *   既存のリポジトリには AWS CLI の `put-lifecycle-policy` コマンドで後から設定が可能です。
*   **推奨設定**
    *   特定の要件がない場合、「最新のイメージ20個を残して古いものを自動削除」する設定がシンプルかつ実用的です。