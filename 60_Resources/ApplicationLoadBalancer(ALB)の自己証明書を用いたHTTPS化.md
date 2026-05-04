---
title: "ApplicationLoadBalancer(ALB)の自己証明書を用いたHTTPS化"
source: "https://qiita.com/klynk2024/items/76db8d65838857227bd9"
author:
  - "[[ykarakita]]"
published: 2022-05-30
created: 2026-05-01
description: "概要 ALBの利用においてHTTPS化を行うための方法。 ALBのDNS名と同名の自己証明書を作成し、ACMへインポート。後、ALBに適用すればできると想定。 前提 構成は以下の通り。 構成のポイントは以下。 ・ALBはプライベート ・ALB－バックエンドサーバ(..."
tags:
  - "clippings"
---
### 概要
AWSのApplication Load Balancer (ALB) を自己署名証明書を使用してHTTPS化する手順について解説した記事です。

### 要点
- **目的**: プライベートなALB環境において、自己証明書を作成・適用してHTTPS通信を有効化する。
- **構築手順**:
    1. **SSL証明書の作成**: OpenSSLを使用し、秘密鍵、CSR、および有効期限1年の証明書を生成。
    2. **ACMへのインポート**: 作成した証明書ファイルをAWS Certificate Manager (ACM) にインポート。
    3. **ALB設定変更**: ALBのリスナーをHTTPS (443ポート) に変更し、インポートした証明書をアタッチ。
- **動作確認**: 自己署名証明書のため、`curl`コマンド実行時に`-k`オプション（検証無視）を使用して通信を確認。