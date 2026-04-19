---
task_id: 2026-04-19-CloudFrontmTLS設計メモ
created: 2026-04-19T10:51:13+09:00
status: Proposed
urgency: 中
priority: 中
effort: M
tags:
  - task
  - aws
  - cloudfront
source_daily:
  - - 10_Daily/2026-04-19
---

# CloudFrontmTLS設計メモ

## 背景・目的
CloudFront mTLS と KVS / TrustStore の組み合わせは、今後の案件で再利用可能な実装パターンになりそう。PoC 観点で先に整理しておくと、必要になったときの立ち上がりが速い。

## やること（ステップ）
- [ ] Required / Optional のどちらを基本方針にするか、ユースケース別に判断基準を書く
- [ ] TrustStore、Connection Functions、KVS の役割を 1 枚にまとめる
- [ ] PoC の第 1 段階を mTLS 接続確認、第 2 段階を失効チェック連携に分けて整理する

## 参考情報・出典
- [[60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート]]
- [[60_Resources/Amazon CloudFront KeyValueStoreを活用した記事のリリース制御]]
- [[60_Resources/AWSCloudFrontTrustStore CaCertificatesBundleS3Location - AWS CloudFormation]]
- [[60_Resources/describe-key-value-store — AWS CLI 2.34.32 Command Reference]]

## 完了条件
mTLS / TrustStore / KVS の関係が 1 枚で説明でき、PoC をどう分割するかが決まっている。

## メモ・懸念点
技術面よりも、どのクライアントに証明書を配るかや失効管理の運用方針が先に詰まりやすい。
