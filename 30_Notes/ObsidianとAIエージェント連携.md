---
created: 2026-04-19T10:05:19+09:00
source: 00_Inbox/Clippings/Obsidian CLI.md
tags: [ナレッジ, Obsidian, AI, CLI]
---

# ObsidianとAIエージェント連携

## 概要
Obsidian を AI エージェントの作業ハブとして使うには、Vault を「読む場所」から「取り込む・整理する・実行する場所」へ変える必要がある。今回のクリッピング群では、Obsidian CLI、Web Clipper、Claude Code 連携、WSL2 接続がその中核として繰り返し登場した。

## 詳細
### 最小構成
- Obsidian CLI を有効化し、Vault に対する read / append / daily / task 操作を端末から実行できる状態にする
- Web Clipper で raw source を Markdown として Vault に保存する
- Claude Code や他 CLI エージェントは、Vault 上のノートを編集対象にして運用する

### 運用の軸
- **入力層**: Web Clipper、チャットログ、簡易メモなどを `00_Inbox/` に集約する
- **整理層**: Daily / Weekly / Notes で情報を要約し、重複を削る
- **実行層**: Daily / Kanban / CLI から次アクションにつなげる

### 実装メモ
- WSL2 / Windows 連携では、Vault のパス解決と Obsidian 側の起動状態がつまずきやすい
- CLI 導入後は Daily Note 更新やタスク一覧取得など、低リスクなコマンドから自動化を試すのが安全
- プラグイン追加は後回しでよく、まずは CLI・MCP・Daily 運用の導線を作る方が効果が大きい

## 関連リンク
- [[10_Daily/2026-04-19]]
- [[11_Weekly/2026-W16]]
- [[30_Notes/LLM長期記憶と第二の脳]]

## 出典・参照
- `00_Inbox/Clippings/Obsidian CLI.md`
- `00_Inbox/Clippings/Obsidian CLI が全ユーザーに無料開放されたので Claude Code 用スキルと一緒にセットアップした.md`
- `00_Inbox/Clippings/Obsidian × Claude Codeで情報整理を緩くやってみたけど、想像以上によかった話.md`
- `00_Inbox/Clippings/ObsidianからAIエージェントとチャットできるプラグインを作った (Claude Code，Codex，Gemini CLI対応).md`
- `00_Inbox/Clippings/WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata.md`
- `00_Inbox/Clippings/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md`
