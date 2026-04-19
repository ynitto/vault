---
created: 2026-04-19T10:05:19+09:00
source: 00_Inbox/Clippings/信頼は相互に Amazon CloudFront が mTLS をサポート.md
tags: [ナレッジ, AWS, CloudFront, Security]
---

# CloudFront mTLSとKVS活用

## 概要
CloudFront の mTLS 対応により、エッジでの認証・失効管理・リリース制御をより細かく組めるようになった。KVS と TrustStore を合わせて見ると、ゼロトラスト寄りの構成を CDN レイヤで実現する道筋が見える。

## 詳細
### mTLS の使い分け
- **Required**: すべての接続でクライアント証明書を必須にする
- **Optional**: 段階導入や混在環境向け。証明書ベースの接続と通常接続を共存させる

### KVS / TrustStore との組み合わせ
- TrustStore で信頼する証明書束を管理する
- KVS で失効対象やリリース制御フラグを保持する
- Connection Functions と合わせて、TLS ハンドシェイク時に条件分岐させる

### 使いどころ
- 社内アプリや B2B API のクライアント認証
- デバイス証明書を使う IoT 系アクセス制御
- 段階リリースや緊急停止フラグのエッジ判定

## 関連リンク
- [[10_Daily/2026-04-19]]
- [[11_Weekly/2026-W16]]

## 出典・参照
- `00_Inbox/Clippings/信頼は相互に Amazon CloudFront が mTLS をサポート.md`
- `00_Inbox/Clippings/Amazon CloudFront KeyValueStoreを活用した記事のリリース制御.md`
- `00_Inbox/Clippings/AWSCloudFrontTrustStore CaCertificatesBundleS3Location - AWS CloudFormation.md`
- `00_Inbox/Clippings/describe-key-value-store — AWS CLI 2.34.32 Command Reference.md`
- `00_Inbox/Clippings/【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点.md`
