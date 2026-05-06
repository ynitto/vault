---
title: "ECRのライフサイクルポリシーをCloudFormationで定義する方法とその設定指針"
type: "topic"
tags:
  - "aws"
  - "cloudformation"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ECRのライフサイクルポリシーをCloudFormationで定義する方法とその設定指針.md"
summary: "ECRライフサイクルポリシーのCloudFormationでの設定方法"
---

# ECRのライフサイクルポリシーをCloudFormationで定義する方法とその設定指針

## 概要

ECRライフサイクルポリシーのCloudFormationでの設定方法

*発行: 2019-02-15 / [[aws-cloudformation-ecr-cloudformation-https-165eab]]*

## 主要なトピック

- [[aws]]
- [[cloudformation]]

## 詳細

- 本記事は、ECRのコンテナイメージによるストレージコスト増大を防ぐための「ライフサイクルポリシー」を、CloudFormationテンプレートで定義する方法について解説しています。
- 要点まとめ
- **ライフサイクルポリシーの必要性**
- コンテナイメージの蓄積によるコスト増加を抑制するため、不要なイメージを自動削除する設定が推奨されます。
- **CloudFormation設定の注意点**
- `LifecyclePolicyText` プロパティは **JSON形式のみ** 対応しています。
- YAMLテンプレート内で指定する場合、可読性のために「リテラルスタイル（`|`）」を用いるのがおすすめです。
- **効率的なポリシー作成方法**
- GUIで設定を試行し、AWS CLIの `get-lifecycle-policy` で出力されたJSONを取得して活用すると効率的です。

*発行: 2019-02-15 / [[aws-cloudformation-ecr-cloudformation-https-165eab]]*

## 関連テーマ

- [[aws]]
- [[cloudformation]]

## 出典

- `60_Resources/ECRのライフサイクルポリシーをCloudFormationで定義する方法とその設定指針.md`
- https://dev.classmethod.jp/articles/cfn-for-ecr-lifecyclepolicy/
