---
title: "esbuild - Plugins"
type: "topic"
tags:
  - "javascript"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/esbuild - Plugins.md"
summary: "esbuild のプラグイン API は、ビルドプロセスにカスタムロジックを注入するための機能です。`build` API でのみ使用可能であり、Java…"
---

# esbuild - Plugins

## 概要

esbuild のプラグイン API は、ビルドプロセスにカスタムロジックを注入するための機能です。`build` API でのみ使用可能であり、JavaScript または Go で記述する必要があります。

## 主要なトピック

- [[javascript]]

## 詳細

- esbuild のプラグイン API は、ビルドプロセスにカスタムロジックを注入するための機能です。`build` API でのみ使用可能であり、JavaScript または Go で記述する必要があります。
- 主要な機能と概念
- **オンリゾルブ (onResolve)**: インポートパスの解決方法をカスタマイズ・インターセプトします。
- **オンロード (onLoad)**: ファイルの読み込み方法を定義し、内容の変換や仮想モジュールの生成を行います。
- **仮想モジュール**: ファイルシステム上に実体がないモジュールを作成可能です（`namespace` で管理）。
- **フィルタリング**: 正規表現によるフィルタリングで、パフォーマンス低下を最小限に抑えます。
- **ライフサイクル**: `onStart`（ビルド開始時）、`onEnd`（ビルド終了時）、`onDispose`（クリーンアップ時）のコールバックを提供します。
- 注意点
- **パフォーマンス**: プラグインはビルド速度に影響を与えるため、フィルタを適切に設定し、可能な限り最小限の範囲で動作させる必要があります。

## 関連テーマ

- [[javascript]]

## 出典

- `../60_Resources/esbuild - Plugins.md`
- https://esbuild../.github.io/plugins/#filters
