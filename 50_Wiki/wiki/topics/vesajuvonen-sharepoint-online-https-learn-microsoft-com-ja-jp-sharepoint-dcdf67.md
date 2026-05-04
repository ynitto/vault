---
title: "SharePoint Online で調整またはブロックを回避する"
type: "topic"
tags:
  - "vesajuvonen"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/SharePoint Online で調整またはブロックを回避する.md"
summary: "SharePoint Online の調整とブロックの回避策について"
---

# SharePoint Online で調整またはブロックを回避する

## 概要

SharePoint Online の調整とブロックの回避策について

## 主要なトピック

- [[vesajuvonen]]

## 詳細

- SharePoint Online では、サービスの信頼性とパフォーマンスを維持するために、API 利用状況に応じて「調整（スロットリング）」や「ブロック」が行われます。本ガイドは、これを回避・適切に処理するための指針です。
- 調整（スロットリング）の仕組み
- **目的:** リソースの過剰使用を防ぎ、公平なアクセスを維持する。
- **検知:** 制限を超えると HTTP 429（要求過多）や 503（ビジー）が返される。
- **リソース単位:** 要求ごとの負荷に応じて計算される「リソースユニット」により制限を判定。
- 調整を処理する方法
- **ヘッダーの活用:** `Retry-After`（再試行待機時間）や `RateLimit` ヘッダー（現在の使用率）を尊重する。
- **APIの選定:** 可能であれば従来の CSOM/REST よりも最適化された **Microsoft Graph API** を優先的に利用する。
- **トラフィックの装飾:** アプリケーション登録を行い、`User-Agent` 文字列を正しく設定することで、適切に識別されるようにする。

## 関連テーマ

- [[vesajuvonen]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/SharePoint Online で調整またはブロックを回避する.md`
- https://learn.microsoft.com/ja-jp/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online
