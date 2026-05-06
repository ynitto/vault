---
title: "ansible.builtin.blockinfile - テキストファイルの内容を複数行単位で編集する"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ansible.builtin.blockinfile - テキストファイルの内容を複数行単位で編集する.md"
summary: "`ansible.builtin.blockinfile` は、テキストファイル内に**複数行のテキストブロックを挿入、更新、削除**するためのモジュール…"
---

# ansible.builtin.blockinfile - テキストファイルの内容を複数行単位で編集する

## 概要

`ansible.builtin.blockinfile` は、テキストファイル内に**複数行のテキストブロックを挿入、更新、削除**するためのモジュールです。変更箇所は「マーカーライン」で囲まれ、次回実行時の目印として利用されます。

## 主要なトピック


## 詳細

- `ansible.builtin.blockinfile` は、テキストファイル内に**複数行のテキストブロックを挿入、更新、削除**するためのモジュールです。変更箇所は「マーカーライン」で囲まれ、次回実行時の目印として利用されます。
- 主要な機能・ポイント
- **柔軟な挿入位置**: `insertafter` や `insertbefore` を使用して、正規表現に一致する行の前後、ファイルの先頭（BOF）、末尾（EOF）を指定可能。
- **管理の自動化**: マーカーライン（デフォルトは `# BEGIN/END ANSIBLE MANAGED BLOCK`）により、同じテキストブロックの更新や削除を冪等的に処理。
- **マーカーのカスタマイズ**: `marker` パラメーターでマーカーラインの形式を自由に変更可能。これにより、同一ファイル内に複数の管理ブロックを配置しても競合を防げます。
- **ファイル作成**: `create: yes` を設定すると、対象ファイルが存在しない場合に自動生成します。
- **状態管理**: `state: present`（挿入・更新）と `state: absent`（削除）で制御します。

## 関連テーマ


## 出典

- `60_Resources/ansible.builtin.blockinfile - テキストファイルの内容を複数行単位で編集する.md`
- https://zenn.dev/y_mrok/books/ansible-no-module-no-tsukaikata/viewer/ansible_builtin_blockinfile
