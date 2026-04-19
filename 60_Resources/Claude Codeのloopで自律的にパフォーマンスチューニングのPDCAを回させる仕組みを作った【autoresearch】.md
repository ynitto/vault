---
original_source: 00_Inbox/Clippings/Claude Codeのloopで自律的にパフォーマンスチューニングのPDCAを回させる仕組みを作った【autoresearch】.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, 2026-04]
---

---
title: "Claude Codeの/loopで自律的にパフォーマンスチューニングのPDCAを回させる仕組みを作った【autoresearch】"
source: "https://zenn.dev/dely_jp/articles/3117e590465e38"
author:
published: 2026-03-30
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
Andre Karpathy氏が公開したAI自律改善リポジトリ「autoresearch」の概念を応用し、RailsコントローラーのパフォーマンスチューニングをAIが自律的に行う仕組み「autoresearch-controller」を構築した事例紹介記事です。

### 要点
- **自律的PDCAサイクルの構築**: Claude Codeの機能（スキル・サブエージェント・hooks）を活用し、「コード変更 → ベンチマーク → 結果判定 → 記録」を10分間隔のループで自動化。
- **防御機構（ハーネスエンジニアリング）の実装**: AIの暴走を防ぐため、以下の防御層を導入。
    - **テストデータの隔離**: チューニング担当エージェントにベンチマーク用データへのアクセス権を与えず、専用サブエージェントで分離。
    - **Bashコマンドのホワイトリスト制御**: 許可されたコマンド以外を一切禁止。
    - **ブランチ保護**: 指定のブランチ以外での実行を遮断。
- **再帰的改善**: 試行履歴（`tuning_results.tsv`）をAIが参照することで、過去の成功・失敗から学習し、改善精度を向上させる構造を実現。
- **エンジニアの役割の変化**: コードを直接書く作業から、AIの行動原理や制限（ハーネス）を設計するエンジニアリングへとシフトすることを提唱。