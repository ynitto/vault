---
title: GitHub Copilot でサブエージェントからサブエージェントを呼び出して TDD（テスト駆動開発）ワークフローを作成
source: https://qiita.com/leomarokun/items/3040cd6ae4c51b2329f6
author:
- '[[leomarokun]]'
published: 2026-04-03
created: 2026-04-19
description: はじめに 2026年3月リリースの VS Code 1.113 で Nested Subagents - サブエージェントが別のサブエージェントを呼び出せるようになった機能です。
  この記事では、Nested Subagents の仕組みと、実際に動かして検証した結果をお伝...
tags:
- resource/web
- ai-agent
- git
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/GitHub Copilot でサブエージェントからサブエージェントを呼び出して TDD（テスト駆動開発）ワークフローを作成.md
copied_at: 2026-04-19 10:51:13+09:00
---
### 概要
2026年3月にリリースされたVS Code v1.113の新機能「Nested Subagents（サブエージェントの入れ子呼び出し）」を活用し、TDD（テスト駆動開発）の自動化ワークフローを構築する手法の解説です。

### 要点
- **Nested Subagentsとは**
  - サブエージェントが別のサブエージェントを直接呼び出せる機能。
  - 従来は無限再帰防止のため禁止されていたが、設定により可能になった。

- **サブエージェントの主な特徴**
  - **コンテキスト分離**: メインの会話履歴を汚さず独立して動作。
  - **同期実行**: メインエージェントは結果を待ってから次へ進む。
  - **効率性**: 途中経過ではなく結果の要約のみを返すためトークンを節約可能。

- **TDDワークフローの構成**
  - Red（失敗テスト作成）、Green（最小実装）、Refactor（品質改善）の3つのフェーズを専門エージェントに役割分担。
  - `agent-customization`コマンドで各エージェントを自動生成可能。

- **運用上の対策と注意点**
  - **無限再帰**: `agents`プロパティで呼び出し先を制限する。
  - **コンテキスト断絶**: 必要情報をプロンプトに含める。
  - **トークン消費**: 階層は2階層程度に留め、軽量モデルを併用する。
  - **権限管理**: `user-invocable`と`disable-model-invocation`を使い分け、ユーザー用と内部用を明確にする。