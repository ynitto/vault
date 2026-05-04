---
title: "kintone REST APIの共通仕様"
type: "topic"
tags:
  - "authentication"
  - "networking"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/kintone REST APIの共通仕様.md"
summary: "kintone REST APIは、アプリ、レコード、スペースを操作するためのインターフェースです。以下に重要なポイントをまとめます。"
---

# kintone REST APIの共通仕様

## 概要

kintone REST APIは、アプリ、レコード、スペースを操作するためのインターフェースです。以下に重要なポイントをまとめます。

## 主要なトピック

- [[authentication]]
- [[networking]]

## 詳細

- kintone REST APIは、アプリ、レコード、スペースを操作するためのインターフェースです。以下に重要なポイントをまとめます。
- 1. リクエストの基本
- **形式**: リクエストボディは原則JSON、ファイルアップロードはマルチパート形式。
- **URL構成**: `https://{domain}/k/v1/{RESOURCE}` （ゲストスペースは `.../k/guest/{SPACE_ID}/v1/...`）
- **主要ヘッダー**:
- `Host`: ドメイン:ポート番号
- `Content-Type`: `application/json` 等
- `X-Cybozu-Authorization` / `X-Cybozu-API-Token`: 認証情報
- `X-HTTP-Method-Override`: HTTPメソッドのオーバーライド（URL長制限回避に有効）

## 関連テーマ

- [[authentication]]
- [[networking]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/kintone REST APIの共通仕様.md`
- https://cybozu.dev/ja/kintone/docs/rest-api/overview/kintone-rest-api-overview/
