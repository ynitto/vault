---
title: "AWS CloudFormationでWAFを設定したELBを構築しよう"
type: "topic"
tags:
  - "aws"
  - "authentication"
  - "cloudformation"
  - "networking"
  - "s-horikoshi"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/AWS CloudFormationでWAFを設定したELBを構築しよう.md"
summary: "本記事は、AWS CloudFormationを使用して、WAF（Web Application Firewall）を統合したELB（Elastic Lo…"
---

# AWS CloudFormationでWAFを設定したELBを構築しよう

## 概要

本記事は、AWS CloudFormationを使用して、WAF（Web Application Firewall）を統合したELB（Elastic Load Balancer）環境を構築するためのテンプレートと手順を紹介しています。

*発行: 2021-02-03 / [[aws-authentication-aws-cloudformation-waf-7f41c8]]*

## 主要なトピック

- [[aws]]
- [[authentication]]
- [[cloudformation]]
- [[networking]]
- [[s-horikoshi]]

## 詳細

- 本記事は、AWS CloudFormationを使用して、WAF（Web Application Firewall）を統合したELB（Elastic Load Balancer）環境を構築するためのテンプレートと手順を紹介しています。
- 構築内容の要点
- **ネットワーク**: VPC、Publicサブネット（2つ）、インターネットゲートウェイ、ルートテーブルの設定。
- **セキュリティ**: 80ポートを許可するセキュリティグループの作成。
- **ELB**: Application Load Balancerの構築およびヘルスチェック設定を含むターゲットグループの設定。
- **WAF**: SQLインジェクション、XSS攻撃対策、およびカスタムヘッダー認証（トークン検証）を含むルールグループとWeb ACLの設定。
- 構築のポイント
- **テンプレート化**: システム名や環境名（dev/stg/prod）をパラメータ化することで、再利用可能な構成管理を実現。
- **モジュール化**: ネットワーク、セキュリティグループ、ELB、WAFの4つのスタックに分割して管理。

*発行: 2021-02-03 / [[aws-authentication-aws-cloudformation-waf-7f41c8]]*

## 関連テーマ

- [[aws]]
- [[authentication]]
- [[cloudformation]]
- [[networking]]
- [[s-horikoshi]]

## 出典

- `../60_Resources/AWS CloudFormationでWAFを設定したELBを構築しよう.md`
- https://qiita.com/s_horikoshi/items/9b5da901601e947114ec
