---
title: "PowerAutomateでTeamsの投稿をExcelに自動転記する方法"
type: "topic"
tags:
  - "office365adm"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/PowerAutomateでTeamsの投稿をExcelに自動転記する方法.md"
summary: "Power AutomateでTeams投稿をExcelに自動転記する方法"
---

# PowerAutomateでTeamsの投稿をExcelに自動転記する方法

## 概要

Power AutomateでTeams投稿をExcelに自動転記する方法

*発行: 2021-10-22 / [[office365adm-powerautomate-teams-excel-https-78a219]]*

## 主要なトピック

- [[office365adm]]

## 詳細

- Teamsのチャット内容を自動的にExcelへ蓄積し、業務効率化や見落とし防止を実現する手順です。
- 1. 下準備
- **Excel作成**: A1:C1をテーブル化し、ヘッダーを「件名」「連絡内容」「投稿日時」に設定。
- **ファイル配置**: 作成したExcelファイルをTeamsのチャネル内「ファイル」へアップロード。
- 2. Power Automateフロー作成
- **トリガー**: 「チャネルに新しいメッセージが追加されたとき」を選択。
- **変換処理**:
- **HTMLからテキスト**: メッセージ本文をプレーンテキストに変換。
- **タイムゾーンの変換**: 投稿日時（UTC）を日本時間（JST）へ変換。

*発行: 2021-10-22 / [[office365adm-powerautomate-teams-excel-https-78a219]]*

## 関連テーマ

- [[office365adm]]

## 出典

- `60_Resources/PowerAutomateでTeamsの投稿をExcelに自動転記する方法.md`
- https://yjk365.jp/config/teams-excel/
