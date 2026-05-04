---
title: "Amazon Q(Kiro)CLIを起動するとターミナルが激重になるのを解消した話"
type: "topic"
tags:
  - "aws"
  - "python"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon Q(Kiro)CLIを起動するとターミナルが激重になるのを解消した話.md"
summary: "Amazon Q CLI起動時にターミナルが非常に重くなり、クラッシュする問題が発生。原因は、`mise`のPython環境設定が不完全で、shimが無限…"
---

# Amazon Q(Kiro)CLIを起動するとターミナルが激重になるのを解消した話

## 概要

Amazon Q CLI起動時にターミナルが非常に重くなり、クラッシュする問題が発生。原因は、`mise`のPython環境設定が不完全で、shimが無限ループしていたことでした。`mise`で正しいPythonバージョンをインストール・設定することで解決しました。

*発行: 2025-12-26 / [[aws-python-amazon-q-kiro-8b6656]]*

## 主要なトピック

- [[aws]]
- [[python]]

## 詳細

- Amazon Q CLI起動時にターミナルが非常に重くなり、クラッシュする問題が発生。原因は、`mise`のPython環境設定が不完全で、shimが無限ループしていたことでした。`mise`で正しいPythonバージョンをインストール・設定することで解決しました。
- 重要なポイント
- **現象**: ターミナルの起動が極端に遅く、頻繁にクラッシュする。
- **原因**:
- `mise`でPythonがインストールされていないにもかかわらず、shimパスが参照されていた。
- 不正な設定により、`mise/shims/python3`プロセスが無限に生成されCPUを圧迫。
- **解決策**:
- 該当プロセスの強制終了 (`kill`)。
- `mise install python@<version>` で適切に環境をインストール。

*発行: 2025-12-26 / [[aws-python-amazon-q-kiro-8b6656]]*

## 関連テーマ

- [[aws]]
- [[python]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Amazon Q(Kiro)CLIを起動するとターミナルが激重になるのを解消した話.md`
- https://qiita.com/masaozi3/items/53b98ea386397ec1ed8f
