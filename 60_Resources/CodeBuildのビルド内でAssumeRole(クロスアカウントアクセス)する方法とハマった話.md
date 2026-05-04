---
title: "CodeBuildのビルド内でAssumeRole(クロスアカウントアクセス)する方法とハマった話"
source: "https://dev.classmethod.jp/articles/assumerole-in-codebuild/"
author:
  - "[[佐伯航]]"
published: 2019-09-18
created: 2026-05-01
description: "CodeBuildからAssumeRoleする方法はズバリこれだ！ってエントリがなかった気がするので書きました。今更感がありますがご了承ください。また、CodePipelineで少しハマったので共有目的で本エントリを書きました。"
tags:
  - "clippings"
---
### CodeBuildでクロスアカウントAssumeRoleを行う方法と注意点

本記事は、AWS CodeBuildから別アカウントのIAMロールへAssumeRoleする方法と、クロスアカウントでのECR連携における制約についての解説です。

#### **1. CodeBuildからAssumeRoleする手順**
- **IAM設定**: 
    - 実行先アカウント（account-a）で、実行元アカウント（account-b）のCodeBuildサービスロールを信頼するロールを作成。
    - account-bのCodeBuildサービスロールに `sts:AssumeRole` の許可を付与。
- **buildspec.ymlでの実装**:
    - **AWS CLIプロファイル利用**: `pre_build`フェーズで設定ファイル（`config`）を作成し、環境変数 `AWS_CONFIG_FILE` で読み込ませる。
    - **環境変数利用**: `sts assume-role`コマンドで取得した一時クレデンシャルを `AWS_ACCESS_KEY_ID` 等の環境変数にエクスポートする。

#### **2. ECRクロスアカウント連携のハマりポイント**
- **事象**: 他AWSアカウントからのECRへのイメージPUSHをトリガーにCodePipelineを開始させようとしたが、自動起動しなかった。
- **原因**: 他アカウントからのECR操作はCloudWatch Events（EventBridge）の対象となるイベントが配信されない仕様のため。
- **解決策（ワークアラウンド）**: 
    - 他アカウントから直接PUSHせず、一度CodeBuild内でAssumeRoleを実行してから対象アカウントのECRへPUSHすることで、イベントを正常に発生させる。

#### **重要な教訓**
- AWSサービス間の連携トラブル時は、CloudTrailログを確認することで「イベントが発生しているか」「必要なフィールドが含まれているか」の切り分けが可能。
