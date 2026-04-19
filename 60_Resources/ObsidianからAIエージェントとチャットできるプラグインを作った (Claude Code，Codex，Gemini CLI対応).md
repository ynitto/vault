---
original_source: 00_Inbox/Clippings/ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応).md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, obsidian, ai-agent, 2026-04]
---

---
title: "ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応)"
source: "https://zenn.dev/tokium_dev/articles/2fc1fa15407efe"
author:
published: 2026-02-25
created: 2026-04-19
description:
tags:
  - "clippings"
---
# Obsidian Agent Client Plugin: AIエージェントとチャット

## はじめに
*   **Obsidian Agent Client Plugin**は、Obsidian内でClaude CodeやGemini CLIなどのAIエージェントとチャットできる個人開発プラグイン。
*   Agent Client Protocol (ACP) を基盤とし、ノートの要約、整理、文章執筆、調査などをObsidian内で完結。

## 開発背景
*   **既存の課題**: ObsidianとAIの連携が不便（ターミナルとの切り替え、有料機能の制限、API利用料の問題）。
*   TOKIUMの「AI 100K」制度でClaude Codeを日常的に使う中で、この不便さを解消したいと考え開発。

## 機能と強み
### 3つの強み
1.  **Obsidianに統合**: サイドパネルでチャットが完結し、シームレスな作業が可能。
2.  **エージェントの機能そのまま**: MCPサーバー、カスタムコマンド、Web検索など、各エージェントの機能が利用でき、既存のサブスクリプションも活用可能。
3.  **好きなエージェントを選べる**: ACP対応エージェントなら接続可能で、タスクに応じた使い分けや新エージェントの試用が可能。

### 便利な機能
*   **ノートの自動メンション**: 開いているノートのコンテキストを自動的にエージェントに伝達。
*   **チャットのエクスポート**: チャット履歴をObsidianノートとして保存・再利用可能。
*   **セッションの並列実行**: 複数のエージェントセッションを同時に実行可能。

## セットアップガイド (Claude Codeの例)
1.  **前提**: Obsidian, Node.jsのインストール、Claude CodeサブスクリプションまたはAnthropic APIキー。
2.  **プラグインのインストール**: BRAT経由で「Obsidian Agent Client」をインストール・有効化。
3.  **Claude Codeのインストールと認証**: Claude Code本体とACPアダプターをインストールし、認証を行う。
4.  **プラグインの設定**: Node.jsと`claude-agent-acp`のパスをObsidian設定で指定。チャットパネルを開いて「こんにちは」などで動作確認。

## 技術的な仕組み
### Agent Client Protocol (ACP) とは
*   AIエージェントとエディタ間の通信を標準化するオープンプロトコル（Zed Editorチーム策定）。
*   Language Server Protocol (LSP) と同様に、エージェントとクライアント間の相互運用性を高める。
*   **Agent**: AIを使ってタスクを実行するプログラム。
*   **Client**: ユーザーとエージェントの間のインターフェース（本プラグイン）。

### 通信の仕組み
*   **JSON-RPC 2.0ベース**: クライアントがエージェントを子プロセスとして起動し、標準入出力でJSONメッセージをやり取り。
*   **双方向通信**: クライアントからエージェントへのリクエストだけでなく、エージェントからクライアントへの権限リクエストなども発生。
*   **通信フェーズ**: 初期化 → セッション開始 → プロンプトターン（session/update通知による進行状況ストリーミング）

### プラグインの設計
*   **Electron (Node.js)**: `child_process`モジュールでエージェントプロセス起動とJSON-RPC通信を実現。
*   **メッセージ分離**: ユーザーに表示されるメッセージと、エージェントに送るメッセージ（自動でノートパスやコンテキストを付加）を区別。
*   **権限リクエストのハンドリング**: Promiseを使用してエージェントからの双方向の権限要求（例: ファイル編集）を非同期で処理。複数のリクエストも順次提示。

## まとめ
*   Obsidian Agent Client PluginはGitHubで800以上のStarを獲得し、ACP公式サイトにも掲載。
*   今後の開発目標は、セットアップの簡略化、公式コミュニティプラグイン化、機能拡充。
*   TOKIUMではAIエージェントエンジニアを含む多様なポジションで人材を募集。