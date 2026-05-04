---
title: "CloudFormationでクロスアカウントアクセスロールを作成してみた"
type: "topic"
tags:
  - "aws"
  - "cloudformation"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/CloudFormationでクロスアカウントアクセスロールを作成してみた.md"
summary: "CloudFormationを使用して、別のアカウントのIAMユーザーが対象アカウントのリソースを操作するための「クロスアカウントアクセスロール」を作成す…"
---

# CloudFormationでクロスアカウントアクセスロールを作成してみた

## 概要

CloudFormationを使用して、別のアカウントのIAMユーザーが対象アカウントのリソースを操作するための「クロスアカウントアクセスロール」を作成する方法を解説しています。

*発行: 2022-09-12 / [[aws-cloudformation-cloudformation-https-dev-classmethod-jp-articles-crea-20f8ac]]*

## 主要なトピック

- [[aws]]
- [[cloudformation]]

## 詳細

- CloudFormationを使用して、別のアカウントのIAMユーザーが対象アカウントのリソースを操作するための「クロスアカウントアクセスロール」を作成する方法を解説しています。
- 要点
- **クロスアカウントアクセスロールとは**
- アカウントBのIAMユーザーが、アカウントAのIAMロールを使用してリソースを操作する仕組み。
- 再ログイン不要で効率的に複数アカウントを管理可能。
- **CloudFormationの工夫点**
- `Parameters` でユーザー名やアカウントIDを動的に指定可能。
- `AssumeRolePolicyDocument` で特定のIAMユーザーのみがロールを引き受けられるよう制限。
- `Condition` に `aws:MultiFactorAuthPresent: true` を含め、MFA必須によるセキュリティ強化を実施。

*発行: 2022-09-12 / [[aws-cloudformation-cloudformation-https-dev-classmethod-jp-articles-crea-20f8ac]]*

## 関連テーマ

- [[aws]]
- [[cloudformation]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/CloudFormationでクロスアカウントアクセスロールを作成してみた.md`
- https://dev.classmethod.jp/articles/created_a_cross-account_access_role_in_cloudformation/
