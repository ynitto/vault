---
title: "信頼は相互に: Amazon CloudFront が mTLS をサポート"
source: "https://aws.amazon.com/jp/blogs/news/trust-goes-both-ways-amazon-cloudfront-now-supports-viewer-mtls/"
author:
  - "[[Yutaka Oka]]"
  - "[[Tomoya Kudo]]"
  - "[[and Sagar Desarda]]"
published: 2025-12-04
created: 2026-04-19
description: "本日より、Amazon CloudFront はエンドユーザーから CloudFront への相互 TLS 認証 (mTLS) をサポートし、高度に分散された機密性の高いアプリケーションのセキュリティを強化します。現代のアーキテクチャでは、クライアント・サーバー間の通信を保護するには標準的な TLS 以上のものが必要であり、mTLS は相互の認証を強制することでこのモデルを拡張します。これにより、データが交換される前にクライアントとサーバーの両方が互いの身元を検証することが保証されます。さらに、この新機能はプロトコルレベルできめ細かなアクセス制御と ID 検証を強制し、規制環境における監査とコンプライアンスを合理化します。"
tags:
  - "clippings"
---
### Amazon CloudFront が mTLS をサポート
Amazon CloudFront は、エンドユーザーと CloudFront 間の相互 TLS 認証 (mTLS) をサポートしました。これにより、アプリケーションのセキュリティ強化とアクセス制御の最適化が可能になります。

#### 主なメリット
- **ゼロトラストの実現**: クライアントとサーバー双方が証明書を検証し、認証を相互に行うことで信頼を確立。
- **多様なユースケース**: 金融取引（PCI DSS）、IoTデバイス認証、企業内アプリのアクセス制限、医療データ保護などに有効。
- **運用の効率化**: AWS Private CA や Trust Store と統合し、証明書のプロビジョニングから検証までを自動化。

#### 実装と管理のポイント
- **柔軟なモード選択**: 
    - **Required**: すべての接続に有効な証明書を必須とする。
    - **Optional**: mTLS と非 mTLS の混在を許可し、無効な証明書のみを拒否する。
- **高度な制御**: 
    - **Connection Functions**: TLS ハンドシェイク時にカスタムロジックを実行し、証明書情報に基づいた柔軟な許可・拒否が可能。
    - **KeyValueStore との連携**: 失効した証明書のシリアル番号を管理し、リアルタイムで拒否する失効チェックを実装可能。
- **詳細な可視化**: 「Connection Logs」を使用して、mTLS ハンドシェイクの成功・失敗を追跡・トラブルシューティングできる。