---
title: "uv （pythonパッケージマネージャー）の使い方　詳細版"
type: "topic"
tags:
  - "git"
  - "ci-cd"
  - "docker"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/uv （pythonパッケージマネージャー）の使い方　詳細版.md"
summary: "uvは、Rustで記述された高速かつモダンなPythonプロジェクト・パッケージマネージャーです。pip、venv、poetry等の機能を統合し、単体でP…"
---

# uv （pythonパッケージマネージャー）の使い方　詳細版

## 概要

uvは、Rustで記述された高速かつモダンなPythonプロジェクト・パッケージマネージャーです。pip、venv、poetry等の機能を統合し、単体でPythonバージョンの管理から依存関係の解決、ツール実行までを完結できます。

*発行: 2024-11-02 / [[git-ci-cd-uv-python-https-7774aa]]*

## 主要なトピック

- [[git]]
- [[ci-cd]]
- [[docker]]
- [[performance]]

## 詳細

- uvは、Rustで記述された高速かつモダンなPythonプロジェクト・パッケージマネージャーです。pip、venv、poetry等の機能を統合し、単体でPythonバージョンの管理から依存関係の解決、ツール実行までを完結できます。
- 主な特徴と機能
- **圧倒的な高速性能**: Rust製で並行処理や効率的なキャッシュ機構により、インストールや環境構築が非常に高速。
- **オールインワン**: Python本体の管理、仮想環境の構築、パッケージの追加・削除、プロジェクト設定を一括で行える。
- **標準への準拠**: `pyproject.toml`（PEP 621）をベースとし、クロスプラットフォームで一貫した `uv.lock` を生成。
- **柔軟な実行**:
- `uv run`: スクリプトやツールを隔離環境で実行。
- `uvx`: インストール不要でパッケージを一時実行。
- インラインメタデータによる依存宣言をサポート。

*発行: 2024-11-02 / [[git-ci-cd-uv-python-https-7774aa]]*

## 関連テーマ

- [[git]]
- [[ci-cd]]
- [[docker]]
- [[performance]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/uv （pythonパッケージマネージャー）の使い方　詳細版.md`
- https://zenn.dev/tabayashi/articles/52389e0d6c353a
