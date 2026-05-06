---
title: "Git でファイル名の大文字小文字の変更が検出されない"
type: "topic"
tags:
  - "git"
  - "lx-sasabo"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/Git でファイル名の大文字小文字の変更が検出されない.md"
summary: "Gitでファイル名の大文字・小文字変更が反映されない問題への対策"
---

# Git でファイル名の大文字小文字の変更が検出されない

## 概要

Gitでファイル名の大文字・小文字変更が反映されない問題への対策

*発行: 2024-03-05 / [[git-lx-sasabo-git-https-qiita-com-lx-sasabo-items-2236926f37be67c777fa-3d1ada]]*

## 主要なトピック

- [[git]]
- [[lx-sasabo]]

## 詳細

- Gitの設定（`core.ignorecase`）が `true` の場合、ファイル名の大文字と小文字の変更が差分として検出されない現象が発生します。本記事では、この問題を解決するための2つの方法を紹介しています。
- 主な解決策
- **`git mv` コマンドを使用する**
- Gitのコマンド経由でリネームを行うことで、確実に変更を追跡させる方法です。（推奨）
- 実行例: `git mv wiki/topics/OldName.cs wiki/topics/NewName.cs`
- **`core.ignorecase` を `false` に設定する**
- 設定変更によりGitで大文字・小文字を区別させる方法です。
- コマンド: `git config core.ignorecase false`
- **注意:** プロジェクト環境によっては、既存のファイル認識に影響を与えたり、作りが壊れたりする可能性があるため、慎重な判断が求められます。

*発行: 2024-03-05 / [[git-lx-sasabo-git-https-qiita-com-lx-sasabo-items-2236926f37be67c777fa-3d1ada]]*

## 関連テーマ

- [[git]]
- [[lx-sasabo]]

## 出典

- `../60_Resources/Git でファイル名の大文字小文字の変更が検出されない.md`
- https://qiita.com/lx-sasabo/items/2236926f37be67c777fa
