---
original_source: 00_Inbox/Clippings/🔥 はじめての Agent Skills 🔥 12 選＆リポジトリ一覧！GitHub Copilot でも使える AI の手順書.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, git, 2026-04]
---

---
title: "🔥 はじめての Agent Skills 🔥 12 選＆リポジトリ一覧！GitHub Copilot でも使える AI の手順書"
source: "https://qiita.com/aktsmm/items/08eef2cdeeb0a32b69a2"
author:
  - "[[aktsmm]]"
published: 2025-12-24
created: 2026-04-19
description: "この記事は GitHub Dockyard Advent Calendar 2025🎄 の 25 日目の記事 です。 メリークリスマス 🎄！！ こんにちは、AI エージェントの進化にワクワクが止まらないアーキテクトのやまぱんです。 補足コメントや質問、いいね、拡散、ぜひお..."
tags:
  - "clippings"
---
### Agent Skills の要約
Agent Skills は、AI エージェントに専門知識や特定のワークフローをパッケージ化して教えるためのオープンスタンダードです。

### 主なポイント
- **Skills の役割**: Tool（できること）と Instructions（ルール）を補完し、「特定のタスクをどう実行するか」という手順を標準フォーマット（SKILL.md, scripts, resources）でパッケージ化します。
- **仕組み**: 「必要な時だけ必要な知識を読み込む（Progressive Disclosure）」ことで、コンテキストウィンドウを効率的に使用します。
- **互換性**: Anthropic 公式規格であり、Claude だけでなく **GitHub Copilot でも利用可能** です。
- **作成方法**: `skill-creator` という専用 Skill を使うと、対話形式で新しい Skill を自動生成できます。
- **セキュリティ**: 野良 Skill には悪意ある挙動のリスクがあるため、公式や信頼できるソースの利用が強く推奨されます。

### エージェントワークフローの使い分け
| 項目 | 役割 |
| :--- | :--- |
| **Tool** | API 接続やファイル操作など、物理的な能力 |
| **Instructions** | コーディング規約や文体など、常に守るべき共通ルール |
| **Skills** | 分岐や手順を含むワークフローなどの専門知識 |

### 導入のメリット
- **標準化**: ツール間での再利用が容易。
- **配布**: フォルダ一つでインストール可能なパッケージ形式。
- **エコシステム**: `awesome-copilot` や `awesome-claude-skills` でコミュニティと共有・貢献が可能。