---
title: "How do you disable Google Chrome SafeBrowsing while using Puppeteer?"
type: "topic"
tags:
  - "crazy-redd-61911-gold"
  - "ggorlen"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How do you disable Google Chrome SafeBrowsing while using Puppeteer.md"
summary: "Puppeteerを使用して自動化を行う際、Google Chromeの「SafeBrowsing（セーフブラウジング）」機能やパスワード流出通知がポップ…"
---

# How do you disable Google Chrome SafeBrowsing while using Puppeteer?

## 概要

Puppeteerを使用して自動化を行う際、Google Chromeの「SafeBrowsing（セーフブラウジング）」機能やパスワード流出通知がポップアップし、スクリプトの実行を阻害する問題への解決策を議論したトピックです。

*発行: 2024-03-08 / [[crazy-redd-61911-gold-ggorlen-do-you-disable-ea973f]]*

## 主要なトピック

- [[crazy-redd-61911-gold]]
- [[ggorlen]]

## 詳細

- Puppeteerを使用して自動化を行う際、Google Chromeの「SafeBrowsing（セーフブラウジング）」機能やパスワード流出通知がポップアップし、スクリプトの実行を阻害する問題への解決策を議論したトピックです。
- 要点まとめ
- **問題の背景**: ログイン時に特定のパスワードを使用すると、ブラウザがデータ流出警告ダイアログを表示し、スクリプトが停止・失敗する。
- **主な解決策**:
- **`puppeteer-extra`の活用**: `puppeteer-extra-plugin-user-preferences`プラグインを使用して、`safebrowsing.enabled`や`enhanced`を`false`に設定する。
- **コマンドライン引数の追加**: `args`に`--disable-features=SafeBrowsing`や`--suppress-message-center-popups`などのフラグを追加してポップアップを抑制する。
- **外部設定**: システム上のChromeパスを明示的に指定し、適切な権限で起動させることで動作が安定する場合がある。
- **注意点**: 以前有効だった手法がブラウザの更新により効かなくなる場合があるため、複数の引数やプラグインの組み合わせを試す必要がある。

*発行: 2024-03-08 / [[crazy-redd-61911-gold-ggorlen-do-you-disable-ea973f]]*

## 関連テーマ

- [[crazy-redd-61911-gold]]
- [[ggorlen]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How do you disable Google Chrome SafeBrowsing while using Puppeteer.md`
- https://stackoverflow.com/questions/78124291/how-do-you-disable-google-chrome-safebrowsing-while-using-puppeteer
