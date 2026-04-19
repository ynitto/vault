---
title: "Design Docの書き方ガイド"
source: "https://zenn.dev/baleenstudio/articles/120c007876d39d"
author:
published: 2025-07-29
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 要約
この記事は、チームやAIを活用した開発において重要となる「Design Doc（設計書）」の効果的な書き方を解説したガイドです。個人開発での経験から、文脈（コンテキスト）を言語化し、Googleが提唱するテンプレートをベースにした設計ドキュメントの作成を推奨しています。

### 要点
- **なぜDesign Docが必要か**
  - コードだけでは伝わらない「なぜその実装にしたのか」という文脈をチームやAIと共有するため。
- **構成案（テンプレート）**
  - **Context & Scope**: 背景と対象範囲の明確化。
  - **Goals & Non-goals**: 何を目指し、何を対象外とするか（誤解を防ぐ）。
  - **The Actual Design**: 
    - システム構成図、API設計、データ保存先、擬似コードなどを記載。
    - 制約条件の整理。
  - **Alternatives Considered**: 検討した代替案とその採用理由の記録。
  - **Cross-cutting Concerns**: セキュリティなど横断的な関心事項。
  - **Reference & Changelog**: 参照元や変更履歴の記録。
- **運用のコツ**
  - メンテナンス負荷を減らすため、ドキュメントのスコープを小さく保つ。
  - AIを活用して変更履歴（Changelog）などを自動生成・更新する。