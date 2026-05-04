---
title: "vshn/asciidoctor-confluence-exporter: Command and Docker image to export Confluence wiki content to AsciiDoc"
source: "https://github.com/vshn/asciidoctor-confluence-exporter"
author:
published:
created: 2026-05-01
description: "Command and Docker image to export Confluence wiki content to AsciiDoc - vshn/asciidoctor-confluence-exporter"
tags:
  - "clippings"
---
### Confluence to AsciiDoc Exporter の概要
このプロジェクトは、Confluence Wiki上のページを読み込み、AsciiDoc形式に変換して出力するPythonツールです。Dockerイメージとしても提供されています。

### 主な特徴と要点
- **機能**: ConfluenceのページIDを指定し、内容をAsciiDocとして取得・表示。
- **動作環境**:
    - Python 3
    - Pandoc (変換エンジン)
- **セキュリティ**: 認証情報（ユーザー名・パスワード）は環境変数 `CONFLUENCE_USERNAME` および `CONFLUENCE_PASSWORD` で管理。
- **Docker利用**: コンテナイメージ `ghcr.io/vshn/asciidoctor-confluence-exporter` を利用可能。
    - 実行例: `podman run --rm --env-file credentials --volume "${PWD}":/data ghcr.io/vshn/asciidoctor-confluence-exporter:1.2 --wiki=https://wiki.url <page-id>`