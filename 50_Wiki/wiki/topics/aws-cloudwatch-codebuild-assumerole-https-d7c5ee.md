---
title: "CodeBuildのビルド内でAssumeRole(クロスアカウントアクセス)する方法とハマった話"
type: "topic"
tags:
  - "aws"
  - "cloudwatch"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/CodeBuildのビルド内でAssumeRole(クロスアカウントアクセス)する方法とハマった話.md"
summary: "CodeBuildでクロスアカウントAssumeRoleを行う方法と注意点"
---

# CodeBuildのビルド内でAssumeRole(クロスアカウントアクセス)する方法とハマった話

## 概要

CodeBuildでクロスアカウントAssumeRoleを行う方法と注意点

*発行: 2019-09-18 / [[aws-cloudwatch-codebuild-assumerole-https-d7c5ee]]*

## 主要なトピック

- [[aws]]
- [[cloudwatch]]

## 詳細

- 本記事は、AWS CodeBuildから別アカウントのIAMロールへAssumeRoleする方法と、クロスアカウントでのECR連携における制約についての解説です。
- *1. CodeBuildからAssumeRoleする手順**
- **IAM設定**:
- 実行先アカウント（account-a）で、実行元アカウント（account-b）のCodeBuildサービスロールを信頼するロールを作成。
- account-bのCodeBuildサービスロールに `sts:AssumeRole` の許可を付与。
- **buildspec.ymlでの実装**:
- **AWS CLIプロファイル利用**: `pre_build`フェーズで設定ファイル（`config`）を作成し、環境変数 `AWS_CONFIG_FILE` で読み込ませる。
- **環境変数利用**: `sts assume-role`コマンドで取得した一時クレデンシャルを `AWS_ACCESS_KEY_ID` 等の環境変数にエクスポートする。
- *2. ECRクロスアカウント連携のハマりポイント**

*発行: 2019-09-18 / [[aws-cloudwatch-codebuild-assumerole-https-d7c5ee]]*

## 関連テーマ

- [[aws]]
- [[cloudwatch]]

## 出典

- `60_Resources/CodeBuildのビルド内でAssumeRole(クロスアカウントアクセス)する方法とハマった話.md`
- https://dev.classmethod.jp/articles/assumerole-in-codebuild/
