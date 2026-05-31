---
title: "日々の開発で使っているClaude Code Skills"
source: "https://zenn.dev/remitaid/articles/4f9dc787b6c191"
author:
published: 2026-05-22
created: 2026-05-31
description:
tags:
  - "clippings"
---
### Claude Codeを活用した開発効率化の要約
本記事は、エンジニアがClaude Codeの「Skills」機能を活用して、計画から実装までを効率的に自走させる手法を解説しています。

#### 重要なポイント
- **リサーチと計画の重要性**
  - 単にAIにコードを書かせるのではなく、リサーチと計画（`plan.md`）の質を高めることがクオリティ向上に直結する。
  - 「実装は退屈な作業であるべき」という思想のもと、創造的な作業は人間によるプランの策定や修正に集中させる。

- **活用している主要なSkills**
  - **brainstorming**: 計画の立案とドキュメント化。
  - **subagent-driven-development / executing-plans**: プランに基づく実装の自動実行。
  - **dig / decomposition**: 要件の明確化とタスクの細分化により、長時間（30分程度）の自走を実現。
  - **drawio**: アーキテクチャ図の生成と管理。

- **自作Skillsによるワークフロー最適化**
  - **feature-dev**: リサーチ→計画→実装の3段階フェーズで構成。人間がインラインで注釈（NOTE/REJECT/QUESTION）を入れ、計画を洗練させるサイクルを重視。
  - **codex**: 実装後のコードレビューに使用。
  - **commit-message**: コミットメッセージの生成やfixupの検討を支援。

- **運用上の工夫**
  - プラン専用のディレクトリを作成し、`k1LoW/mo`などを用いて可視化することで、AIの生成物を効率的に管理している。
