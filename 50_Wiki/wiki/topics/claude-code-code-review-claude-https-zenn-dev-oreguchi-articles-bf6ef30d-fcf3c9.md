---
title: "あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った"
type: "topic"
tags:
  - "claude-code"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った.md"
summary: "Claude Codeなどの既存AIスキルを、言語・ロケール・実行エージェントといった3つの軸で、意図した通りの仕様に正確に変換するプラグイン「skill…"
---

# あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った

## 概要

Claude Codeなどの既存AIスキルを、言語・ロケール・実行エージェントといった3つの軸で、意図した通りの仕様に正確に変換するプラグイン「skill-conversion」の紹介。

*発行: 2026-04-28 / [[claude-code-code-review-claude-https-zenn-dev-oreguchi-articles-bf6ef30d-fcf3c9]]*

## 主要なトピック

- [[claude-code]]
- [[code-review]]

## 詳細

- Claude Codeなどの既存AIスキルを、言語・ロケール・実行エージェントといった3つの軸で、意図した通りの仕様に正確に変換するプラグイン「skill-conversion」の紹介。
- 主な要点
- **変換の3軸モデル**: プログラミング言語・FW、自然言語、実行エージェントを独立して変更可能。
- **7つの設計機構**:
- **変換規則表**: 翻訳前に対応表を確定し、揺れを抑制。
- **追加台帳**: ユーザー承認のない機能追加を禁止し、監査ログを保持。
- **不動点レビューループ**: 2パス連続ゼロ変更で品質を担保。
- **差分レポート**: 変換内容の詳細サマリと総合判定を出力。
- **Conversion Profile**: 忠実度・バランス・有用性の3段階から期待値を宣言。

*発行: 2026-04-28 / [[claude-code-code-review-claude-https-zenn-dev-oreguchi-articles-bf6ef30d-fcf3c9]]*

## 関連テーマ

- [[claude-code]]
- [[code-review]]

## 出典

- `../60_Resources/あらゆるスキルを自分のプラットフォーム仕様に変換するClaude Codeプラグインを作った.md`
- https://zenn.dev/oreguchi/articles/bf6ef30d916552
