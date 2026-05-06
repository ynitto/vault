---
title: "CloudFrontを経由しないALBへのアクセスを制限する"
type: "topic"
tags:
  - "aws"
  - "cloudfront"
  - "security"
  - "revcomm-hirashin"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/CloudFrontを経由しないALBへのアクセスを制限する.md"
summary: "CloudFrontとALBを用いた構成において、ALBへ直接アクセスされるセキュリティリスクを防ぐための2つの手法を解説しています。"
---

# CloudFrontを経由しないALBへのアクセスを制限する

## 概要

CloudFrontとALBを用いた構成において、ALBへ直接アクセスされるセキュリティリスクを防ぐための2つの手法を解説しています。

*発行: 2022-09-22 / [[aws-cloudfront-cloudfront-alb-https-bd45fd]]*

## 主要なトピック

- [[aws]]
- [[cloudfront]]
- [[security]]
- [[revcomm-hirashin]]

## 詳細

- CloudFrontとALBを用いた構成において、ALBへ直接アクセスされるセキュリティリスクを防ぐための2つの手法を解説しています。
- セキュリティ上の課題
- ALBがインターネット公開されているため、DNS名が漏洩するとCloudFront（およびWAF）を介さずに直接アクセスされる危険性がある。
- アクセス制限の手法
- 方法1：カスタムヘッダーの検証
- CloudFront側で秘密のカスタムヘッダーを付与し、ALB側でその値を検証する。
- **デメリット**: 秘匿情報（ヘッダー値）が平文で保存され、管理が煩雑になる。
- 方法2：AWS Managed Prefix Listの利用（推奨）
- CloudFrontのマネージドプレフィックスリストをソースとして、ALBのSecurity Groupを設定する。

*発行: 2022-09-22 / [[aws-cloudfront-cloudfront-alb-https-bd45fd]]*

## 関連テーマ

- [[aws]]
- [[cloudfront]]
- [[security]]
- [[revcomm-hirashin]]

## 出典

- `60_Resources/CloudFrontを経由しないALBへのアクセスを制限する.md`
- https://tech.revcomm.co.jp/cf-alb-access-restriction
