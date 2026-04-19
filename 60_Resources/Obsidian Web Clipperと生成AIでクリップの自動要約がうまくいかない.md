---
original_source: 00_Inbox/Clippings/Obsidian Web Clipperと生成AIでクリップの自動要約がうまくいかない.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, obsidian, 2026-04]
---

---
title: "Obsidian Web Clipperと生成AIでクリップの自動要約がうまくいかない"
source: "https://zenn.dev/2rezure/articles/e662f43ad9ea35"
author:
published: 2025-03-13
created: 2026-04-19
description:
tags:
  - "clippings"
---
### Obsidian Web ClipperでのAI要約問題解決
Obsidian Web ClipperでGeminiやGPT-4oがWebページをうまく要約しない、またはコンテキストが渡されない問題の解決策。

#### 問題点
*   AI要約時にWebページの`content`や`fullHtml`がAIに正しく渡されていない。

#### 解決策
*   **テンプレート側で「インタープリターコンテキスト」を明示的に設定する。**
    *   詳細設定だけでなく、実際に使用するテンプレートのJSON設定にも`\\"context\\": \\"{{fullHtml}}\\"`を含める。
    *   要約指示:`\\"noteContentFormat\\": \\"{{\\"内容を要約してください。。\