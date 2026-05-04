---
title: "運用しているAWS CloudFormationのテンプレートをJSONからYAMLに移行する"
source: "https://dev.classmethod.jp/articles/aws-cloudformation-migration-json-to-yaml/"
author:
  - "[[武田隆志]]"
published: 2018-09-04
created: 2026-05-01
description: "現在運用しているAWS CloudFormationスタックがあるのですが、そのテンプレートはJSONで書かれています。それをYAMLに書き換えた上でシームレスにスタック更新が可能かが調べても分からなかったため試してみました。"
tags:
  - "clippings"
---
### 記事の要約
既存のAWS CloudFormationスタック（JSON形式）を、運用を維持したままYAML形式へシームレスに移行できるかを検証した内容です。

### 移行のポイント
- **移行手法:** `cfn-flip` ツールを使用することで、JSONテンプレートをYAMLへ容易に変換可能。
- **検証結果:** 既存スタックに対してYAMLテンプレートを用いて更新を実行したところ、問題なく完了し、追加したタグも正しく反映された。
- **結論:** 運用中のスタックであっても、JSONからYAMLへの移行はリスクなく実施可能。読みやすさやメンテナンス性の観点から、YAMLへの移行を推奨。