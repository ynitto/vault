---
original_source: 00_Inbox/Clippings/Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, design, 2026-04]
---

---
title: "Claude CodeのSkillsでハーネスエンジニアリングを実装した — ルール自動生成でコード品質を継続改善する"
source: "https://zenn.dev/shintaroamaike/articles/df3ecc0ddee047"
author:
published: 2026-04-01
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
Claude Codeのコーディングルール管理を自動化するスキル「AutoHarness」の紹介記事です。プロジェクト固有の規約を自動生成・適用することで、AIによるコード品質の継続的な改善を実現します。

### 要点
- **AutoHarnessとは**
  - DeepMindの論文の着想を得た、プロジェクト固有のルール（型定義、命名規則、禁止パターン）を管理するフレームワーク。
  - 開発現場の「暗黙知」を文章化し、Claude Codeへ適切に指示するコストを削減します。

- **主な機能**
  - `/autoharness-init`: プロジェクトを解析し、ルールファイル（`.claude/rules/harness.md`）と検証スクリプトを自動生成。
  - `/autoharness-update`: コード生成後のフィードバックやエラーに基づき、ルールを自律的に改善。

- **メリット**
  - ルールの一元管理により、プロンプトへの記述コストを削減。
  - チーム固有のコーディング規約の蓄積が可能。
  - CI環境等での自動検証への展開が可能。

- **評価結果（n=5の小規模試験）**
  - 指示書にルールを明記しなくても、ハーネスの導入により `pathlib` や `Decimal` の使用率が大幅に向上しました。
  - 一方、バグ修正の正確性など、ロジック自体の要件達成にはハーネスの有無による大きな差は見られませんでした。