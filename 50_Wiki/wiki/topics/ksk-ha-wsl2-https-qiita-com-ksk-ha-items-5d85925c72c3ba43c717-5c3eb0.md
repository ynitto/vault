---
title: "WSL2を自動起動する設定"
type: "topic"
tags:
  - "ksk-ha"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/WSL2を自動起動する設定.md"
summary: "Windows再起動時にWSL2を自動的に起動させるための、タスクスケジューラを利用した設定手順の解説記事です。"
---

# WSL2を自動起動する設定

## 概要

Windows再起動時にWSL2を自動的に起動させるための、タスクスケジューラを利用した設定手順の解説記事です。

*発行: 2025-09-13 / [[ksk-ha-wsl2-https-qiita-com-ksk-ha-items-5d85925c72c3ba43c717-5c3eb0]]*

## 主要なトピック

- [[ksk-ha]]

## 詳細

- Windows再起動時にWSL2を自動的に起動させるための、タスクスケジューラを利用した設定手順の解説記事です。
- 自動起動設定の要点
- **タスクスケジューラの利用**
- 「タスクの作成」から任意の名前を設定。
- 「全般」タブで「ユーザーがログオンしているかどうかにかかわらず実行する」を選択。
- **トリガーとアクションの設定**
- **トリガー**: 「スタートアップ時」に設定。
- **プログラム**: `C:\Windows\System32\wsl.exe`
- **引数**: `-u root sleep infinity`

*発行: 2025-09-13 / [[ksk-ha-wsl2-https-qiita-com-ksk-ha-items-5d85925c72c3ba43c717-5c3eb0]]*

## 関連テーマ

- [[ksk-ha]]

## 出典

- `60_Resources/WSL2を自動起動する設定.md`
- https://qiita.com/ksk_ha/items/5d85925c72c3ba43c717
