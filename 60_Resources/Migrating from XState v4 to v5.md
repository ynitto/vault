---
title: "Migrating from XState v4 to v5"
source: "https://stately.ai/docs/migration"
author:
published:
created: 2026-04-30
description:
tags:
  - "clippings"
---
### XState v5 移行ガイドの要約
XState v5への移行は、APIの名称変更やTypeScriptサポートの強化、アーキテクチャの改善を伴う重要な更新です。主な変更点は以下の通りです。

#### 1. APIの名称変更
- **createMachine()**: `Machine()`からの変更
- **createActor()**: `interpret()`からの変更
- **machine.provide()**: `machine.withConfig()`からの変更
- **actors**: `services`から名称変更

#### 2. 主要なアーキテクチャ変更
- **コンテキスト設定**: `machine.withContext()`は廃止され、`input`を使用。
- **イベント処理**: `send()`は`raise()`または`sendTo()`に分離。
- **実装関数**: すべての関数は`{ context, event, ... }`という単一の引数を受け取る形式に統一。
- **状態検証**: `in`プロパティは廃止され、`guard: stateIn(...)`を使用。

#### 3. 状態と観測
- **購読**: `onTransition()`は廃止され、`actor.subscribe()`を使用。
- **履歴**: `state.history`は廃止され、`actor.subscribe()`での管理へ移行。
- **値の取得**: `state.nextEvents`は廃止され、専用のヘルパー関数が必要。

#### 4. TypeScript・ツール・React
- **TypeScript**: バージョン5.0以上が必須。
- **@xstate/react**: `useInterpret()`は`useActorRef()`に名称変更。`useActor()`の引数は既存のactorではなく、actorの「ロジック」を指定する形式へ変更。
- **移行のヒント**: v4とv5を並行利用して段階的に移行することも可能。
