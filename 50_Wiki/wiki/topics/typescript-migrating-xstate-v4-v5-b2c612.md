---
title: "Migrating from XState v4 to v5"
type: "topic"
tags:
  - "typescript"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Migrating from XState v4 to v5.md"
summary: "XState v5への移行は、APIの名称変更やTypeScriptサポートの強化、アーキテクチャの改善を伴う重要な更新です。主な変更点は以下の通りです。"
---

# Migrating from XState v4 to v5

## 概要

XState v5への移行は、APIの名称変更やTypeScriptサポートの強化、アーキテクチャの改善を伴う重要な更新です。主な変更点は以下の通りです。

## 主要なトピック

- [[typescript]]

## 詳細

- XState v5への移行は、APIの名称変更やTypeScriptサポートの強化、アーキテクチャの改善を伴う重要な更新です。主な変更点は以下の通りです。
- 1. APIの名称変更
- **createMachine()**: `Machine()`からの変更
- **createActor()**: `interpret()`からの変更
- **machine.provide()**: `machine.withConfig()`からの変更
- **actors**: `services`から名称変更
- 2. 主要なアーキテクチャ変更
- **コンテキスト設定**: `machine.withContext()`は廃止され、`input`を使用。
- **イベント処理**: `send()`は`raise()`または`sendTo()`に分離。

## 関連テーマ

- [[typescript]]

## 出典

- `../60_Resources/Migrating from XState v4 to v5.md`
- https://stately.ai/docs/migration
