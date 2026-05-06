---
title: "GitHub Copilot は自ら学ぶ: Copilot Memory 入門"
type: "topic"
tags:
  - "git"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/GitHub Copilot は自ら学ぶ Copilot Memory 入門.md"
summary: "GitHub Copilotがセッションを跨いで学習・記憶する「メモリ機能」の全体像と仕組みを解説する連載の第1回。メモリの分類（保存場所・共有範囲）を整…"
---

# GitHub Copilot は自ら学ぶ: Copilot Memory 入門

## 概要

GitHub Copilotがセッションを跨いで学習・記憶する「メモリ機能」の全体像と仕組みを解説する連載の第1回。メモリの分類（保存場所・共有範囲）を整理し、特にGitHubクラウド上に保存される「Copilot Memory」の重要性と技術的特性（リアルタイム検証機能など）について詳説しています。

*発行: 2026-04-05 / [[git-performance-copilot-memory-https-81237b]]*

## 主要なトピック

- [[git]]
- [[performance]]

## 詳細

- GitHub Copilotがセッションを跨いで学習・記憶する「メモリ機能」の全体像と仕組みを解説する連載の第1回。メモリの分類（保存場所・共有範囲）を整理し、特にGitHubクラウド上に保存される「Copilot Memory」の重要性と技術的特性（リアルタイム検証機能など）について詳説しています。
- 要点まとめ
- 1. メモリ機能の全体マップ
- **保存場所**: ローカル保存型（各環境依存）とクラウド保存型（GitHub CAPI経由）の2種類。
- **共有範囲**: ユーザー単位、リポジトリ単位、チャットセッション単位の3階層。
- 2. Copilot Memory（クラウド保存型）
- **リポジトリスコープ**: チームで共有可能な唯一のメモリ。
- **Just-in-time Verification**: `citations`（根拠となるコード場所）を保存し、使用時に現在のコードベースと一致するかリアルタイム検証するため、情報の陳腐化を防げる。
- **寿命と延命**: 未使用期間が28日を超えると自動削除されるが、使用されるたびに寿命がリセットされる。

*発行: 2026-04-05 / [[git-performance-copilot-memory-https-81237b]]*

## 関連テーマ

- [[git]]
- [[performance]]

## 出典

- `../60_Resources/GitHub Copilot は自ら学ぶ Copilot Memory 入門.md`
- https://zenn.dev/microsoft/articles/50863342150992
