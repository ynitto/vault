---
original_source: 00_Inbox/Clippings/Obsidian Web Clipper × AI でWebページを自動要約＆ストックしてみた.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, obsidian, 2026-04]
---

---
title: "Obsidian Web Clipper × AI でWebページを自動要約＆ストックしてみた"
source: "https://dev.classmethod.jp/articles/try-obsidian-web-clipper-ai-summary/"
author:
  - "[[toyoshima-masaya]]"
published: 2025-03-05
created: 2026-04-19
description:
tags:
  - "clippings"
---
## Obsidian Web ClipperでWebページをAI要約する設定方法

### 概要
Obsidian Web Clipperのブラウザ拡張機能とAIインタープリター（Google Gemini等）を連携させ、Webページを自動で要約・整理する方法を紹介します。

### 設定手順

#### 1. インタープリターの設定
- **プロバイダー指定**: Obsidian Web Clipperの設定画面で、Google Gemini, DeepSeek, OpenAIなどのAIプロバイダーを選択し、APIキーを入力します。
- **モデル選択**: 要約に使用するAIモデルを選択します（例: Gemini 2.0 Flash）。
- **詳細設定**: `{{fullHtml}}`に設定します。

#### 2. テンプレートの設定
- ノートの保存先ディレクトリを指定します。
- ノートの内容として、以下の要約プロンプトを設定します。
  > 「内容を簡潔に要約してください。また要点ごとにマークダウン形式で簡潔にまとめてください。その際、箇条書きや見出しを活用し重要なポイントが一目で分かるようにしてください。」

### Webページ要約の実行と結果
- 拡張機能を開くと自動で要約が開始し、数秒で完了します。
- 要約内容は、指定したプロンプトに基づき、簡潔かつマークダウン形式で分かりやすくまとめられます。
- 元記事へのリンクも保存されるため、必要に応じて参照できます。

### まとめ
この方法により、気になる記事を効率的に要約・保存し、Obsidian内で整理することが可能になります。
