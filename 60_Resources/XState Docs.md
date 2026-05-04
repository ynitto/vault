---
title: "XState Docs"
source: "https://xstate.js.org/docs/guides/transitions.html#eventless-always-transitions"
author:
published:
created: 2026-05-01
description: "Documentation for XState: State Machines and Statecharts for the Modern Web"
tags:
  - "clippings"
---
### XState 状態遷移の概要
XStateにおける「遷移」は、イベント発生時に現在の状態から次の状態へどのように変化するかを定義する仕組みです。

### 主要なポイント
*   **遷移の定義**: `on` プロパティ内にイベント名とターゲット状態を指定します。
*   **マシン遷移メソッド**: `machine.transition(state, event)` は、現在の状態とイベントに基づいて新しい状態を返す純粋関数です。
*   **遷移の優先順位**: 階層構造では、より深い階層にある（子ノードの）定義が優先されます。
*   **遷移の種類**:
    *   **内部遷移 (Internal)**: 状態ノードを終了・再実行せず、ターゲットが子ノードの場合や `internal: true` を指定した際に発生。
    *   **外部遷移 (External)**: 状態ノードを終了・再実行する（デフォルトの挙動）。
    *   **イベントレス遷移 (`always`)**: 条件が満たされたら即座に実行される遷移。
    *   **禁止遷移 (Forbidden)**: `undefined` を指定することで、イベントを無視し親のハンドラへの伝播も防ぐ。
*   **高度な機能**:
    *   **ガード (Guards)**: `cond` を用いた条件付き分岐。
    *   **ワイルドカード (`*`)**: どのイベントでもマッチする遷移。
    *   **複数ターゲット**: 配列を用いて、並列状態の複数ノードへ同時に遷移可能。