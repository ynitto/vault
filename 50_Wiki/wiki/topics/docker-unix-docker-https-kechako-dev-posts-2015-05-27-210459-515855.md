---
title: "Unix プロセスと Docker の罠"
type: "topic"
tags:
  - "docker"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Unix プロセスと Docker の罠.md"
summary: "Dockerコンテナ環境において、Unixプロセスの親子関係やゾンビプロセスが発生する仕組みと、その解決策を解説した記事です。"
---

# Unix プロセスと Docker の罠

## 概要

Dockerコンテナ環境において、Unixプロセスの親子関係やゾンビプロセスが発生する仕組みと、その解決策を解説した記事です。

*発行: 2015-05-28 / [[docker-unix-docker-https-kechako-dev-posts-2015-05-27-210459-515855]]*

## 主要なトピック

- [[docker]]

## 詳細

- Dockerコンテナ環境において、Unixプロセスの親子関係やゾンビプロセスが発生する仕組みと、その解決策を解説した記事です。
- 要点まとめ
- **プロセスの基本**
- Unixプロセスには親子関係があり、全てのプロセスの先祖はPID 1の「initプロセス」である。
- 親が死んだ子プロセスはinitが引き取る（孤児プロセス）。
- **ゾンビプロセス**
- 子の終了ステータスを親が回収しないと、システム上に「ゾンビプロセス」として残る。
- 放置するとリソースを圧迫するため、`Process.wait`等での回収が不可欠。
- **Dockerの罠**

*発行: 2015-05-28 / [[docker-unix-docker-https-kechako-dev-posts-2015-05-27-210459-515855]]*

## 関連テーマ

- [[docker]]

## 出典

- `60_Resources/Unix プロセスと Docker の罠.md`
- https://kechako.dev/posts/2015/05/27/210459/
