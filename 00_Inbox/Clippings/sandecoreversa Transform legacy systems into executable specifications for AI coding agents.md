---
title: "sandeco/reversa: Transform legacy systems into executable specifications for AI coding agents"
source: "https://github.com/sandeco/reversa"
author:
published:
created: 2026-05-05
description: "Transform legacy systems into executable specifications for AI coding agents - sandeco/reversa"
tags:
  - "clippings"
---
### Reversa: レガシーコードをAI用仕様書へ変換するフレームワーク

Reversaは、レガシーシステムをAIエージェントが理解・操作可能な「実行可能な仕様書」へと変換するリバースエンジニアリングフレームワークです。

#### 主な特徴とメリット
*   **コードの非破壊性**: 元のプロジェクトファイルを一切変更・削除せず、`.reversa/`フォルダのみに成果物を出力します。
*   **AIエージェントとの統合**: Claude Code, Cursor, Windsurfなど主要なAI環境に対応し、自動化された分析プロセスを提供します。
*   **構造的な分析**: 5段階のパイプライン（偵察、発掘、解釈、生成、レビュー）を通じて、ビジネスルールやアーキテクチャを体系的に抽出します。
*   **トレーサビリティ**: 抽出した仕様はコードとの対応関係が明確で、安全なシステム改修が可能です。

#### 活用できる成果物
*   **技術ドキュメント**: C4図、ERD、データ辞書、API定義（OpenAPI）。
*   **運用ドキュメント**: 状態遷移図、権限行列、ビジネスルールの用語集。
*   **信頼性指標**: 抽出した情報に対し「確認済み(緑)」「推論(黄)」「未確定(赤)」の3段階で信頼性を付与。

#### 利用方法
1.  **インストール**: `npx reversa install` をプロジェクトルートで実行。
2.  **起動**: `/reversa` コマンドで分析を開始。
3.  **運用**: 進捗は `state.json` に保存され、いつでも再開可能。

※利用前にGit等でのバックアップを強く推奨します。
