---
title: "SNS Eメールサブスクリプションに記載される Unsubscribe リンクを無効化する - サーバーワークスエンジニアブログ"
source: "https://blog.serverworks.co.jp/sns-remove-unsubscribe-link"
author:
  - "[[swx-satake]]"
  - "[[エンジニアブログの記事一覧はコチラ]]"
published: 2020-10-12
created: 2026-04-30
description: "SRE部 佐竹です。 今回は SNS のEメールサブスクリプションにある Unsubscribe リンクを無効化する方法について記載しました。受信者の誰か1人でも Unsubscribe のURLリンクをクリックしてしまうと意図せず Unsubscribe されてしまうため、本番運用においては本対応を実施しておくのがより良いと存じます。"
tags:
  - "clippings"
---

### 概要
Amazon SNSのEメールサブスクリプションに含まれる「Unsubscribe（登録解除）リンク」を無効化し、誤操作やスパムフィルタによる意図しない登録解除を防ぐ方法を解説した記事です。

### 要点
- **背景**
  - 通知メール内のUnsubscribeリンクをクリックするだけで、誰でも簡単に通知停止が可能。
  - スパムフィルタの自動アクセスにより、意図せず購読が解除されるリスクがある。

- **無効化の手順**
  1. 既存のサブスクリプションを削除。
  2. 再度サブスクリプションを作成し、送られてくる確認メール内のURLを直接クリックしない。
  3. 確認メール内の「Confirm subscription」URLをコピーし、AWSマネジメントコンソールの「Confirm subscription」画面から直接登録を行う。

- **効果**
  - 上記手順で登録することで、以降は通知メール内のUnsubscribeリンクを押下しても「Subscription not removed」と表示され、登録解除が無効化される。
