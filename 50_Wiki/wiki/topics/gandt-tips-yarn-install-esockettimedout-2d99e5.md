---
title: "【Tips】yarn install時に発生しうるESOCKETTIMEDOUTの回避"
type: "topic"
tags:
  - "gandt"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【Tips】yarn install時に発生しうるESOCKETTIMEDOUTの回避.md"
summary: "`yarn install`実行時に発生するエラー「ESOCKETTIMEDOUT」は、大容量パッケージのダウンロード時間が規定時間を超過することで発生し…"
---

# 【Tips】yarn install時に発生しうるESOCKETTIMEDOUTの回避

## 概要

`yarn install`実行時に発生するエラー「ESOCKETTIMEDOUT」は、大容量パッケージのダウンロード時間が規定時間を超過することで発生します。解決策として、タイムアウト時間を延長する設定を`.yarnrc`ファイルに追加することで回避可能です。

*発行: 2019-09-18 / [[gandt-tips-yarn-install-esockettimedout-2d99e5]]*

## 主要なトピック

- [[gandt]]

## 詳細

- `yarn install`実行時に発生するエラー「ESOCKETTIMEDOUT」は、大容量パッケージのダウンロード時間が規定時間を超過することで発生します。解決策として、タイムアウト時間を延長する設定を`.yarnrc`ファイルに追加することで回避可能です。
- 対応策
- **設定ファイル**: `yarn install`を実行するディレクトリに`.yarnrc`を作成または編集する。
- **記述内容**:
- ```text
- network-timeout 600000
- ```
- ※上記は600,000ミリ秒（10分）の設定値です。
- 補足

*発行: 2019-09-18 / [[gandt-tips-yarn-install-esockettimedout-2d99e5]]*

## 関連テーマ

- [[gandt]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/【Tips】yarn install時に発生しうるESOCKETTIMEDOUTの回避.md`
- https://qiita.com/GandT/items/9c2afa82609ff6062fd3
