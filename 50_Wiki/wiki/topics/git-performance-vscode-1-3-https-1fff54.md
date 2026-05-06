---
title: "VSCodeが重い！メモリ使用量を1/3にする設定まとめ"
type: "topic"
tags:
  - "git"
  - "performance"
  - "typescript"
  - "nolanlover0527"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/VSCodeが重い！メモリ使用量を13にする設定まとめ.md"
summary: "この記事では、VSCodeのメモリ使用量を削減し、動作を高速化するための設定を網羅的に解説しています。"
---

# VSCodeが重い！メモリ使用量を1/3にする設定まとめ

## 概要

この記事では、VSCodeのメモリ使用量を削減し、動作を高速化するための設定を網羅的に解説しています。

*発行: 2025-10-28 / [[git-performance-vscode-1-3-https-1fff54]]*

## 主要なトピック

- [[git]]
- [[performance]]
- [[typescript]]
- [[nolanlover0527]]

## 詳細

- この記事では、VSCodeのメモリ使用量を削減し、動作を高速化するための設定を網羅的に解説しています。
- 1. 拡張機能の整理【最重要】
- **特定:** `Developer: Show Running Extensions` で起動負荷が高いものを特定。
- **削除・無効化:** 不要な拡張機能を削除し、必要に応じて「ワークスペース単位」で有効化を使い分ける。
- **改善:** 拡張機能の数を減らすことで、スタートアップパフォーマンスが大幅に向上します。
- 2. ファイル監視・除外設定
- `files.watcherExclude` / `files.exclude` / `search.exclude` に `node_modules` や `dist`、`build` などの不要なディレクトリを追加し、エディタ負荷を軽減する。
- 3. TypeScript環境の最適化
- `tsconfig.json` の `skipLibCheck: true` を設定。

*発行: 2025-10-28 / [[git-performance-vscode-1-3-https-1fff54]]*

## 関連テーマ

- [[git]]
- [[performance]]
- [[typescript]]
- [[nolanlover0527]]

## 出典

- `60_Resources/VSCodeが重い！メモリ使用量を13にする設定まとめ.md`
- https://qiita.com/nolanlover0527/items/071277263f8851012e6b
