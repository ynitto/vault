---
title: "Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた"
source: "https://zenn.dev/naomine_egawa/articles/harness-engineering-meetup-and-agent-harness"
author:
published: 2026-04-30
created: 2026-05-05
description:
tags:
  - "clippings"
---
## Harness Engineering：AIエージェントを実戦で動かすための「仕組み」

AIエージェントを長期間かつ無人で安定稼働させるためのインフラ層・パイプラインの設計手法「Harness Engineering」についての考察記事です。

### 要点まとめ

- **Harness Engineeringとは**
  - AIモデル周辺のインフラ（ツール連携、状態管理、障害回復、セキュリティ、可観測性）のこと。モデル単体ではなく「実戦で使えるようにする仕組み」を指す。

- **解決すべき技術的課題**
  - 状態管理と復元（Gitをソースとしたセッション継続）
  - 長時間稼働のためのチェックポイント（WIPコミットなど）
  - エージェントの排他制御・ヘルスチェック
  - エージェント間の通信プロトコル（A2A）やツール接続規格（MCP）の活用

- **標準化への動き**
  - Googleなどのテック企業が、社内ツールをOSS化してデファクト標準化する流れが加速（A2A, ADK, Scionなど）。

- **今学ぶべき重要知識**
  - 特定ツールへの依存を避け、「問題の解決パターン」そのものを理解する。
  - KubernetesやHTTP/JSONベースの通信プロトコルなど、陳腐化しにくい技術基盤に投資する。

- **結論**
  - ハーネスの構築はまだ開拓地であり、事例共有やコミュニティを通じて「手探りの知見」を共有することが重要である。
