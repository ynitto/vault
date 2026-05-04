---
title: "kintone REST APIの共通仕様"
source: "https://cybozu.dev/ja/kintone/docs/rest-api/overview/kintone-rest-api-overview/"
author:
published:
created: 2026-05-01
description: "kintone REST APIの共通仕様を説明します。"
tags:
  - "clippings"
---
### kintone REST API 共通仕様の概要
kintone REST APIは、アプリ、レコード、スペースを操作するためのインターフェースです。以下に重要なポイントをまとめます。

#### 1. リクエストの基本
- **形式**: リクエストボディは原則JSON、ファイルアップロードはマルチパート形式。
- **URL構成**: `https://{domain}/k/v1/{RESOURCE}` （ゲストスペースは `.../k/guest/{SPACE_ID}/v1/...`）
- **主要ヘッダー**:
  - `Host`: ドメイン:ポート番号
  - `Content-Type`: `application/json` 等
  - `X-Cybozu-Authorization` / `X-Cybozu-API-Token`: 認証情報
  - `X-HTTP-Method-Override`: HTTPメソッドのオーバーライド（URL長制限回避に有効）

#### 2. レスポンスとエラー
- **ステータスコード**: 200番台で成功。それ以外はエラー。
- **エラー情報**: `id`（サポート用）、`code`（エラー種類）、`message`（メッセージ）を含むオブジェクトが返却される。

#### 3. 日時の取り扱い
- **フォーマット**: 基本的にISO 8601形式（`YYYY-MM-DDTHH:MM:SSZ`）。
- **登録・更新時**: UTCまたはオフセット付きの表記も可能。

#### 4. 主要な制限事項
- **同時接続数**: 1ドメインにつき最大100まで。
- **実行回数**: アプリごとに1日1万件（スタンダード）または10万件（ワイド）の制限あり。
- **レコード操作**: 一括処理は最大100件まで。また、ルックアップ等の特定フィールドは値の取得のみ可能。