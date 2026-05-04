---
title: "チーム スペースを使用するチームへの対応ガイド"
type: "topic"
tags:
  - "authentication"
  - "sayo"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/チーム スペースを使用するチームへの対応ガイド.md"
summary: "Dropboxが提供する「チームスペース」への移行に伴い、APIを利用した連携アプリケーションで必要となる仕様変更や対応方法を解説した技術ガイドです。"
---

# チーム スペースを使用するチームへの対応ガイド

## 概要

Dropboxが提供する「チームスペース」への移行に伴い、APIを利用した連携アプリケーションで必要となる仕様変更や対応方法を解説した技術ガイドです。

*発行: 2023-03-09 / [[authentication-sayo-https-navi-dropbox-jp-guide-to-adding-support-for-te-e64e68]]*

## 主要なトピック

- [[authentication]]
- [[sayo]]

## 詳細

- Dropboxが提供する「チームスペース」への移行に伴い、APIを利用した連携アプリケーションで必要となる仕様変更や対応方法を解説した技術ガイドです。
- 主要な変更点と対応のポイント
- 1. チームスペースの仕組み
- **フォルダ構造の刷新**: チームメンバー全員で同じフォルダ構造を共有し、個人の環境に依存しない統一された管理を実現。
- **名前空間**: チームスペース移行後は「チームルート名前空間」以下ですべてのデータが管理されるようになります。
- 2. アプリケーション開発での対応事項
- **アクセススコープの変更**: チームスペース使用時には、APIリクエストに `Dropbox-API-Path-Root` ヘッダーを含め、チームルート名前空間を指定する必要があります。
- **ファイルパスの扱い**: `home_path` を使用してメンバー個人のフォルダとチームのトップレベルフォルダを区別して扱う必要があります。
- **管理者権限の管理**: チームフォルダと異なり、トップレベルフォルダ操作には管理者権限の判定や `Dropbox-API-Select-Admin` ヘッダーの使用が必要な場合があります。

*発行: 2023-03-09 / [[authentication-sayo-https-navi-dropbox-jp-guide-to-adding-support-for-te-e64e68]]*

## 関連テーマ

- [[authentication]]
- [[sayo]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/チーム スペースを使用するチームへの対応ガイド.md`
- https://navi.dropbox.jp/guide-to-adding-support-for-team-space
