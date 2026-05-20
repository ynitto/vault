---
title: "たった数行でコード品質がグッと上がる、CLAUDE.md / AGENTS.md にいつも追記してるやつ"
source: "https://zenn.dev/peka2/articles/6dc7d5a87a99dd"
author:
published: 2026-05-14
created: 2026-05-16
description:
tags:
  - "clippings"
---
### 記事の要約
開発の初期段階で『CLAUDE.md』や『AGENTS.md』に適切なルールを定義することで、AI（Claude Code等）の出力品質を大幅に向上させる手法についての解説記事です。

### 要点まとめ

#### AIの品質向上ルール
- **初期設定の重要性**: 最初の一歩でコード品質の99%が決まるため、納得がいかなければ全消ししてやり直すことも厭わない。
- **必須のドキュメント規約**:
  - KISS, DRY, YAGNI原則の遵守。
  - TSDoc（@param, @returns等）の強制。
  - 全ファイルの冒頭に2行程度の役割・責務を記述。
  - コロケーションの重視。
  - ADR（設計決定記録）を`docs/adr`に記録する。
  - デザイントークン（oklch）の活用とLucide-reactの採用。

#### 専門分野別のルール
- **DB利用時**: フルスキャンを防ぐため、EXPLAINを用いたクエリ確認を徹底する。
- **Next.js 16.2以降**: 
  - `<Suspense>`をページ全体にかけない。
  - 最小スコープでコンポーネントを定義する。
  - 学習データの古さを考慮し、「コーディング前に必ず`node_modules/next/dist/docs/`を参照する」ルールを導入する。
