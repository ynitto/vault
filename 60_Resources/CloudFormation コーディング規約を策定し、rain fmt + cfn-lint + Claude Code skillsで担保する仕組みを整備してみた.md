---
original_source: 00_Inbox/Clippings/CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, 2026-04]
---

---
title: "CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた"
source: "https://dev.classmethod.jp/articles/cfn-coding-guidelines/"
author:
  - "[[桑野翔]]"
published: 2026-03-24
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
AWS CloudFormationテンプレートの品質担保に向け、コーディング規約の策定と、それを自動的に守るためのツール環境（rain, cfn-lint, Claude Code skills）を整備した取り組みの紹介。

### 主な要点
*   **規約策定の背景**
    *   開発速度を落とさず、自然に規約を守れる「開発体験」を重視。
    *   MUST/SHOULD/MAYでルールレベルを定義し、レビューの判断基準を明確化。
*   **導入ツールと役割**
    *   **rain fmt**: ファイル保存時に自動実行し、セクション順序や記法を自動整形。
    *   **cfn-lint**: 構文チェックに加え、プロジェクト固有の4つのカスタムルール（W9001〜W9004）で必須項目やハードコードを検知。
    *   **Claude Code skills (`/cfn-review`)**: ツールで自動判定できない規約（英語のみ、NoEcho設定等）をLLMが補助チェック。
*   **品質担保の仕組み**
    *   ツール（自動担保）とレビュー（人手）の役割を明確に分担。
    *   Claude Codeがサマリを出力することで、レビュアーと開発者の双方の負担を軽減。
*   **継続的改善**
    *   GitHub Issueでの報告フローを整備し、チームでルールとツールを育てていく文化を醸成。