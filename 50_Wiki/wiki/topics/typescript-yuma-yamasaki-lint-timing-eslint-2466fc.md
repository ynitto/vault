---
title: "重い lint ルールを特定しよう！TIMING オプションで ESLint 実行速度改善"
type: "topic"
tags:
  - "typescript"
  - "yuma-yamasaki"
  - "2023-web-abema"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/重い lint ルールを特定しよう！TIMING オプションで ESLint 実行速度改善.md"
summary: "CI環境で発生していたESLintの実行不安定問題（失敗率50%超）を、TIMINGオプションによるボトルネック分析とルールの最適化で解消した事例。"
---

# 重い lint ルールを特定しよう！TIMING オプションで ESLint 実行速度改善

## 概要

CI環境で発生していたESLintの実行不安定問題（失敗率50%超）を、TIMINGオプションによるボトルネック分析とルールの最適化で解消した事例。

*発行: 2024-10-09 / [[typescript-yuma-yamasaki-lint-timing-eslint-2466fc]]*

## 主要なトピック

- [[typescript]]
- [[yuma-yamasaki]]
- [[2023-web-abema]]

## 詳細

- CI環境で発生していたESLintの実行不安定問題（失敗率50%超）を、TIMINGオプションによるボトルネック分析とルールの最適化で解消した事例。
- 実施した主な対策
- **ボトルネックの特定**: `TIMING=1` オプションを実行し、各ルールの処理時間を可視化。
- **冗長ルールの精査**: TypeScriptと重複する `import/namespace` などのルールを特定。
- **不要なルールの無効化**: TypeScriptが本来行うチェックと重複しているプラグイン設定を無効化。
- 成果
- **安定性の向上**: CIの失敗率が50%超から10%前後へ改善。
- **コスト削減**: ジョブの失敗減少により、CI実行にかかるインフラ費用（クレジット）を大幅に削減。
- **開発効率の向上**: 開発者の手戻りや待ち時間が減り、開発体験が改善。

*発行: 2024-10-09 / [[typescript-yuma-yamasaki-lint-timing-eslint-2466fc]]*

## 関連テーマ

- [[typescript]]
- [[yuma-yamasaki]]
- [[2023-web-abema]]

## 出典

- `60_Resources/重い lint ルールを特定しよう！TIMING オプションで ESLint 実行速度改善.md`
- https://developers.cyberagent.co.jp/blog/archives/50143/
