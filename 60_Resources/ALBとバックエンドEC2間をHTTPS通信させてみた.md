---
title: "ALBとバックエンドEC2間をHTTPS通信させてみた"
source: "https://dev.classmethod.jp/articles/alb-backend-https/"
author:
  - "[[hiroyuki kaji]]"
published: 2026-05-20
created: 2026-05-01
description: "ALBのターゲットグループ設定でHTTPSが選択できるため、バックエンドEC2とのHTTPS通信設定し通信できるのか確認してみました。 また、利用したサーバ証明書は、ALBはACM、EC2は自己証明書（オレオレ証明書）を利用してみました。どなたかのお役に立てれば光栄です。"
tags:
  - "clippings"
---
### 要約
本記事は、AWSのApplication Load Balancer (ALB) とバックエンドのEC2インスタンス間でHTTPS通信を確立する方法の解説です。ALBでSSLオフロード（ACMを利用）しつつ、ALBからEC2間もHTTPSで通信させる構成手順を紹介しています。

### ポイント
- **目的**: ALBとEC2間を暗号化（HTTPS）して通信する。
- **構成**: 
    - クライアント・ALB間：ACM証明書
    - ALB・EC2間：自己署名証明書（オレオレ証明書）
- **実装手順の要点**:
    - **EC2構築**: `mod_ssl`をインストールしてHTTPSサーバを構築。
    - **証明書作成**: `openssl`を用いて秘密鍵、公開鍵(CSR)、自己証明書を作成し、ApacheのConfigを修正。
    - **ALB設定**: ターゲットグループのプロトコルを「HTTPS」に設定。
- **結果**: ターゲットグループのプロトコル設定を変更するだけで、バックエンドとのHTTPS通信が容易に実現可能。