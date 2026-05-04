---
title: "Stacked Diffs (and why you should know about them)"
source: "https://newsletter.pragmaticengineer.com/p/stacked-diffs"
author:
  - "[[Gergely Orosz]]"
published:
created: 2026-05-01
description: "Meta and Google have been using stacking for closer to a decade: a coding workflow that is very efficient for small PRs. So what is stacking, and how come it’s not more widespread in the industry?"
tags:
  - "clippings"
---
### 記事の要約
この記事は、MetaやGoogleで採用されている効率的なコードレビュー手法「Stacked Diffs（スタックド・ディフ）」について解説しています。これは、大きな機能を小さな依存関係のある複数のプルリクエスト（PR）に分割し、レビュー待ちによる停滞を防ぎながら並行開発を可能にする手法です。

### Stacked Diffsの主なポイント
* **概念**: 1つの大きなPRを「小さなコミット単位（ディフ）」に分割し、それぞれを独立してレビュー・マージ可能にする手法。
* **メリット**:
    * **継続的な開発**: 前のPRがマージされるのを待たずに次の作業を進められる。
    * **コード品質の向上**: 小さな単位でレビューするため、バグの発見やコード理解が容易になる。
    * **生産性**: 「コーディングの勢い（フロー）」を維持しやすく、手待ち時間を最小化できる。
* **運用の課題**: 
    * 依存関係があるため、先行するディフに変更が入ると、後続のディフで「インタラクティブ・リベース」が必要になる。
    * 習熟にはGitの履歴操作（リベース）スキルが求められる。
* **推奨ツール**:
    * [Graphite](https://graphite.dev/)
    * [Gerrit](https://www.gerritcodereview.com/)
    * [Sapling](https://sapling-scm.com/)
    * [ReviewStack](https://reviewstack.dev/)