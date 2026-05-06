---
title: 既存コードから仕様書を逆生成するClaude Codeスキル cc-rsg を作ってみた
source: https://zenn.dev/daishiro/articles/cc-rsg-reverse-spec-generation
author: null
published: 2026-05-02
created: 2026-05-05
description: null
tags:
- clippings
- resource/web
- 2026-05
- claude-code
- ai-agent
original_source: 00_Inbox/Clippings/既存コードから仕様書を逆生成するClaude Codeスキル cc-rsg を作ってみた.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 概要
レガシーコードから仕様書を逆生成するClaude Code用スキル「cc-rsg」の紹介記事。LLM特有の「嘘の混じったもっともらしい仕様書」を排し、信頼性を担保する仕組みを重視して開発された。

### 要点
* **「美しいフィクション」問題への対策**
  - 推測による補完を避け、「分からない」を明示することに価値を置く設計。
* **5つの原則**
  - 正直さ（未確定事項の可視化）、トレーサビリティ（行番号参照）、抜け漏れ防止（全インベントリ抽出）、段階的詳細化、再開可能性。
* **6フェーズ状態マシン**
  - 状態管理（.cc-rsg/state.json）により、LLMの暴走を防止し、中断・再開を可能にしている。
* **機械的カバレッジ検証**
  - LLMの主観に頼らず、スクリプト（Python AST等）でコードベースの網羅性を物理的に検証。
* **Question Bank（不確実性の管理）**
  - 疑問点を構造化して管理し、回答不能な事実は「未確定事項」として仕様書に記載。
* **主な用途**
  - レガシー保守、オンボーディング、仕様書整備など。
