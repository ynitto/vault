---
title: "Node.js Docker baseイメージには alpine < distroless < ubuntu+slim 構成がよさそう"
type: "topic"
tags:
  - "testing"
  - "docker"
  - "node-js"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Node.js Docker baseイメージには alpine < distroless < ubuntu+slim 構成がよさそう.md"
summary: "Node.js Dockerイメージ選定のベストプラクティス"
---

# Node.js Docker baseイメージには alpine < distroless < ubuntu+slim 構成がよさそう

## 概要

Node.js Dockerイメージ選定のベストプラクティス

*発行: 2022-06-14 / [[testing-docker-node-js-docker-base-4bb3cc]]*

## 主要なトピック

- [[testing]]
- [[docker]]
- [[node-js]]
- [[performance]]

## 詳細

- Node.jsのDockerベースイメージ選択において、安定性、セキュリティ、運用コストのバランスを考慮した解説記事です。
- 推奨されないイメージ
- **node:alpine**: musl libcによる互換性の問題、パッケージの再現性（pinning）の困難さから非推奨。
- **node:<version> / node:latest**: 不要なパッケージが多く、イメージサイズが大きく脆弱性リスクも高いため非推奨。
- 推奨される選択肢
- 1. **slim系イメージ（手軽）**
- Debianベースの軽量版。手軽に使いたい場合に最適。
- 2. **distrolessイメージ（上級者向け）**
- パッケージマネージャーやShellを排した超軽量イメージ。セキュリティ重視だが、構築の手間とバージョン管理の難易度が高い。

*発行: 2022-06-14 / [[testing-docker-node-js-docker-base-4bb3cc]]*

## 関連テーマ

- [[testing]]
- [[docker]]
- [[node-js]]
- [[performance]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Node.js Docker baseイメージには alpine < distroless < ubuntu+slim 構成がよさそう.md`
- https://zenn.dev/jrsyo/articles/e42de409e62f5d
