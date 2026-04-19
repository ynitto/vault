---
title: AWS::CloudFront::TrustStore CaCertificatesBundleS3Location - AWS CloudFormation
source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-truststore-cacertificatesbundles3location.html
author: null
published: null
created: 2026-04-19
description: The CA certificates bundle location in Amazon S3.
tags:
- resource/web
- aws
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/AWSCloudFrontTrustStore CaCertificatesBundleS3Location
  - AWS CloudFormation.md
copied_at: 2026-04-19 10:51:13+09:00
---
### 概要
本ドキュメントは、AWS CloudFormation における `AWS::CloudFront::TrustStore` のプロパティである `CaCertificatesBundleS3Location` の仕様を定義しています。これは、CloudFront トラストストアで使用する CA 証明書バンドルを S3 バケットから指定するための設定です。

### 主な構成要素

#### 1. 必須プロパティ
*   **Bucket**: 証明書バンドルが保存されている S3 バケット名。
*   **Key**: バケット内のファイルパス（キー）。
*   **Region**: バケットが存在する AWS リージョン（形式: `[a-z]{2}-[a-z]+-\d`）。

#### 2. 任意プロパティ
*   **Version**: S3 バケットのバージョン管理を使用している場合のオブジェクトバージョン。

#### 3. 更新時の挙動
*   すべてのプロパティの更新において「**中断なし (No interruption)**」でスタック更新が可能です。