---
title: "Claude Code に質の高いPR書かせる Google Engineering Practices 食わせたスキル"
source: "https://izanami.dev/post/e63c7bfd-cc85-4421-a4e7-776e93fb8720"
author:
  - "[[コムテ]]"
published: 2026-05-23
created: 2026-05-31
description: "Google が公開してるGoogle Engineering Practices Documentation は Google 社内のコードレビュー基準を一般公開したドキュメント群。Claude Code のスキルに読ませてPRのクオリティをあげる"
tags:
  - "clippings"
---
### 概要
Google のコードレビュー基準である「Google Engineering Practices」を Claude Code に組み込み、高品質な PR を作成・セルフレビューさせる手法についての解説。

### 要点まとめ
- **スキルの設計:** 内容を要約（distill）すると情報が劣化するため、原文を `references/` に同梱し、必要な時だけ参照させる「薄い手順書 ＋ 厚い辞書」の構造を採用。
- **実装のコツ:** `SKILL.md` にワークフローとセルフレビュー用チェックリストを記載し、判断に迷った時のみ原文の特定ファイルを読ませることでコンテキスト消費を抑える。
- **運用の成果:** 実データの diff を流したところ、AI が空 catch や null チェック漏れを検知し、「直すまで submit 不可」と判断する高度なセルフレビューを実現。
- **汎用性:** レビュー基準を「哲学（非依存）」と「観点（領域固有）」に分解することで、コードレビューだけでなく文章作成時のレビューなど、他の領域へ容易に転用可能。
