---
title: "AWS CloudFormationでWAFを設定したELBを構築しよう"
source: "https://qiita.com/s_horikoshi/items/9b5da901601e947114ec"
author:
  - "[[s_horikoshi]]"
published: 2021-02-03
created: 2026-05-01
description: "はじめに AWS CloudFormationを利用してVPC構築のテンプレートのサンプルです。 テンプレートの概要が分からない場合は、はじめてのAWS CloudFormationテンプレートを理解するを参考にしてください。 コードはGitHubにもあります。 今回は、..."
tags:
  - "clippings"
---
### 記事の要約
本記事は、AWS CloudFormationを使用して、WAF（Web Application Firewall）を統合したELB（Elastic Load Balancer）環境を構築するためのテンプレートと手順を紹介しています。

### 構築内容の要点
- **ネットワーク**: VPC、Publicサブネット（2つ）、インターネットゲートウェイ、ルートテーブルの設定。
- **セキュリティ**: 80ポートを許可するセキュリティグループの作成。
- **ELB**: Application Load Balancerの構築およびヘルスチェック設定を含むターゲットグループの設定。
- **WAF**: SQLインジェクション、XSS攻撃対策、およびカスタムヘッダー認証（トークン検証）を含むルールグループとWeb ACLの設定。

### 構築のポイント
- **テンプレート化**: システム名や環境名（dev/stg/prod）をパラメータ化することで、再利用可能な構成管理を実現。
- **モジュール化**: ネットワーク、セキュリティグループ、ELB、WAFの4つのスタックに分割して管理。
- **自動化**: `create_stacks.sh` および `delete_stacks.sh` スクリプトを用意し、コマンド操作によるスタックの一括作成・削除が可能。