---
title: "Question regarding rampusers and constantusers"
type: "topic"
tags:
  - "testing"
  - "saxenaj"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Question regarding rampusers and constantusers.md"
summary: "Gatlingのユーザー注入プロファイルに関する要約"
---

# Question regarding rampusers and constantusers

## 概要

Gatlingのユーザー注入プロファイルに関する要約

*発行: 2023-01-04 / [[testing-saxenaj-question-regarding-rampusers-21ab4d]]*

## 主要なトピック

- [[testing]]
- [[saxenaj]]

## 詳細

- Gatlingコミュニティにおける、`constantUsersPerSec`と`rampUsersPerSec`の挙動に関する質問とその回答のまとめです。
- 主要なポイント
- **ユーザー数とリクエスト数の混同に注意**
- これらの設定は「秒間あたりのリクエスト数」ではなく「**秒間あたりのユーザー開始数**」を定義します。
- シナリオが1つのリクエストのみで構成されている場合を除き、ユーザー数とリクエスト数は一致しません。
- **設定の解説**
- `constantUsersPerSec(10).during(20)`: 20秒間、毎秒10ユーザーを生成（合計200ユーザー）。
- `rampUsersPerSec(5).to(10).during(20)`: 20秒かけて毎秒5ユーザーから10ユーザーまで線形に加速（合計150ユーザー）。
- **テストの目的（用語の訂正）**

*発行: 2023-01-04 / [[testing-saxenaj-question-regarding-rampusers-21ab4d]]*

## 関連テーマ

- [[testing]]
- [[saxenaj]]

## 出典

- `../60_Resources/Question regarding rampusers and constantusers.md`
- https://community.gatling.io/t/question-regarding-rampusers-and-constantusers/7486/3
