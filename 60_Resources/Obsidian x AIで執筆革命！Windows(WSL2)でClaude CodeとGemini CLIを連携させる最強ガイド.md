---
title: Obsidian x AIで執筆革命！Windows(WSL2)でClaude CodeとGemini CLIを連携させる最強ガイド
source: https://qiita.com/toki_mwc/items/c1c448344a2ecb810eb1
author:
- '[[toki_mwc]]'
published: 2025-07-07
created: 2026-04-19
description: 「Obsidianでの知的生産をもっと効率化したい…」 「話題のClaude CodeやGemini CLIを使いたいけど、Windowsだと面倒くさそう…」
  そんなお悩みを持つWindowsユーザーのあなたに朗報です！本記事では、**Windows Subsystem f...
tags:
- resource/web
- obsidian
- ai-agent
- windows
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/Obsidian x AIで執筆革命！Windows(WSL2)でClaude CodeとGemini
  CLIを連携させる最強ガイド.md
copied_at: 2026-04-19 10:51:13+09:00
---
## Qiita記事「Obsidian x AIで執筆革命！」要約

本記事は、Windows環境でObsidian、Claude Code、Gemini CLIを連携させ、次世代のAI執筆環境を構築する手順を解説する。

### 1. 最強の組み合わせ

*   **Obsidian**: ナレッジベース
*   **Claude Code**: AIエージェント（ファイル整理、リファクタリング）
*   **Gemini CLI**: AIパートナー（リサーチ、アイデア出し、執筆）
*   **Windows + WSL2**: 安定した実行環境

### 2. 環境構築手順

1.  **WSL2とNode.jsのインストール**: WindowsにWSL2をインストールし、Ubuntu上でNode.js (v20.x) をセットアップする。
2.  **AIツールのインストール**: `npm` を使用してClaude CodeとGemini CLIをグローバルインストールする。
3.  **Obsidian Terminalプラグイン設定**: ObsidianのTerminalプラグインで、WSL2を呼び出すプロファイルを設定する。
4.  **指示書ファイル作成**: `CLAUDE.md` (整理・構成担当) と `GEMINI.md` (執筆・アイデア担当) を作成し、AIの役割とルールを定義する。
5.  **AIとの対話**: Obsidianのターミナルから `claude` または `gemini` コマンドでAIを起動し、指示書に基づいた対話（ファイル整理、記事作成など）を行う。

### 3. まとめ

この環境により、Obsidianが知的生産プラットフォームとなり、AIと共に思考からアウトプットまでをシームレスに行えるようになる。