---
title: "Skillsで実現する軽量パーソナルRAG"
source: "https://zenn.dev/karaage0703/articles/d7eaf62437185d"
author:
published: 2026-03-01
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 軽量パーソナルRAG「workspace-rag」の概要
PostgreSQLやDockerを必要とせず、SQLiteと`uv`のみで構築可能な軽量RAGシステムの実装解説記事です。

### 要点まとめ
- **技術スタックの簡素化**
  - DBにSQLite、埋め込みモデルに`multilingual-e5-small`を採用し、環境構築のハードルを大幅に下げました。
- **Skillsの活用**
  - AIエージェントの「Skills」規格を利用し、必要な時にコマンドとして呼び出す形式を採用。MCPサーバーのような常駐プロセスの手間を削減しました。
- **検索の精度・利便性向上**
  - **関連度スコアの付与:** 検索結果にスコア（高・中・低）を表示し、AIエージェントが情報の重要度を判断しやすくしました。
  - **常駐サーバーモード:** 初回起動時のモデルロード時間を回避するため、HTTPサーバー化により検索速度を約0.1秒まで高速化可能です。
- **AIアシスタント連携**
  - Claude Code等のAIエージェントに自律的なワークスペース検索をさせることで、効率的な情報活用を実現しています。