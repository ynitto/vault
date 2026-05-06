---
title: "Stacked Diffs (and why you should know about them)"
type: "topic"
tags:
  - "cloudformation"
  - "code-review"
  - "networking"
  - "gergely-orosz"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../../60_Resources/Stacked Diffs (and why you should know about them).md"
summary: "この記事は、MetaやGoogleで採用されている効率的なコードレビュー手法「Stacked Diffs（スタックド・ディフ）」について解説しています。こ…"
---

# Stacked Diffs (and why you should know about them)

## 概要

この記事は、MetaやGoogleで採用されている効率的なコードレビュー手法「Stacked Diffs（スタックド・ディフ）」について解説しています。これは、大きな機能を小さな依存関係のある複数のプルリクエスト（PR）に分割し、レビュー待ちによる停滞を防ぎながら並行開発を可能にする手法です。

## 主要なトピック

- [[cloudformation]]
- [[code-review]]
- [[networking]]
- [[gergely-orosz]]

## 詳細

- この記事は、MetaやGoogleで採用されている効率的なコードレビュー手法「Stacked Diffs（スタックド・ディフ）」について解説しています。これは、大きな機能を小さな依存関係のある複数のプルリクエスト（PR）に分割し、レビュー待ちによる停滞を防ぎながら並行開発を可能にする手法です。
- Stacked Diffsの主なポイント
- **概念**: 1つの大きなPRを「小さなコミット単位（ディフ）」に分割し、それぞれを独立してレビュー・マージ可能にする手法。
- **メリット**:
- **継続的な開発**: 前のPRがマージされるのを待たずに次の作業を進められる。
- **コード品質の向上**: 小さな単位でレビューするため、バグの発見やコード理解が容易になる。
- **生産性**: 「コーディングの勢い（フロー）」を維持しやすく、手待ち時間を最小化できる。
- **運用の課題**:
- 依存関係があるため、先行するディフに変更が入ると、後続のディフで「インタラクティブ・リベース」が必要になる。

## 関連テーマ

- [[cloudformation]]
- [[code-review]]
- [[networking]]
- [[gergely-orosz]]

## 出典

- `../../60_Resources/Stacked Diffs (and why you should know about them).md`
- https://newsletter.pragmaticengineer.com/p/stacked-diffs
