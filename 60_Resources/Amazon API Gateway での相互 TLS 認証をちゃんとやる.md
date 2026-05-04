---
title: "Amazon API Gateway での相互 TLS 認証をちゃんとやる"
source: "https://tech.aptpod.co.jp/entry/2021/12/06/070000"
author:
  - "[[aptpod_tech-writer]]"
published: 2021-12-06
created: 2026-04-30
description: "aptpod Advent Calendar 2021 の 6 日目を担当する、SRE チームの柏崎です。 弊社では、intdash を組み合わせたプロジェクトが多くあります。 とあるプロジェクトでは、車両に設置するエッジコンピュータが Amazon API Gateway を利用した API と通信する、というカスタマイズ部分があります。 先日このプロジェクトで、エッジコンピュータと Amazon API Gateway の通信に、セキュリティ強化のため相互 TLS 認証を導入することになりました。 今回は、Amazon API Gateway の相互 TLS 認証での課題を解決し、より厳格…"
tags:
  - "clippings"
---
### 記事の要約
Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この問題を Lambda オーソライザーを活用して解決し、失効済み証明書による不正アクセスを拒否する実装方法を解説しています。

### 重要なポイント

#### 課題
*   Amazon API Gateway の標準機能では、mTLS の証明書失効リスト（CRL）や OCSP による検証が行われない。
*   一度発行された証明書は、有効期限内であれば失効させてもアクセスが遮断されないリスクがある。

#### 解決策：Lambda オーソライザーの実装
*   **仕組み**: Lambda オーソライザーへ渡される証明書情報を利用し、Lambda 関数内で `certvalidator` 等を用いて失効状態を検証する。
*   **効率化**: トラストストアをハンドラ外で読み込み（グローバルスコープ）、Lambda のコールドスタート時にのみ S3 と通信することでレイテンシを抑える。
*   **設定**:
    *   API Gateway の認可キャッシュを有効にすることで、都度の Lambda 実行を回避可能。
    *   検証の結果、失効している場合は `Deny` ポリシーを返すことでアクセスを遮断する。
