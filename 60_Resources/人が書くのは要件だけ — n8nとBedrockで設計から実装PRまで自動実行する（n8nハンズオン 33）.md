---
title: "人が書くのは要件だけ — n8nとBedrockで設計から実装PRまで自動実行する（n8nハンズオン 3/3）"
source: "https://zenn.dev/okamyuji/articles/n8n-bedrock-prd-implementation-agent"
author:
published: 2026-05-09
created: 2026-05-16
description:
tags:
  - "clippings"
---
## 概要
n8n、Gemini、Amazon Bedrock（Claude 3.5 Sonnet）を組み合わせ、要件定義からPR作成、コード実装までを自動化するパイプラインの構築手順を解説した記事です。

## 主要なポイント
- **自動化パイプラインの構築**
  - フォーム入力により、PRD（製品要求仕様書）とDesign Docを自動生成。
  - リポジトリのブランチ作成、設計書のコミット、PR作成、実装のコミット、PRへの要約投稿を一気通貫で実行。
- **役割の分離と最適化**
  - 設計フェーズ：Geminiを使用（構造化データの生成に強み）。
  - 実装フェーズ：BedrockのClaude 3.5 Sonnetを使用（コード生成とAWS環境内での処理に最適）。
- **セキュリティと安全性の担保**
  - **二重防御**: Gemini/Bedrockの出力をバリデーションし、不正なコードや秘匿情報の流出を防ぐ。
  - **フォーム保護**: Shared Secretによる認証を実装し、第三者による不正実行を防止。
  - **人間レビューの必須化**: GitHubのBranch ProtectionとCODEOWNERSを設定し、AI生成PRへの人間による承認を機械的に強制。
- **運用上のノウハウ**
  - Markdownの書式を維持したGoogle Doc作成には、HTML変換を経由したmultipart/related POSTが有効。
  - LambdaやBedrockのIAM権限設定におけるリソースARN指定の注意点（完全一致の重要性）。
