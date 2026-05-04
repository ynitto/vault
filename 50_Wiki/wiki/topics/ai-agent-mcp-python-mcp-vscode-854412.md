---
title: "Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する"
type: "topic"
tags:
  - "ai-agent"
  - "mcp"
  - "python"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する.md"
summary: "VSCode v1.99で導入された「Copilot Agent Mode」において、MCP（Model Context Protocol）を使用して外部…"
---

# Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する

## 概要

VSCode v1.99で導入された「Copilot Agent Mode」において、MCP（Model Context Protocol）を使用して外部ツールをAIに利用させる手法を解説した記事です。

*発行: 2025-04-30 / [[ai-agent-mcp-python-mcp-vscode-854412]]*

## 主要なトピック

- [[ai-agent]]
- [[mcp]]
- [[python]]

## 詳細

- VSCode v1.99で導入された「Copilot Agent Mode」において、MCP（Model Context Protocol）を使用して外部ツールをAIに利用させる手法を解説した記事です。
- 要点まとめ
- **MCPとは**
- AI Agentが外部データやツールと連携するための標準プロトコル。
- 「AIがタスク実行のために外部ツールを使う仕組み」と理解すればOK。
- **ハンズオン：MCPサーバー実装の流れ**
- 1. **実装**: Python SDK（`mcp`パッケージ）を利用し、計算機能（add/subtract）を持つサーバーを作成。
- 2. **起動方式**: `stdio`を利用することで、同一ホスト上のVSCodeと安全かつ高速に連携。
- 3. **設定**: VSCodeの`setting.json`にサーバーの起動コマンドを指定し、エディタから認識させる。

*発行: 2025-04-30 / [[ai-agent-mcp-python-mcp-vscode-854412]]*

## 関連テーマ

- [[ai-agent]]
- [[mcp]]
- [[python]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Pythonで自作したMCPサーバーをVSCode Copilot Agentから利用する.md`
- https://zenn.dev/mochizuki875/articles/1f7f3f3527fcf9
