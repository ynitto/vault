---
title: Obsidianで最適なPKM環境を考える
source: https://zenn.dev/game8_blog/articles/0e50c36cd63b98
author: null
published: 2023-12-20
created: 2026-04-19
description: null
tags:
- resource/web
- obsidian
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/Obsidianで最適なPKM環境を考える.md
copied_at: 2026-04-19 10:51:13+09:00
---
# Obsidianで最適なPKM環境を構築する

情報の整理が苦手な著者が、負担を減らしつつ必要な情報を管理・整理するため、Obsidianを用いたPKM（Personal Knowledge Management）環境を構築する経緯と設定について解説します。

## 環境と使用ツール

-   **OS**: macOS
-   **主要ツール**: Obsidian, Git (GitHub)

## Obsidianを選択した理由

-   **ローカルで完結**: ネットワークやサービス障害に依存せず、思考を中断させないため。
-   **プレーンテキストで記述**: 不要な装飾の思考ノイズを排除し、書くことに集中するため。
-   **Markdown対応**: 馴染み深い記法でノイズが少なく、将来的な移植性も高い。
-   **独立した作業環境**: ブラウザや開発エディタから隔離し、メモ作成に特化するため。
-   **高いカスタマイズ性**: プラグインでGit連携や自動化など、個人の要望に細かく対応できるため。
-   **豊富なメモ管理機能**: リンク、グラフビュー、階層型タグ、軽快な検索、デイリーノート機能など。
-   **その他**: 動作の軽快さ、PKMに特化した使用感、OSSによる持続性。

## Obsidianの主要設定

-   **保管庫の作成**: `~/Documents/notes/g8note` に作成。
-   **フォルダ構成**: 
    -   `_Configs` (Extra, Templates)
    -   `Daily`
    -   `Inbox`
-   **テンプレート設定**: 
    -   全てのメモに共通のFrontmatter (`id`, `aliases`, `tags`, `created`, `updated`) を用意。
    -   デイリーノートには日付を自動入力するテンプレート (`_Configs/Templates/Daily.md`) を設定。
    -   通常のノートにはTemplaterプラグインでFrontmatter (`_Configs/Templates/_frontmatter.md`) を自動挿入。
-   **更新日の自動更新**: Update time on edit plugin を導入し、Frontmatterの `updated` を5分間隔で自動更新（`_Configs`配下は除く）。
-   **Gitで変更管理**: Obsidian Gitプラグインを導入し、GitHubプライベートリポジトリで10分間隔で自動commit & push。
-   **「とりあえず書く」環境の実現**: Obsidian Memosプラグインを導入し、X（旧Twitter）のようなUIでデイリーノートにフロー情報を即座に記録。⌘Enterで投稿可能に設定。

## 設定しなかった機能

-   **Zettelkastenのユニークノートクリエイター**: Prefixが長すぎたり、意味のない数字列がノイズになるため見送り。フロー情報はデイリーノートで対応。

## 日々の運用

-   MacBook起動中は常にObsidianを起動。
-   Memosと記事編集、プレビューの3ペイン構成で使用。
-   思いついたことはMemosに即座に書き留める。
-   Memosのフロー情報は、気が向いた時にストックメモに整理。
-   整理済みのMemosは完了チェックまたは削除し、溜め込みすぎないよう習慣づける。
-   Markdown入力の即時プレビューによる「心地よさ」を重視し、継続的な利用を促す。