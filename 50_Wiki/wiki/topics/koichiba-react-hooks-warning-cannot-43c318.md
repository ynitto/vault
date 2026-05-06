---
title: "React Hooks: 子コンポーネントから親の状態をレンダー時に変えたら叱られた ー Warning: Cannot update a component while rendering a different component"
type: "topic"
tags:
  - "koichiba"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/React Hooks 子コンポーネントから親の状態をレンダー時に変えたら叱られた ー Warning Cannot update a component while rendering a different component.md"
summary: "Reactにおいて、子コンポーネントのレンダー中に親コンポーネントの状態（state）を更新しようとすると発生する警告「`Warning: Cannot…"
---

# React Hooks: 子コンポーネントから親の状態をレンダー時に変えたら叱られた ー Warning: Cannot update a component while rendering a different component

## 概要

Reactにおいて、子コンポーネントのレンダー中に親コンポーネントの状態（state）を更新しようとすると発生する警告「`Warning: Cannot update a component while rendering a different component`」の原因と解決策を解説した技術記事です。

*発行: 2020-05-16 / [[koichiba-react-hooks-warning-cannot-43c318]]*

## 主要なトピック

- [[koichiba]]

## 詳細

- Reactにおいて、子コンポーネントのレンダー中に親コンポーネントの状態（state）を更新しようとすると発生する警告「`Warning: Cannot update a component while rendering a different component`」の原因と解決策を解説した技術記事です。
- 要点
- **問題の原因**
- Reactではコンポーネントのレンダー中に他のコンポーネントの状態を変更することが禁止されています（副作用の禁止）。
- **解決策：`useEffect`の利用**
- コンポーネントのレンダーが完全に終了した後に状態更新を実行するため、`useEffect`フックを使用します。
- `useEffect`の副作用関数内で親から渡された状態更新関数（`setState`）を呼び出すことで、警告を回避しつつ意図した状態変更を実現できます。
- **コード実装のポイント**
- 子コンポーネント側で`useEffect(() => setColor(color), [color, setColor]);`のように記述し、依存配列に更新関数と値を指定することで安全に親の状態を更新します。

*発行: 2020-05-16 / [[koichiba-react-hooks-warning-cannot-43c318]]*

## 関連テーマ

- [[koichiba]]

## 出典

- `../60_Resources/React Hooks 子コンポーネントから親の状態をレンダー時に変えたら叱られた ー Warning Cannot update a component while rendering a different component.md`
- https://qiita.com/FumioNonaka/items/3fe39911e3f2479128e8
