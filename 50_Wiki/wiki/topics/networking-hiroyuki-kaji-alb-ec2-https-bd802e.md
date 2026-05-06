---
title: "ALBとバックエンドEC2間をHTTPS通信させてみた"
type: "topic"
tags:
  - "networking"
  - "hiroyuki-kaji"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/ALBとバックエンドEC2間をHTTPS通信させてみた.md"
summary: "本記事は、AWSのApplication Load Balancer (ALB) とバックエンドのEC2インスタンス間でHTTPS通信を確立する方法の解説…"
---

# ALBとバックエンドEC2間をHTTPS通信させてみた

## 概要

本記事は、AWSのApplication Load Balancer (ALB) とバックエンドのEC2インスタンス間でHTTPS通信を確立する方法の解説です。ALBでSSLオフロード（ACMを利用）しつつ、ALBからEC2間もHTTPSで通信させる構成手順を紹介しています。

*発行: 2026-05-20 / [[networking-hiroyuki-kaji-alb-ec2-https-bd802e]]*

## 主要なトピック

- [[networking]]
- [[hiroyuki-kaji]]

## 詳細

- 本記事は、AWSのApplication Load Balancer (ALB) とバックエンドのEC2インスタンス間でHTTPS通信を確立する方法の解説です。ALBでSSLオフロード（ACMを利用）しつつ、ALBからEC2間もHTTPSで通信させる構成手順を紹介しています。
- ポイント
- **目的**: ALBとEC2間を暗号化（HTTPS）して通信する。
- **構成**:
- クライアント・ALB間：ACM証明書
- ALB・EC2間：自己署名証明書（オレオレ証明書）
- **実装手順の要点**:
- **EC2構築**: `mod_ssl`をインストールしてHTTPSサーバを構築。
- **証明書作成**: `openssl`を用いて秘密鍵、公開鍵(CSR)、自己証明書を作成し、ApacheのConfigを修正。

*発行: 2026-05-20 / [[networking-hiroyuki-kaji-alb-ec2-https-bd802e]]*

## 関連テーマ

- [[networking]]
- [[hiroyuki-kaji]]

## 出典

- `../60_Resources/ALBとバックエンドEC2間をHTTPS通信させてみた.md`
- https://dev.classmethod.jp/articles/alb-backend-https/
