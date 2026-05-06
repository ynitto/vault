---
title: "運用しているAWS CloudFormationのテンプレートをJSONからYAMLに移行する"
type: "topic"
tags:
  - "cloudformation"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/運用しているAWS CloudFormationのテンプレートをJSONからYAMLに移行する.md"
summary: "既存のAWS CloudFormationスタック（JSON形式）を、運用を維持したままYAML形式へシームレスに移行できるかを検証した内容です。"
---

# 運用しているAWS CloudFormationのテンプレートをJSONからYAMLに移行する

## 概要

既存のAWS CloudFormationスタック（JSON形式）を、運用を維持したままYAML形式へシームレスに移行できるかを検証した内容です。

*発行: 2018-09-04 / [[cloudformation-aws-cloudformation-json-yaml-01cf7d]]*

## 主要なトピック

- [[cloudformation]]

## 詳細

- 既存のAWS CloudFormationスタック（JSON形式）を、運用を維持したままYAML形式へシームレスに移行できるかを検証した内容です。
- 移行のポイント
- **移行手法:** `cfn-flip` ツールを使用することで、JSONテンプレートをYAMLへ容易に変換可能。
- **検証結果:** 既存スタックに対してYAMLテンプレートを用いて更新を実行したところ、問題なく完了し、追加したタグも正しく反映された。
- **結論:** 運用中のスタックであっても、JSONからYAMLへの移行はリスクなく実施可能。読みやすさやメンテナンス性の観点から、YAMLへの移行を推奨。

*発行: 2018-09-04 / [[cloudformation-aws-cloudformation-json-yaml-01cf7d]]*

## 関連テーマ

- [[cloudformation]]

## 出典

- `../60_Resources/運用しているAWS CloudFormationのテンプレートをJSONからYAMLに移行する.md`
- https://dev.classmethod.jp/articles/aws-cloudformation-migration-json-to-yaml/
