---
original_source: 00_Inbox/Clippings/Obsidian CLI が全ユーザーに無料開放されたので Claude Code 用スキルと一緒にセットアップした.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, obsidian, ai-agent, 2026-04]
---

---
title: "Obsidian CLI が全ユーザーに無料開放されたので Claude Code 用スキルと一緒にセットアップした"
source: "https://zenn.dev/kairininja/articles/zenn-obsidian-cli-agent-skills-setup"
author:
published: 2026-03-27
created: 2026-04-19
description:
tags:
  - "clippings"
---
# Obsidian CLI 無料開放とClaude Code用スキルセットアップ

Obsidian v1.12.7以降、公式CLIが全ユーザーに無料で開放されました。これに伴い、CLIのセットアップと、Obsidian CEOが公開するClaude Code用エージェントスキル「kepano/obsidian-skills」の導入方法が解説されています。

## Obsidian CLIとは
*   Obsidian v1.12で導入された公式コマンドラインインターフェース。
*   GUIで可能な操作のほぼ全てをターミナルから実行可能。
*   ノートの作成、読み取り、検索、追記などがターミナルから行える。
*   シェルスクリプトやAIエージェントとの連携が想定されている。
*   v1.12.7で専用バイナリに置き換えられ、大幅に高速化。
*   コマンド自動補完に対応。

## CLI セットアップ手順
1.  **Obsidianのアップデート**: Obsidianをv1.12.7以降にアップデート。
2.  **CLIの有効化**: `Settings` → `General` → `Command line interface` でCLIを有効化し、`obsidian`コマンドをシステムPATHに追加。
3.  **動作確認**: `obsidian version`または`obsidian help`を実行。
    *   **注意**: Windowsでは管理者権限でターミナルを起動しないこと。

## 主なCLIコマンド
| コマンド                     | 説明                     |
| :--------------------------- | :----------------------- |
| `obsidian daily`             | 今日のデイリーノートを開く |
| `obsidian daily:append`      | デイリーノートに追記     |
| `obsidian create`            | ノートを作成             |
| `obsidian read`              | ノートを読み取る         |
| `obsidian search`            | ノートを検索             |
| `obsidian plugin:reload`     | プラグインをリロード     |

## kepano/obsidian-skillsの導入
### obsidian-skillsとは
*   Obsidian CEOのkepano（Steph Ango）が公開するエージェントスキル集。
*   Claude CodeなどのAIエージェントにObsidianの操作方法を教えるスキルファイル群。
*   CLI経由のVault操作、Markdown記法、.baseファイル操作、.canvasファイル操作などが含まれる。

### 導入手順
1.  **インストール**: Claude Codeのセッション内で`/plugin marketplace add kepano/obsidian-skills`を実行、またはリポジトリの内容をVaultルートの`/.claude`フォルダに手動で配置。
2.  **動作確認**: Claude Codeに「今日のデイリーノートにテストと追記して」と依頼し、`obsidian daily:append`コマンドが実行されるか確認。