---
title: "SNS Eメールサブスクリプションに記載される Unsubscribe リンクを無効化する - サーバーワークスエンジニアブログ"
type: "topic"
tags:
  - "aws"
  - "swx-satake"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/SNS Eメールサブスクリプションに記載される Unsubscribe リンクを無効化する - サーバーワークスエンジニアブログ.md"
summary: "Amazon SNSのEメールサブスクリプションに含まれる「Unsubscribe（登録解除）リンク」を無効化し、誤操作やスパムフィルタによる意図しない登…"
---

# SNS Eメールサブスクリプションに記載される Unsubscribe リンクを無効化する - サーバーワークスエンジニアブログ

## 概要

Amazon SNSのEメールサブスクリプションに含まれる「Unsubscribe（登録解除）リンク」を無効化し、誤操作やスパムフィルタによる意図しない登録解除を防ぐ方法を解説した記事です。

*発行: 2020-10-12 / [[aws-swx-satake-sns-e-unsubscribe-523ddf]]*

## 主要なトピック

- [[aws]]
- [[swx-satake]]

## 詳細

- Amazon SNSのEメールサブスクリプションに含まれる「Unsubscribe（登録解除）リンク」を無効化し、誤操作やスパムフィルタによる意図しない登録解除を防ぐ方法を解説した記事です。
- 要点
- **背景**
- 通知メール内のUnsubscribeリンクをクリックするだけで、誰でも簡単に通知停止が可能。
- スパムフィルタの自動アクセスにより、意図せず購読が解除されるリスクがある。
- **無効化の手順**
- 1. 既存のサブスクリプションを削除。
- 2. 再度サブスクリプションを作成し、送られてくる確認メール内のURLを直接クリックしない。
- 3. 確認メール内の「Confirm subscription」URLをコピーし、AWSマネジメントコンソールの「Confirm subscription」画面から直接登録を行う。

*発行: 2020-10-12 / [[aws-swx-satake-sns-e-unsubscribe-523ddf]]*

## 関連テーマ

- [[aws]]
- [[swx-satake]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/SNS Eメールサブスクリプションに記載される Unsubscribe リンクを無効化する - サーバーワークスエンジニアブログ.md`
- https://blog.serverworks.co.jp/sns-remove-unsubscribe-link
