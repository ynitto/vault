---
title: "【初心者向け】ELBからプライベートサブネットへのアクセスに困った話 - サーバーワークスエンジニアブログ"
type: "topic"
tags:
  - "swx-isoya"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【初心者向け】ELBからプライベートサブネットへのアクセスに困った話 - サーバーワークスエンジニアブログ.md"
summary: "AWS初心者がプライベートサブネット上のWebサーバーに対してELB（ALB）経由でアクセスできないトラブルに直面し、その解決過程を記録した記事です。AL…"
---

# 【初心者向け】ELBからプライベートサブネットへのアクセスに困った話 - サーバーワークスエンジニアブログ

## 概要

AWS初心者がプライベートサブネット上のWebサーバーに対してELB（ALB）経由でアクセスできないトラブルに直面し、その解決過程を記録した記事です。ALBの配置要件（サブネット設計）の理解不足が原因であり、適切なパブリックサブネットへの配置によって解決に至りました。

*発行: 2021-11-01 / [[swx-isoya-elb-https-blog-serverworks-co-jp-alb-private-subnet-aws-4ff48e]]*

## 主要なトピック

- [[swx-isoya]]

## 詳細

- AWS初心者がプライベートサブネット上のWebサーバーに対してELB（ALB）経由でアクセスできないトラブルに直面し、その解決過程を記録した記事です。ALBの配置要件（サブネット設計）の理解不足が原因であり、適切なパブリックサブネットへの配置によって解決に至りました。
- トラブルの原因と解決のポイント
- **トラブル状況**
- プライベートサブネット上のWebサーバーにALBからアクセスできず、503エラーが発生。
- **根本的な誤解**
- 「ALBはVPC内にあれば良い」と考えていたが、実際にはALBを配置するサブネットにはインターネットゲートウェイ（IGW）へのルートが必要。
- **解決策**
- 該当AZにパブリックサブネットを作成し、ALBをそこに配置するように変更。
- **学び・教訓**

*発行: 2021-11-01 / [[swx-isoya-elb-https-blog-serverworks-co-jp-alb-private-subnet-aws-4ff48e]]*

## 関連テーマ

- [[swx-isoya]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【初心者向け】ELBからプライベートサブネットへのアクセスに困った話 - サーバーワークスエンジニアブログ.md`
- https://blog.serverworks.co.jp/alb-private-subnet
