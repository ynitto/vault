---
title: "【基礎から学ぶ】VPCのDNSについてまとめてみた - サーバーワークスエンジニアブログ"
source: "https://blog.serverworks.co.jp/tech/2017/04/03/vpc-dns-matome/"
author:
  - "[[serverworks]]"
  - "[[記事一覧]]"
published: 2017-04-03
created: 2026-05-01
description: "こんにちは、技術３課の紅林です。花粉症なので、最近は花粉にやられて目がしょぼしょぼです。 さて、今回はVPCのDNSの設定/機能についてまとめてみました。目次は以下の通りです。 VPCのDNSについて VPCのDNSに関する設定 DNS Resolution DNS Hostname DHCP Options Sets VPCのDNSに関する機能 AmazonProvidedDNS パブリックDNSホスト名、プライベートDNSホスト名 設定と有効になる機能の関係性 検証 まとめ VPCのDNSについて VPCにはDNSに関するいくつかの設定/機能があります。まずはそれぞれを簡単に記します。 V…"
tags:
  - "clippings"
---
### 【基礎から学ぶ】VPCのDNS要約
VPCにおけるDNSの仕組み、設定項目、および各設定が機能に与える影響についての解説記事です。

### 要点まとめ
*   **VPCのDNS設定項目**
    *   **DNS Resolution:** AmazonProvidedDNS（169.254.169.253）の利用可否を制御。
    *   **DNS Hostname:** インスタンスへのパブリックDNSホスト名付与を制御。
    *   **DHCP Options Sets:** ドメイン名やDNSサーバーの設定を管理。

*   **VPCのDNS機能**
    *   **AmazonProvidedDNS:** VPC内の名前解決を行う標準DNS。
    *   **ホスト名:** パブリック/プライベートDNSホスト名がインスタンスに自動割り当てされる。

*   **設定と機能の関係**
    *   「DNS Resolution」と「DNS Hostname」の両方を有効にすることで、パブリックDNSホスト名が付与され、かつAmazonProvidedDNSでのプライベートDNS解決が可能になる。
    *   片方でも無効の場合、AmazonProvidedDNSでプライベートDNS名を解決できなくなるため注意が必要。