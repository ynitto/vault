---
title: "社内勉強会：iOSのBluetooth通信でRSA暗号化体験"
type: "topic"
tags:
  - "git"
  - "timers-tech"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/社内勉強会：iOSのBluetooth通信でRSA暗号化体験.md"
summary: "本記事は、iOSエンジニアによる社内勉強会での発表内容をまとめたものです。「SICP（計算機プログラムの構造と解釈）」を題材に、学習の一環として2台のiP…"
---

# 社内勉強会：iOSのBluetooth通信でRSA暗号化体験

## 概要

本記事は、iOSエンジニアによる社内勉強会での発表内容をまとめたものです。「SICP（計算機プログラムの構造と解釈）」を題材に、学習の一環として2台のiPhone間でBluetooth通信を利用し、RSA暗号の仕組みを体験できるデモアプリ「BluetoothRSASample」を開発した事例が紹介されています。

*発行: 2015-11-06 / [[git-timers-tech-ios-bluetooth-rsa-f1b8d3]]*

## 主要なトピック

- [[git]]
- [[timers-tech]]

## 詳細

- 本記事は、iOSエンジニアによる社内勉強会での発表内容をまとめたものです。「SICP（計算機プログラムの構造と解釈）」を題材に、学習の一環として2台のiPhone間でBluetooth通信を利用し、RSA暗号の仕組みを体験できるデモアプリ「BluetoothRSASample」を開発した事例が紹介されています。
- 要点
- **目的**: RSA暗号（公開鍵・秘密鍵）の仕組みを実体験として理解すること。
- **開発したアプリ**: 2台のiPhone間でBluetooth通信を行い、鍵の受け渡しや暗号化・復号化を行うデモアプリを作成。
- **技術要素**:
- Bluetooth通信（Apple公式の「BTLE Transfer」を参考に実装）。
- RSA暗号の基本的な数学的ロジック（累乗計算と剰余演算）。
- **公開情報**: ソースコードをGitHubにて公開。
- **結論**: 数学的な暗号の仕組みが、端末間のやりとりを通じて「暗号化・復号化」として実感できる内容となっている。

*発行: 2015-11-06 / [[git-timers-tech-ios-bluetooth-rsa-f1b8d3]]*

## 関連テーマ

- [[git]]
- [[timers-tech]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/社内勉強会：iOSのBluetooth通信でRSA暗号化体験.md`
- https://techblog.timers-inc.com/entry/2015/11/06/120817
