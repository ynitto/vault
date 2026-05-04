---
title: "GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った"
type: "topic"
tags:
  - "ai-agent"
  - "git"
  - "networking"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った.md"
summary: "GitHubのリポジトリを「掲示板」として利用することで、離れた場所にある2台のPC間でGitHub Copilot Agentを協調させる仕組み「GH-…"
---

# GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った

## 概要

GitHubのリポジトリを「掲示板」として利用することで、離れた場所にある2台のPC間でGitHub Copilot Agentを協調させる仕組み「GH-Copilot Multi Agent Mission Board」を開発し、自宅ネットワークでのトラブル原因を特定したという報告記事です。

*発行: 2026-04-17 / [[ai-agent-git-copilot-agent-teams-6dc7c4]]*

## 主要なトピック

- [[ai-agent]]
- [[git]]
- [[networking]]

## 詳細

- GitHubのリポジトリを「掲示板」として利用することで、離れた場所にある2台のPC間でGitHub Copilot Agentを協調させる仕組み「GH-Copilot Multi Agent Mission Board」を開発し、自宅ネットワークでのトラブル原因を特定したという報告記事です。
- 要点
- **コンセプト**: Gitリポジトリをメッセージ基盤（掲示板）として利用。APIや専用バスを使わず、Gitのpush/pullのみで複数Agentを連携。
- **自律化**: 自作のVS Code拡張「Copilot Scheduler」を用いて`/pull`コマンドを定期実行し、完全自律運転を実現。
- **実用例**: 「RDP突然死」というトラブルを、2台のAgentがそれぞれ別角度（パケット解析・NIC設定確認）から調査することで特定。原因は「Global Secure Access (GSA) Client」による通信インターセプトでした。
- **特徴と利点**:
- 特別なインフラ不要で、GitHub環境のみで利用可能。
- 「何を確認させるか」を事前に定義・設計することで、放置状態でも調査が進む。
- **公開情報**: テンプレートリポジトリとして[GitHubにて公開中](https://github.com/aktsmm/gh-copilot-multi-agent-mission-board)。

*発行: 2026-04-17 / [[ai-agent-git-copilot-agent-teams-6dc7c4]]*

## 関連テーマ

- [[ai-agent]]
- [[git]]
- [[networking]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った.md`
- https://qiita.com/aktsmm/items/28f38fd1edea4edab31b
