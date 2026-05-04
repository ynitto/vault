---
title: "Node.js Docker baseイメージには alpine < distroless < ubuntu+slim 構成がよさそう"
source: "https://zenn.dev/jrsyo/articles/e42de409e62f5d"
author:
published: 2022-06-14
created: 2026-05-01
description:
tags:
  - "clippings"
---
### Node.js Dockerイメージ選定のベストプラクティス

Node.jsのDockerベースイメージ選択において、安定性、セキュリティ、運用コストのバランスを考慮した解説記事です。

#### 推奨されないイメージ
- **node:alpine**: musl libcによる互換性の問題、パッケージの再現性（pinning）の困難さから非推奨。
- **node:<version> / node:latest**: 不要なパッケージが多く、イメージサイズが大きく脆弱性リスクも高いため非推奨。

#### 推奨される選択肢
1. **slim系イメージ（手軽）**
   - Debianベースの軽量版。手軽に使いたい場合に最適。
2. **distrolessイメージ（上級者向け）**
   - パッケージマネージャーやShellを排した超軽量イメージ。セキュリティ重視だが、構築の手間とバージョン管理の難易度が高い。
3. **Ubuntu + slimのハイブリッド構成（バランス◎）**
   - Multi-stageビルドを活用。slim系からNode.jsバイナリのみを抽出し、Ubuntuをベースにする手法。高いセキュリティと柔軟な運用の両立が可能。

#### Docker運用の重要ポイント
- **Multi-stageビルド**: 環境ごとの最適化に必須。
- **セキュリティ**: rootユーザーの利用を避け、実行ユーザーを分離する。
- **プロセス管理**: `tini`を導入してPID 1問題を回避。
- **ビルド高速化**: `--mount=type=cache`の活用でキャッシュを効率化。