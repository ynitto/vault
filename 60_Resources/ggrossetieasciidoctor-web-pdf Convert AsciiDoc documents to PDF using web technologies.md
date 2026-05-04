---
title: "ggrossetie/asciidoctor-web-pdf: Convert AsciiDoc documents to PDF using web technologies"
source: "https://github.com/ggrossetie/asciidoctor-web-pdf"
author:
published:
created: 2026-05-01
description: "Convert AsciiDoc documents to PDF using web technologies - ggrossetie/asciidoctor-web-pdf"
tags:
  - "clippings"
---
### Asciidoctor Web PDF の概要
Asciidoctor Web PDF は、Web 技術（CSS/JavaScript）を活用して AsciiDoc を PDF に変換するツールです。Paged.js を利用して、ブラウザ上で高度なレイアウトやページネーションを実現します。

### 主な特徴
- **柔軟なレイアウト**: CSS と JS で複雑なデザインが可能。
- **多彩な機能**: 数式（MathJax）、シンタックスハイライト（Highlight.js）、Font Awesome アイコン、目次、メタデータ設定をサポート。
- **カスタマイズ性**: テンプレートやスタイルシートの差し替えが容易。

### インストール方法
- **npm/Yarn**: プロジェクトへのインストールやグローバルインストールが可能。
- **Docker**: コンテナを利用して環境構築不要で利用可能。
- **バイナリ**: 各種 OS 用のプリコンパイル済みバイナリも提供。

### 基本的な使い方と設定
- **変換コマンド**: `asciidoctor-web-pdf document.adoc` で実行。
- **拡張機能**: `--require` オプションで Kroki などの拡張機能をロード可能。
- **デザイン調整**: stylesheet オプションや docinfo ファイルを用いて、フォントやヘッダー・フッター、ページ背景などを細かくカスタマイズ可能。
- **独自レイアウト**: `--template-require` を使用して独自の変換ロジックを適用可能。