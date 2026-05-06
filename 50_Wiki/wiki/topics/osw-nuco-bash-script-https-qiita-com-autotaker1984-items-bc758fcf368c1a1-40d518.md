---
title: "Bash Scriptの作法"
type: "topic"
tags:
  - "osw-nuco"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Bash Scriptの作法.md"
summary: "チーム開発でBashスクリプトを保守しやすくするためのコーディングルールです。"
---

# Bash Scriptの作法

## 概要

チーム開発でBashスクリプトを保守しやすくするためのコーディングルールです。

*発行: 2021-09-23 / [[osw-nuco-bash-script-https-qiita-com-autotaker1984-items-bc758fcf368c1a1-40d518]]*

## 主要なトピック

- [[osw-nuco]]

## 詳細

- チーム開発でBashスクリプトを保守しやすくするためのコーディングルールです。
- 1. 基本設定
- **スクリプト名**: kebab-case（例: `deploy-server.sh`）で統一。
- **改行コード**: LFを使用（`.gitattributes`で設定を推奨）。
- **Shebang**: `#!/bin/bash` を使用。
- **おまじない**: `set -euxo pipefail` でエラーハンドリングを強化。
- **ディレクトリ**: `cd "$(dirname "$0")"` で実行パスを固定。
- 2. 変数と展開
- **変数宣言**: 右辺は `""` または `$()` で囲む。

*発行: 2021-09-23 / [[osw-nuco-bash-script-https-qiita-com-autotaker1984-items-bc758fcf368c1a1-40d518]]*

## 関連テーマ

- [[osw-nuco]]

## 出典

- `60_Resources/Bash Scriptの作法.md`
- https://qiita.com/autotaker1984/items/bc758fcf368c1a167353
