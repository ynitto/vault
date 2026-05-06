---
title: "textlint-ja/textlint-rule-preset-JTF-style: JTF日本語標準スタイルガイド for textlint."
type: "topic"
tags:
  - "git"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/textlint-jatextlint-rule-preset-JTF-style JTF日本語標準スタイルガイド for textlint..md"
summary: "`textlint-rule-preset-JTF-style`は、日本語の文章作成において「JTF日本語標準スタイルガイド（翻訳用）」に準拠したチェック…"
---

# textlint-ja/textlint-rule-preset-JTF-style: JTF日本語標準スタイルガイド for textlint.

## 概要

`textlint-rule-preset-JTF-style`は、日本語の文章作成において「JTF日本語標準スタイルガイド（翻訳用）」に準拠したチェックを自動化するための`textlint`用ルールセットです。

## 主要なトピック

- [[git]]
- [[node-js]]

## 詳細

- `textlint-rule-preset-JTF-style`は、日本語の文章作成において「JTF日本語標準スタイルガイド（翻訳用）」に準拠したチェックを自動化するための`textlint`用ルールセットです。
- 主な要点
- **目的**: 日本語翻訳・執筆時の表記ゆれやスタイルガイドへの準拠を`textlint`で機械的にチェックする。
- **主な機能**:
- 句読点の全角統一、算用数字の半角統一などの自動チェック。
- `--fix`オプションによる一部ルールの自動修正対応。
- **導入と利用**:
- `npm install -D textlint textlint-rule-preset-jtf-style`でインストール可能。
- プロジェクトルートの`.textlintrc`で`\\"preset-jtf-style\\": true`と設定して利用を推奨。

## 関連テーマ

- [[git]]
- [[node-js]]

## 出典

- `60_Resources/textlint-jatextlint-rule-preset-JTF-style JTF日本語標準スタイルガイド for textlint..md`
- https://github.com/textlint-ja/textlint-rule-preset-JTF-style
