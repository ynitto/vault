---
title: "CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた"
type: "topic"
tags:
  - "claude-code"
  - "aws"
  - "git"
  - "cloudformation"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた.md"
summary: "AWS CloudFormationテンプレートの品質担保に向け、コーディング規約の策定と、それを自動的に守るためのツール環境（rain, cfn-lin…"
---

# CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた

## 概要

AWS CloudFormationテンプレートの品質担保に向け、コーディング規約の策定と、それを自動的に守るためのツール環境（rain, cfn-lint, Claude Code skills）を整備した取り組みの紹介。

*発行: 2026-03-24 / [[claude-code-aws-cloudformation-rain-fmt-15db66]]*

## 主要なトピック

- [[claude-code]]
- [[aws]]
- [[git]]
- [[cloudformation]]

## 詳細

- AWS CloudFormationテンプレートの品質担保に向け、コーディング規約の策定と、それを自動的に守るためのツール環境（rain, cfn-lint, Claude Code skills）を整備した取り組みの紹介。
- 主な要点
- **規約策定の背景**
- 開発速度を落とさず、自然に規約を守れる「開発体験」を重視。
- MUST/SHOULD/MAYでルールレベルを定義し、レビューの判断基準を明確化。
- **導入ツールと役割**
- **rain fmt**: ファイル保存時に自動実行し、セクション順序や記法を自動整形。
- **cfn-lint**: 構文チェックに加え、プロジェクト固有の4つのカスタムルール（W9001〜W9004）で必須項目やハードコードを検知。
- **Claude Code skills (`/cfn-review`)**: ツールで自動判定できない規約（英語のみ、NoEcho設定等）をLLMが補助チェック。

*発行: 2026-03-24 / [[claude-code-aws-cloudformation-rain-fmt-15db66]]*

## 関連テーマ

- [[claude-code]]
- [[aws]]
- [[git]]
- [[cloudformation]]

## 出典

- `60_Resources/CloudFormation コーディング規約を策定し、rain fmt + cfn-lint + Claude Code skillsで担保する仕組みを整備してみた.md`
- https://dev.classmethod.jp/articles/cfn-coding-guidelines/
