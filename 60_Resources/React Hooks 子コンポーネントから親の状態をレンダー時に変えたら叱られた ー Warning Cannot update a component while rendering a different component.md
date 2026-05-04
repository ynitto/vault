---
title: "React Hooks: 子コンポーネントから親の状態をレンダー時に変えたら叱られた ー Warning: Cannot update a component while rendering a different component"
source: "https://qiita.com/FumioNonaka/items/3fe39911e3f2479128e8"
author:
  - "[[koichiba]]"
published: 2020-05-16
created: 2026-04-30
description: "ネストした子コンポーネントから親の状態を変えるReactアプリケーションで、少し試行錯誤したことを書きとめます。経緯の説明からはじめますので、タイトルの警告(Warning)の意味が知りたいという方は最後の「レンダーが済んでから親の状態を変える」をお読みください。 配列デ..."
tags:
  - "clippings"
---
### 概要
Reactにおいて、子コンポーネントのレンダー中に親コンポーネントの状態（state）を更新しようとすると発生する警告「`Warning: Cannot update a component while rendering a different component`」の原因と解決策を解説した技術記事です。

### 要点
- **問題の原因**
  - Reactではコンポーネントのレンダー中に他のコンポーネントの状態を変更することが禁止されています（副作用の禁止）。

- **解決策：`useEffect`の利用**
  - コンポーネントのレンダーが完全に終了した後に状態更新を実行するため、`useEffect`フックを使用します。
  - `useEffect`の副作用関数内で親から渡された状態更新関数（`setState`）を呼び出すことで、警告を回避しつつ意図した状態変更を実現できます。

- **コード実装のポイント**
  - 子コンポーネント側で`useEffect(() => setColor(color), [color, setColor]);`のように記述し、依存配列に更新関数と値を指定することで安全に親の状態を更新します。
