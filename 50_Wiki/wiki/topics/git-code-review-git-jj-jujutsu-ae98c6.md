---
title: "Git の次へ。jj（Jujutsu）が変えるバージョン管理の常識"
type: "topic"
tags:
  - "git"
  - "code-review"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Git の次へ。jj（Jujutsu）が変えるバージョン管理の常識.md"
summary: "Googleエンジニアが開発した、Gitと完全互換性を持つ次世代バージョン管理システムです。Gitの複雑なワークフローを簡略化し、学習コストを低減すること…"
---

# Git の次へ。jj（Jujutsu）が変えるバージョン管理の常識

## 概要

Googleエンジニアが開発した、Gitと完全互換性を持つ次世代バージョン管理システムです。Gitの複雑なワークフローを簡略化し、学習コストを低減することを目指しています。

*発行: 2026-01-27 / [[git-code-review-git-jj-jujutsu-ae98c6]]*

## 主要なトピック

- [[git]]
- [[code-review]]

## 詳細

- Googleエンジニアが開発した、Gitと完全互換性を持つ次世代バージョン管理システムです。Gitの複雑なワークフローを簡略化し、学習コストを低減することを目指しています。
- 主要な利点
- **ステージング不要**: ワーキングコピーが直接コミットされるため、`git add` が不要。
- **ダーティな状態の解消**: 常にコミットベースで管理するため `git stash` が不要。
- **柔軟なundo**: すべての操作がログに記録され、`jj undo` で直前の操作を簡単に取り消せる。
- **コンフリクトの扱い**: コンフリクトを「第一級オブジェクト」として保持でき、後から解消が可能。
- **自動リベース**: 親コミットの修正が子孫コミットに自動で反映される。
- Gitとの関係性
- **完全な互換性**: 既存のGitリポジトリに対して `jj git init --colocate` を実行するだけで導入可能。

*発行: 2026-01-27 / [[git-code-review-git-jj-jujutsu-ae98c6]]*

## 関連テーマ

- [[git]]
- [[code-review]]

## 出典

- `60_Resources/Git の次へ。jj（Jujutsu）が変えるバージョン管理の常識.md`
- https://zenn.dev/yamitake/articles/jj-jujutsu-modern-vcs-guide
