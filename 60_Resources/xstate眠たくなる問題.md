---
title: "xstate眠たくなる問題"
source: "https://qiita.com/github0013@github/items/2f2f5233429cfa75ecd1"
author:
  - "[[github0013@github]]"
published: 2021-05-24
created: 2026-05-01
description: "問題 xstateは使えるとビジネスロジックをかなり綺麗に纏められるようになるし、各state事で起こせるeventは固定なので、組む時のバグを減らせるしユーザーがインスペクターから勝手に関連性のないeventを発火させることも出来ない。 便利なはずだと思ってサンプルを見..."
tags:
  - "clippings"
---
### 概要
XStateを用いた状態管理の概念と、ビジネスロジックへの落とし込み方を解説した記事です。

### 主な要点
* **XStateの利点**: ビジネスロジックを整理し、固定されたイベントで状態遷移を制御することで、バグを減らし予期せぬ状態遷移を防止できる。
* **主要な構成要素**:
    * **machine**: 状態遷移の核となる定義。
    * **state**: 現在の状態。
    * **context**: 状態に付随するデータ（値の保持）。
    * **event**: 状態を遷移させるトリガー。
    * **action**: 副作用（結果を気にしない処理やContextの更新）。
    * **invoke**: 非同期処理など、結果に応じて遷移を分ける処理。
    * **activity**: 継続的な処理（setIntervalなど）。
* **導入判断基準**: `setState`などで複数の状態を管理しており、組み合わせによるバグ（例：読み込み中かつエラー）が発生しやすい場合は、XStateへの移行が推奨される。
* **設計のコツ**: TypeScript利用時は`@xstate/immer`を用いると、Contextの更新（assign）が簡潔になる。