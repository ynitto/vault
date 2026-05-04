---
title: "XState Docs"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/XState Docs.md"
summary: "XStateにおける「遷移」は、イベント発生時に現在の状態から次の状態へどのように変化するかを定義する仕組みです。"
---

# XState Docs

## 概要

XStateにおける「遷移」は、イベント発生時に現在の状態から次の状態へどのように変化するかを定義する仕組みです。

## 主要なトピック


## 詳細

- XStateにおける「遷移」は、イベント発生時に現在の状態から次の状態へどのように変化するかを定義する仕組みです。
- 主要なポイント
- **遷移の定義**: `on` プロパティ内にイベント名とターゲット状態を指定します。
- **マシン遷移メソッド**: `machine.transition(state, event)` は、現在の状態とイベントに基づいて新しい状態を返す純粋関数です。
- **遷移の優先順位**: 階層構造では、より深い階層にある（子ノードの）定義が優先されます。
- **遷移の種類**:
- **内部遷移 (Internal)**: 状態ノードを終了・再実行せず、ターゲットが子ノードの場合や `internal: true` を指定した際に発生。
- **外部遷移 (External)**: 状態ノードを終了・再実行する（デフォルトの挙動）。
- **イベントレス遷移 (`always`)**: 条件が満たされたら即座に実行される遷移。

## 関連テーマ


## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/XState Docs.md`
- https://xstate.js.org/docs/guides/transitions.html#eventless-always-transitions
