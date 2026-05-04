---
title: "waitForNavigation doesn't work after evaluate fetch() or XMLHttpRequest() · Issue #1466 · puppeteer/puppeteer"
type: "topic"
tags:
  - "ghost"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/waitForNavigation doesn't work after evaluate fetch() or XMLHttpRequest() · Issue 1466 · puppeteerpuppeteer.md"
summary: "Puppeteerにおいて、`page.evaluate()`内で実行された`fetch`や`XMLHttpRequest`（非同期通信）の完了を`pag…"
---

# waitForNavigation doesn't work after evaluate fetch() or XMLHttpRequest() · Issue #1466 · puppeteer/puppeteer

## 概要

Puppeteerにおいて、`page.evaluate()`内で実行された`fetch`や`XMLHttpRequest`（非同期通信）の完了を`page.waitForNavigation()`で待機できないという問題に関する議論です。

*発行: 2017-11-24 / [[ghost-waitfornavigation-doesn-t-work-111cc2]]*

## 主要なトピック

- [[ghost]]

## 詳細

- Puppeteerにおいて、`page.evaluate()`内で実行された`fetch`や`XMLHttpRequest`（非同期通信）の完了を`page.waitForNavigation()`で待機できないという問題に関する議論です。
- 要点
- **原因**: `waitForNavigation`はURL遷移などのメインフレームのナビゲーションを待機するためのものであり、ページ内での非同期リクエストには反応しない。
- **解決策**:
- **`waitForSelector`や`waitForFunction`**: 非同期通信の結果としてDOMが変化する場合に有効。
- **ネットワークイベントの監視**: `request`や`requestfinished`イベントを使用して通信の完了を独自にフックする。
- **実装のコツ**: 通信が複数発生する場合、タイムアウトを伴う再帰的な待機関数を作成し、イベントリスナーには`.once()`を使用するのが推奨される。

*発行: 2017-11-24 / [[ghost-waitfornavigation-doesn-t-work-111cc2]]*

## 関連テーマ

- [[ghost]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/waitForNavigation doesn't work after evaluate fetch() or XMLHttpRequest() · Issue 1466 · puppeteerpuppeteer.md`
- https://github.com/puppeteer/puppeteer/issues/1466
