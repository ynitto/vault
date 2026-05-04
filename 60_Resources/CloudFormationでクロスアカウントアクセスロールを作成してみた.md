---
title: "CloudFormationでクロスアカウントアクセスロールを作成してみた"
source: "https://dev.classmethod.jp/articles/created_a_cross-account_access_role_in_cloudformation/"
author:
  - "[[小林陸]]"
published: 2022-09-12
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 概要
CloudFormationを使用して、別のアカウントのIAMユーザーが対象アカウントのリソースを操作するための「クロスアカウントアクセスロール」を作成する方法を解説しています。

### 要点
- **クロスアカウントアクセスロールとは**
  - アカウントBのIAMユーザーが、アカウントAのIAMロールを使用してリソースを操作する仕組み。
  - 再ログイン不要で効率的に複数アカウントを管理可能。

- **CloudFormationの工夫点**
  - `Parameters` でユーザー名やアカウントIDを動的に指定可能。
  - `AssumeRolePolicyDocument` で特定のIAMユーザーのみがロールを引き受けられるよう制限。
  - `Condition` に `aws:MultiFactorAuthPresent: true` を含め、MFA必須によるセキュリティ強化を実施。

- **作成時の注意点**
  - IAM関連リソースの作成には `--capabilities CAPABILITY_NAMED_IAM` オプションが必須。
  - ロールには過剰な権限（PowerUserなど）を与えず、必要最小限の権限（最小権限の原則）を付与することが推奨される。