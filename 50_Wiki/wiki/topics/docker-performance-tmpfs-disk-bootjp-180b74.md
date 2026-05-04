---
title: "tmpfsを使ったDISK IOの高速化のススメ｜bootjp"
type: "topic"
tags:
  - "docker"
  - "performance"
  - "bootjp"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/tmpfsを使ったDISK IOの高速化のススメ｜bootjp.md"
summary: "本記事は、メインメモリをファイルシステムとして利用する`tmpfs`を活用し、アプリケーションのDISK IO性能を向上させる手法について解説しています。"
---

# tmpfsを使ったDISK IOの高速化のススメ｜bootjp

## 概要

本記事は、メインメモリをファイルシステムとして利用する`tmpfs`を活用し、アプリケーションのDISK IO性能を向上させる手法について解説しています。

*発行: 2019-07-30 / [[docker-performance-tmpfs-disk-bootjp-180b74]]*

## 主要なトピック

- [[docker]]
- [[performance]]
- [[bootjp]]

## 詳細

- 本記事は、メインメモリをファイルシステムとして利用する`tmpfs`を活用し、アプリケーションのDISK IO性能を向上させる手法について解説しています。
- 主な要点
- **tmpfsとは**
- メインメモリをファイルシステムとして扱う技術（RAMディスクに近い）。
- 高速なアクセスが可能で、Linux環境であれば特別な設定なしで利用可能。
- **利用時の注意点**
- **揮発性:** 再起動時にデータが消えるため、再生成可能な一時データやキャッシュ向け。
- **メモリ消費:** 物理メモリを消費するため、容量予測と制限が必須（OOM KillやSwap発生のリスクに注意）。
- **Docker環境での活用**

*発行: 2019-07-30 / [[docker-performance-tmpfs-disk-bootjp-180b74]]*

## 関連テーマ

- [[docker]]
- [[performance]]
- [[bootjp]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/tmpfsを使ったDISK IOの高速化のススメ｜bootjp.md`
- https://note.com/bootjp/n/ndf0e2ceecfee
