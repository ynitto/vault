---
title: "vshn/asciidoctor-confluence-exporter: Command and Docker image to export Confluence wiki content to AsciiDoc"
type: "topic"
tags:
  - "python"
  - "authentication"
  - "docker"
  - "networking"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/vshnasciidoctor-confluence-exporter Command and Docker image to export Confluence wiki content to AsciiDoc.md"
summary: "Confluence to AsciiDoc Exporter の概要"
---

# vshn/asciidoctor-confluence-exporter: Command and Docker image to export Confluence wiki content to AsciiDoc

## 概要

Confluence to AsciiDoc Exporter の概要

## 主要なトピック

- [[python]]
- [[authentication]]
- [[docker]]
- [[networking]]

## 詳細

- このプロジェクトは、Confluence Wiki上のページを読み込み、AsciiDoc形式に変換して出力するPythonツールです。Dockerイメージとしても提供されています。
- 主な特徴と要点
- **機能**: ConfluenceのページIDを指定し、内容をAsciiDocとして取得・表示。
- **動作環境**:
- Python 3
- Pandoc (変換エンジン)
- **セキュリティ**: 認証情報（ユーザー名・パスワード）は環境変数 `CONFLUENCE_USERNAME` および `CONFLUENCE_PASSWORD` で管理。
- **Docker利用**: コンテナイメージ `ghcr.io/vshn/asciidoctor-confluence-exporter` を利用可能。
- 実行例: `podman run --rm --env-file credentials --volume "${PWD}":/data ghcr.io/vshn/asciidoctor-confluence-exporter:1.2 --wiki=https://wiki.url <page-id>`

## 関連テーマ

- [[python]]
- [[authentication]]
- [[docker]]
- [[networking]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/vshnasciidoctor-confluence-exporter Command and Docker image to export Confluence wiki content to AsciiDoc.md`
- https://github.com/vshn/asciidoctor-confluence-exporter
