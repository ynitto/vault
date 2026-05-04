---
title: "AWS::CloudFront::TrustStore CaCertificatesBundleS3Location - AWS CloudFormation"
type: "topic"
tags:
  - "aws"
  - "cloudformation"
  - "cloudfront"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AWSCloudFrontTrustStore CaCertificatesBundleS3Location - AWS CloudFormation.md"
summary: "本ドキュメントは、AWS CloudFormation における `AWS::CloudFront::TrustStore` のプロパティである `CaC…"
---

# AWS::CloudFront::TrustStore CaCertificatesBundleS3Location - AWS CloudFormation

## 概要

本ドキュメントは、AWS CloudFormation における `AWS::CloudFront::TrustStore` のプロパティである `CaCertificatesBundleS3Location` の仕様を定義しています。これは、CloudFront トラストストアで使用する CA 証明書バンドルを S3 バケットから指定するための設定です。

## 主要なトピック

- [[aws]]
- [[cloudformation]]
- [[cloudfront]]

## 詳細

- 本ドキュメントは、AWS CloudFormation における `AWS::CloudFront::TrustStore` のプロパティである `CaCertificatesBundleS3Location` の仕様を定義しています。これは、CloudFront トラストストアで使用する CA 証明書バンドルを S3 バケットから指定するための設定です。
- 主な構成要素
- 1. 必須プロパティ
- **Bucket**: 証明書バンドルが保存されている S3 バケット名。
- **Key**: バケット内のファイルパス（キー）。
- **Region**: バケットが存在する AWS リージョン（形式: `[a-z]{2}-[a-z]+-\d`）。
- 2. 任意プロパティ
- **Version**: S3 バケットのバージョン管理を使用している場合のオブジェクトバージョン。
- 3. 更新時の挙動

## 関連テーマ

- [[aws]]
- [[cloudformation]]
- [[cloudfront]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/AWSCloudFrontTrustStore CaCertificatesBundleS3Location - AWS CloudFormation.md`
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-truststore-cacertificatesbundles3location.html
