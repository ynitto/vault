---
title: "Obsidian textlintの導入方法を解説"
source: "https://notes.spisignal.jp/Esseys/Obsidian+textlint%E3%81%AE%E5%B0%8E%E5%85%A5%E6%96%B9%E6%B3%95%E3%82%92%E8%A7%A3%E8%AA%AC"
author:
published:
created: 2026-04-25
description: "Obsidian textlintの導入方法を解説 - SpiSignal"
tags:
  - "clippings"
---
### 概要
Obsidianで文章校正を自動化するプラグイン「Obsidian textlint」の導入・設定方法を解説した記事。本プラグインは公式コミュニティプラグインではないため、手動でリポジトリをビルドする必要があります。

### 導入のポイント
- **前提知識**: Git, Node.js, ターミナル操作の基礎が必須。
- **リポジトリ**: メンテナンスが停止しているため、修正が加えられた[フォーク版リポジトリ](https://github.com/ko-shin-ryo/obsidian-textlint-fork)の使用を推奨。

### セットアップ手順
1. **Node.jsの準備**: 実行環境をインストール。
2. **取得とインストール**: リポジトリをクローンし、`npm i`でパッケージを導入。
3. **ルール定義**: `textlint-builder/textlintrc.json`で適用する校正ルールを記述。
4. **ビルド**: `textlint-builder`とプラグイン本体で順次`npm run build`を実行。
5. **設置**: 生成されたファイルをObsidianの`.obsidian/plugins/obsidian-textlint`ディレクトリに配置。

### カスタマイズ
- **設定変更**: `textlintrc.json`を編集し、ルールの有効/無効や閾値（漢字連続数など）を調整可能。
- **ルール追加**: 他のtextlintルール（`incremental-headers`等）も同様の手順で追加・設定が可能。
- **フィルタリング**: `textlint-filter-rule-comments`を使用すれば、特定の範囲で校正を無視する設定も行える。
