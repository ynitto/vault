---
title: ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応)
source: https://zenn.dev/tokium_dev/articles/2fc1fa15407efe
author:
published: 2026-02-25
created: 2026-05-31
description:
tags:
  - clippings
---
### 概要
大学院生でインターン生のRAIT-09氏が、ObsidianからClaude CodeやGemini CLIなどのAIエージェントを直接操作できるプラグイン「**Obsidian Agent Client Plugin**」を開発しました。Agent Client Protocol (ACP) を利用することで、エディタとAIエージェントのシームレスな統合を実現しています。

### 主なポイント
*   **開発の背景**: 従来の「Obsidianとターミナルの行き来」という非効率なワークフローを解消し、Obsidian内でのメモ・執筆・調査の一元管理を目指しました。
*   **プラグインの強み**
    *   **統合環境**: サイドパネルでAIと直接チャットが可能。
    *   **既存ツール活用**: Claude Code等の既存機能をそのまま利用でき、API料金の二重負担も発生しません。
    *   **柔軟性**: ACP対応エージェントであれば、Gemini CLI等とも自由に接続可能です。
*   **便利な機能**
    *   **ノート自動メンション**: 開いているノートを自動でコンテキストとしてAIに伝達。
    *   **履歴管理**: チャットをノートとして保存・再利用可能。
    *   **並列セッション**: 複数のエージェントを同時に動かして作業が可能。
*   **技術的な仕組み**
    *   **ACP (Agent Client Protocol)**: AIエージェントとクライアント（Obsidian）間の通信をJSON-RPC 2.0で標準化。
    *   **アーキテクチャ**: Node.jsの`child_process`を使用してエージェントを子プロセスとして制御し、双方向の通信を実現しています。
