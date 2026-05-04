---
title: "Ansible 2.6 — replace モジュールを使って置換する"
source: "https://qiita.com/YumaInaura/items/0cf2976b09d0658fc38e"
author:
  - "[[YumaInaura]]"
published: 2018-08-02
created: 2026-04-30
description: "replace module を使うことでファイル内の文字列を置換できる。 パラメータ 基本 パラメータ 説明 path リモートマシン上のファイルパス regexp マッチさせる正規表現https://docs.python.org/2/librar..."
tags:
  - "clippings"
---
### Ansible `replace` モジュールの概要
本記事では、Ansible 2.6の`replace`モジュールを使用したファイル内の文字列置換方法を解説しています。

### 要点まとめ
- **機能**: 正規表現を用いてファイル内の特定の文字列を一括置換します。
- **主要パラメータ**:
    - `path`: 対象のファイルパス。
    - `regexp`: マッチさせる正規表現（行単位の制御が可能）。
    - `replace`: 置換後の文字列（省略時は削除）。
- **便利なオプション**:
    - `backup`: 置換前にバックアップを作成（`yes`で有効）。
    - `unsafe_writes`: 非アトミックな書き込みモードへの変更。
- **活用例**: 正規表現のキャプチャグループ（`()`）と後方参照（`\1`）を使用することで、柔軟な置換が可能です。
- **注意点**: 最終更新から時間が経過しているため、最新の公式ドキュメントと併せて確認することが推奨されます。
