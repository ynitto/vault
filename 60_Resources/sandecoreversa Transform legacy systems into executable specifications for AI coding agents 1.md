---
title: 'sandeco/reversa: Transform legacy systems into executable specifications for
  AI coding agents'
source: https://github.com/sandeco/reversa
author: null
published: null
created: 2026-05-05
description: Transform legacy systems into executable specifications for AI coding
  agents - sandeco/reversa
tags:
- clippings
- resource/web
- 2026-05
- claude-code
- ai-agent
- copilot
original_source: 00_Inbox/Clippings/sandecoreversa Transform legacy systems into executable
  specifications for AI coding agents 1.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### Reversaの概要
Reversaは、レガシーシステムをAIコーディングエージェントが理解・実行可能な「仕様書（ドキュメント）」へと変換するフレームワークです。既存コードのビジネスルールやアーキテクチャを抽出し、AIによる安全な保守・進化をサポートします。

### 主要な特徴
- **非破壊的な分析:** 既存コードを一切変更・削除せず、`.reversa/`フォルダ等に成果物を出力します。
- **専門エージェント群:** 役割分担されたAI（Scout, Archaeologist, Architect, Writerなど）が協力して分析を実行します。
- **広範な互換性:** Claude Code, Cursor, Windsurf, GitHub Copilotなど、主要なAI開発環境に対応しています。
- **確実性の可視化:** 出力内容を「🟢確認済み」「🟡推論」「🔴要確認」の3段階で分類します。

### 利用のポイント
- **導入:** `npx reversa install` コマンドで簡単に環境構築が可能。
- **実行:** `/reversa` コマンドで対話的な分析プロセスを開始。
- **成果物:** コード分析、データディクショナリ、C4モデル図、API仕様書、ADR（設計判断の記録）など多岐にわたるドキュメントが生成されます。
- **セキュリティ:** APIキーの要求や外部送信を行わず、手元のAIエージェントのコンテキスト内で動作するため安全です。
