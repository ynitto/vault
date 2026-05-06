---
title: "Obsidianをチームで使えるようにしたいin閉域環境なJTC"
type: "topic"
tags:
  - "obsidian"
  - "git"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Obsidianをチームで使えるようにしたいin閉域環境なJTC.md"
summary: "Obsidian Vaultの一部を共有用サブモジュールとして切り出し、チームで参照可能に。"
---

# Obsidianをチームで使えるようにしたいin閉域環境なJTC

## 概要

Obsidian Vaultの一部を共有用サブモジュールとして切り出し、チームで参照可能に。

*発行: 2025-12-06 / [[obsidian-git-obsidian-jtc-https-12d339]]*

## 主要なトピック

- [[obsidian]]
- [[git]]

## 詳細

- Tl;DR
- Obsidian Vaultの一部を共有用サブモジュールとして切り出し、チームで参照可能に。
- 接続点は共有フォルダ（SMBサーバ）のみ。
- インターネットに繋がらない（閉域環境／イントラネット）で運用。
- 背景と課題
- JTC（日本の伝統的な大企業）の厳しいIT制約（ソフトウェアインストール、新規サーバ設置不可、インターネット接続制限）。
- 2025年2月にObsidianが商用利用無償化され、社内PCでの利用が許可された。
- ナレッジベースとしてObsidianをチームで活用したいが、Gitサーバを立てられない、共有フォルダ（SMB）でのGit運用は衝突に脆弱という問題。
- 解決策：3種類のリポジトリとGitサブモジュール/sparse-checkoutの活用

*発行: 2025-12-06 / [[obsidian-git-obsidian-jtc-https-12d339]]*

## 関連テーマ

- [[obsidian]]
- [[git]]

## 出典

- `60_Resources/Obsidianをチームで使えるようにしたいin閉域環境なJTC.md`
- https://zenn.dev/ningensei848/articles/obsidian-air-gapped-team-sync
