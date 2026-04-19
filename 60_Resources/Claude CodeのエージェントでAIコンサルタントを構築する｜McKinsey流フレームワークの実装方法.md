---
title: Claude CodeのエージェントでAIコンサルタントを構築する｜McKinsey流フレームワークの実装方法
source: https://qiita.com/rcomcpgm-cyber/items/901344b211a6a3e7dda7
author:
- '[[rcomcpgm-cyber]]'
published: 2026-04-10
created: 2026-04-19
description: この記事でわかること Claude Codeの「エージェント機能」を使った専門家エージェントの構築方法 McKinsey/BCG流分析フレームワーク（空雨傘）をAIに組み込む手順
  実際のSaaS事業分析の事例と精度評価 AIコンサルタントが活躍する場面と限界 Cl...
tags:
- resource/web
- ai-agent
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/Claude CodeのエージェントでAIコンサルタントを構築する｜McKinsey流フレームワークの実装方法.md
copied_at: 2026-04-19 10:51:13+09:00
---
### 概要
Claude Codeのエージェント機能を活用し、McKinsey/BCG流の思考フレームワーク（空・雨・傘）を組み込んだ「AIコンサルタント」の構築・運用方法を解説する記事です。

### 要点
- **エージェント機能の活用**: `.claude/agents/` 配下に定義ファイルを配置することで、役割特化型のAIを構築可能。
- **コンサルタントの構築**: 
  - 「イシュー・ドリブン」「仮説志向」「パレートの法則」を核としたマインドセットを定義。
  - 「空（事実）・雨（解釈）・傘（行動）」というフレームワークで出力形式を標準化。
- **実装のポイント**:
  - 適切なツール（Read/WebSearch等）を制限し、思考と分析に特化させる。
  - AI特有の曖昧な回答を避けるため「両案とも有効」といった表現を禁止し、明確な推奨を促す。
- **実運用**: SaaS事業分析において、コードベースの直読により現状の課題を特定し、論理的なロードマップを策定することに成功。