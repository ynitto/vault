---
title: "Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する"
source: "https://zenn.dev/mochizuki875/articles/1f7f3f3527fcf9"
author:
published: 2025-04-30
created: 2026-04-30
description:
tags:
  - "clippings"
---
### 概要
VSCode v1.99で導入された「Copilot Agent Mode」において、MCP（Model Context Protocol）を使用して外部ツールをAIに利用させる手法を解説した記事です。

### 要点まとめ
- **MCPとは**
  - AI Agentが外部データやツールと連携するための標準プロトコル。
  - 「AIがタスク実行のために外部ツールを使う仕組み」と理解すればOK。

- **ハンズオン：MCPサーバー実装の流れ**
  1. **実装**: Python SDK（`mcp`パッケージ）を利用し、計算機能（add/subtract）を持つサーバーを作成。
  2. **起動方式**: `stdio`を利用することで、同一ホスト上のVSCodeと安全かつ高速に連携。
  3. **設定**: VSCodeの`setting.json`にサーバーの起動コマンドを指定し、エディタから認識させる。

- **結果**
  - Copilot Agentがツール情報を自動取得し、ユーザーの自然言語による指示に対して、適切なツールを実行・回答する環境が構築可能。

### 重要なポイント
- **Agent Modeの活用**: Copilotに特定のタスク（今回は計算）を委譲でき、自動化の幅が広がる。
- **通信の重要性**: ローカル開発では`stdio`が推奨されるが、リモート連携にはHTTP/SSEの考慮が必要。
