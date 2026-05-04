---
title: "VSCodeが重い！メモリ使用量を1/3にする設定まとめ"
source: "https://qiita.com/nolanlover0527/items/071277263f8851012e6b"
author:
  - "[[nolanlover0527]]"
published: 2025-10-28
created: 2026-04-30
description: "重くなる主な原因 VSCodeが重くなる最も一般的な原因は、インストールされている拡張機能の数や質です。その他の原因として以下が挙げられます↓ 大規模なプロジェクトを開いていると、VSCodeが必要とするリソースが増加 ファイル監視プロセス（watcherServ..."
tags:
  - "clippings"
---
### VSCodeを軽量化するための最適化設定ガイド

この記事では、VSCodeのメモリ使用量を削減し、動作を高速化するための設定を網羅的に解説しています。

#### 1. 拡張機能の整理【最重要】
- **特定:** `Developer: Show Running Extensions` で起動負荷が高いものを特定。
- **削除・無効化:** 不要な拡張機能を削除し、必要に応じて「ワークスペース単位」で有効化を使い分ける。
- **改善:** 拡張機能の数を減らすことで、スタートアップパフォーマンスが大幅に向上します。

#### 2. ファイル監視・除外設定
- `files.watcherExclude` / `files.exclude` / `search.exclude` に `node_modules` や `dist`、`build` などの不要なディレクトリを追加し、エディタ負荷を軽減する。

#### 3. TypeScript環境の最適化
- `tsconfig.json` の `skipLibCheck: true` を設定。
- `.vscode/settings.json` で `tsserver.log` を無効化し、自動型取得をオフにする。

#### 4. UIの軽量化
- ミニマップ、パンくずリスト、コードレンズなど、リソースを消費するUI要素を無効化する。

#### 5. その他の設定
- **Git:** `autorefresh` や `autofetch` を無効にしてリソース消費を抑制。
- **キャッシュ:** 定期的にキャッシュフォルダをクリアする。
- **OS設定:** Windowsのシステムアニメーションをオフにすることで体感速度を改善。
