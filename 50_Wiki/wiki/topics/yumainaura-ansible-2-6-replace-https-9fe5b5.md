---
title: "Ansible 2.6 — replace モジュールを使って置換する"
type: "topic"
tags:
  - "yumainaura"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Ansible 2.6 — replace モジュールを使って置換する.md"
summary: "Ansible `replace` モジュールの概要"
---

# Ansible 2.6 — replace モジュールを使って置換する

## 概要

Ansible `replace` モジュールの概要

*発行: 2018-08-02 / [[yumainaura-ansible-2-6-replace-https-9fe5b5]]*

## 主要なトピック

- [[yumainaura]]

## 詳細

- 本記事では、Ansible 2.6の`replace`モジュールを使用したファイル内の文字列置換方法を解説しています。
- 要点まとめ
- **機能**: 正規表現を用いてファイル内の特定の文字列を一括置換します。
- **主要パラメータ**:
- `path`: 対象のファイルパス。
- `regexp`: マッチさせる正規表現（行単位の制御が可能）。
- `replace`: 置換後の文字列（省略時は削除）。
- **便利なオプション**:
- `backup`: 置換前にバックアップを作成（`yes`で有効）。

*発行: 2018-08-02 / [[yumainaura-ansible-2-6-replace-https-9fe5b5]]*

## 関連テーマ

- [[yumainaura]]

## 出典

- `../60_Resources/Ansible 2.6 — replace モジュールを使って置換する.md`
- https://qiita.com/YumaInaura/items/0cf2976b09d0658fc38e
