---
title: "Socket.ioコンテナオーケストレーションハンズオン"
source: "https://zenn.dev/micin/articles/2023-12-04_rikson_socketio-container-orchestration"
author:
published: 2023-12-04
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 記事の要約
Socket.ioを用いたリアルタイム通信アプリケーションをKubernetes環境でスケールさせ、ステートを維持したままダウンタイムなしでデプロイする方法を解説したハンズオン記事です。

### 要点まとめ
- **技術スタック**
  - Socket.io (v4.7.2): 再接続制御やWebTransport対応が強み。
  - Kubernetes & Helm: ローカル環境でのオーケストレーションと構成管理に使用。
  - Redis Streams Adapter: 複数Pod間のメッセージ同期とステート復旧（Connection State Recovery）に必須。

- **スケーリングの課題と対策**
  - 単一サーバーではスケールできないため、Redis Adapterを導入して複数Pod間でのイベントブロードキャストを実現。

- **ダウンタイムなしのデプロイ（ロールアウト）**
  - **Graceful Shutdown**: `SIGTERM` を捕捉し `io.close()` を実行して接続を安全に終了させる。
  - **PID1問題の回避**: `tini` を使用してシグナルが適切にアプリケーションへ伝播するように設定。
  - **Connection State Recovery**: 再接続時のステート保持設定により、デプロイ中のセッション断絶をカバー。
