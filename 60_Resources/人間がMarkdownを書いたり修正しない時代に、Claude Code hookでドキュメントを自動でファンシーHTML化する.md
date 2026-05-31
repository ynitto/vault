---
title: "人間がMarkdownを書いたり修正しない時代に、Claude Code hookでドキュメントを自動でファンシーHTML化する"
source: "https://zenn.dev/uehaj/articles/claude-code-fancy-html-hook"
author:
published: 2026-05-10
created: 2026-05-16
description:
tags:
  - "clippings"
---
### 要約
本記事は、人間がMarkdownを修正・作成しないAI駆動開発の時代において、Claude Codeのフック機能を活用し、AIが生成したMarkdownから「人間がレビューしやすいリッチなHTML」を自動生成・ブラウザ表示させる仕組みの提案です。

### 要点
* **レビューの効率化**
    * AIが生成するMarkdownは機械的で人間には読みづらい場合があるため、視認性の高いインフォグラフィック風HTMLに変換することでレビューの質と速度を向上させる。
* **Claude Codeのフック（PostToolUse）活用**
    * `.md`が書き出された際に自動でシェルスクリプトを起動し、Pythonで簡易HTMLを作成後、さらにClaude Codeのヘッドレスモード（`claude -p`）でリッチなHTMLを生成する。
* **自動化とUX**
    * 生成したHTMLは確認ダイアログ（macOS）を経て自動的にブラウザで開くため、ファイル名を探して開く手間を排除する。
* **役割分担の明確化**
    * 「書く・修正する（AI）」と「読む・レビューする（人間）」という役割分担に基づき、ソースとしてのMarkdownとビューとしてのHTMLを使い分ける。
* **運用のポイント**
    * 生成処理はバックグラウンド（`&`）で行い、メインプロセスの作業を妨げない設計にする。
    * 不要な発火を防ぐための除外リスト設定や、APIコストを考慮したオプトイン形式のダイアログ導入が推奨される。
