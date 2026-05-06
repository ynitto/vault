---
title: "Dropbox Business APIの基礎知識"
type: "topic"
tags:
  - "authentication"
  - "nkmk1215"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Dropbox Business APIの基礎知識.md"
summary: "本記事は「DBX Platform デベロッパーガイド」を読んだ際の個人メモです。Dropbox APIの認証方式や名前空間（チームフォルダ/チームスペー…"
---

# Dropbox Business APIの基礎知識

## 概要

本記事は「DBX Platform デベロッパーガイド」を読んだ際の個人メモです。Dropbox APIの認証方式や名前空間（チームフォルダ/チームスペース）の概念について解説しています。

*発行: 2021-09-12 / [[authentication-nkmk1215-dropbox-business-api-0c2684]]*

## 主要なトピック

- [[authentication]]
- [[nkmk1215]]

## 詳細

- 本記事は「DBX Platform デベロッパーガイド」を読んだ際の個人メモです。Dropbox APIの認証方式や名前空間（チームフォルダ/チームスペース）の概念について解説しています。
- 要点まとめ
- 1. アプリのスコープ
- **アプリフォルダー**: アプリ専用フォルダ内のみフル権限。
- **フルDropbox**: ユーザーのフォルダ全体へアクセス可能。
- 2. 主な認証タイプ
- **ユーザー認証**: 特定ユーザーのアカウント操作。
- **チーム認証**: チーム管理やメンバーへの代行操作（Select-User/Select-Adminヘッダーを使用）。
- **アプリ認証**: アプリキーとシークレットを使用し、個別のユーザー・チームを識別しない。

*発行: 2021-09-12 / [[authentication-nkmk1215-dropbox-business-api-0c2684]]*

## 関連テーマ

- [[authentication]]
- [[nkmk1215]]

## 出典

- `../60_Resources/Dropbox Business APIの基礎知識.md`
- https://qiita.com/nkmk1215/items/7b1427a74a74b473266c
