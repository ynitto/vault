---
title: "生成AIによるプレゼンテーション作成"
type: concept
tags: [ai, presentation, pptx, productivity]
created: 2026-05-05
updated: 2026-05-06
sources:
  - "../60_Resources/生成AIでパワポを作る方法一覧【2026年3月版】.md"
summary: "生成AIを使ったPPTX作成手法の比較。編集可能性を重視した手法選択の指針。"
---

# 生成AIによるプレゼンテーション作成

## 概要

2026年時点で利用可能な生成AIによるPPTX作成手法を「編集可能性」の観点で整理。単なる生成だけでなく、実務で修正・再利用できる形式を選ぶことが重要。

*発行: 2026-03-14*

## 詳細

### 手法の分類と選び方

| 用途 | 推奨手法 | 特徴 |
|---|---|---|
| とりあえず1回作りたい | Claude.ai PPTX Skill | 編集可能な正規PPTXを直接生成 |
| Markdownで管理したい | Marp + AI | Git連携可能、標準では画像化 |
| 品質管理・Git管理重視 | PptxGenJS / Office PowerPoint MCP | YAMLで一元管理、デザイン定数をコードで制御 |

### 各手法の詳細

- **Claude.ai PPTX Skill**: プログラムコードを活用し編集可能なPPTXを生成。実用性が高い
- **Gamma/Microsoft Copilot/Canva**: GUI完結型。ツールごとにレイアウト崩れの癖がある
- **NotebookLM**: 出力が画像化されるため直接編集不可
- **Marp**: Markdownで記述。編集可能にするには実験的オプションが必要
- **Claude Code + PptxGenJS**: 最も品質管理しやすい。YAMLで内容を一元管理

## 関連

- [[ai-agent]]
- [[claude-code]]

## 出典

- `../60_Resources/生成AIでパワポを作る方法一覧【2026年3月版】.md`
