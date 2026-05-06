---
title: "Node.js: child_process.fork()で起動したプロセスを子子孫孫殺す方法"
type: "topic"
tags:
  - "node-js"
  - "suin"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Node.js child_process.fork()で起動したプロセスを子子孫孫殺す方法.md"
summary: "Node.jsで`child_process.fork()`を使用して生成した子プロセスおよび孫プロセスを、一括して終了（kill）させる手法についての解…"
---

# Node.js: child_process.fork()で起動したプロセスを子子孫孫殺す方法

## 概要

Node.jsで`child_process.fork()`を使用して生成した子プロセスおよび孫プロセスを、一括して終了（kill）させる手法についての解説記事です。

*発行: 2020-04-07 / [[node-js-suin-node-js-child-process-fork-cb4607]]*

## 主要なトピック

- [[node-js]]
- [[suin]]

## 詳細

- Node.jsで`child_process.fork()`を使用して生成した子プロセスおよび孫プロセスを、一括して終了（kill）させる手法についての解説記事です。
- 要点まとめ
- **課題**: 通常、親プロセスが子プロセスを`kill()`しても、そこから派生した孫プロセスは終了せず、孤児プロセスとして生存し続ける。
- **解決策**: プロセスグループを利用する。
- **`detached: true`の活用**: `fork()`時にこのオプションを指定することで、子プロセスを親とは別の「プロセスグループ」に分離する。
- **負のPIDによるkill**: `process.kill(-pid, 'SIGINT')`のようにPIDに負の値を指定することで、そのグループIDに属するプロセス全体にシグナルを一括送信する。
- **注意点**: 本手法はUNIX/Linux環境を前提としており、グループ全体を終了させる際は親プロセス自体を巻き込まないよう、適切なグループ分離（detached設定）が必要。

*発行: 2020-04-07 / [[node-js-suin-node-js-child-process-fork-cb4607]]*

## 関連テーマ

- [[node-js]]
- [[suin]]

## 出典

- `60_Resources/Node.js child_process.fork()で起動したプロセスを子子孫孫殺す方法.md`
- https://qiita.com/suin/items/ba35a78c0b7268e8e7d1
