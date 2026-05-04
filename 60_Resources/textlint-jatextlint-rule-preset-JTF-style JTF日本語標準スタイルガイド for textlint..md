---
title: "textlint-ja/textlint-rule-preset-JTF-style: JTF日本語標準スタイルガイド for textlint."
source: "https://github.com/textlint-ja/textlint-rule-preset-JTF-style"
author:
published:
created: 2026-05-01
description: "JTF日本語標準スタイルガイド for textlint. Contribute to textlint-ja/textlint-rule-preset-JTF-style development by creating an account on GitHub."
tags:
  - "clippings"
---
### 概要
`textlint-rule-preset-JTF-style`は、日本語の文章作成において「JTF日本語標準スタイルガイド（翻訳用）」に準拠したチェックを自動化するための`textlint`用ルールセットです。

### 主な要点
- **目的**: 日本語翻訳・執筆時の表記ゆれやスタイルガイドへの準拠を`textlint`で機械的にチェックする。
- **主な機能**:
  - 句読点の全角統一、算用数字の半角統一などの自動チェック。
  - `--fix`オプションによる一部ルールの自動修正対応。
- **導入と利用**:
  - `npm install -D textlint textlint-rule-preset-jtf-style`でインストール可能。
  - プロジェクトルートの`.textlintrc`で`\\"preset-jtf-style\\": true`と設定して利用を推奨。
- **カスタマイズ性**:
  - ルールごとの有効・無効化や、特定のルールのオプション設定（例：半角かっこ前後のスペース制御）が可能。
- **保守と貢献**:
  - コミュニティ主導で開発されており、未実装ルールのPull RequestやGitHub Issuesによるフィードバックを歓迎。