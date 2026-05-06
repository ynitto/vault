---
title: "ARM系マシンでx86系のDockerイメージを作成する方法"
type: "topic"
tags:
  - "aws"
  - "docker"
  - "toyoyuto618"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/ARM系マシンでx86系のDockerイメージを作成する方法.md"
summary: "ARMアーキテクチャ（Apple M2 Macなど）環境でDockerイメージをビルドした際、x86系環境（AWS ECSなど）にデプロイすると発生する「…"
---

# ARM系マシンでx86系のDockerイメージを作成する方法

## 概要

ARMアーキテクチャ（Apple M2 Macなど）環境でDockerイメージをビルドした際、x86系環境（AWS ECSなど）にデプロイすると発生する「アーキテクチャ不一致」によるエラーの対処法についての解説記事です。

*発行: 2022-11-13 / [[aws-docker-arm-x86-docker-ec78ee]]*

## 主要なトピック

- [[aws]]
- [[docker]]
- [[toyoyuto618]]

## 詳細

- ARMアーキテクチャ（Apple M2 Macなど）環境でDockerイメージをビルドした際、x86系環境（AWS ECSなど）にデプロイすると発生する「アーキテクチャ不一致」によるエラーの対処法についての解説記事です。
- 要点まとめ
- **原因**: 開発環境（ARM）と実行環境（x86）のCPUアーキテクチャが異なるために発生する互換性エラー。
- **解決策**: ビルド時に `--platform` オプションを使用して、明示的にターゲット環境（linux/amd64）を指定する。
- **コマンド実行時**: `docker build --platform linux/amd64 -t [タグ名] .`
- **Dockerfile**: `FROM --platform=linux/amd64 [ベースイメージ]`
- **docker-compose.yml**: `platform: linux/amd64` を指定。
- **補足**: Docker Desktopに含まれるQEMUエミュレーション機能を利用することで、異種アーキテクチャ向けのイメージ作成が可能。

*発行: 2022-11-13 / [[aws-docker-arm-x86-docker-ec78ee]]*

## 関連テーマ

- [[aws]]
- [[docker]]
- [[toyoyuto618]]

## 出典

- `60_Resources/ARM系マシンでx86系のDockerイメージを作成する方法.md`
- https://qiita.com/sakai00kou/items/b83994c97d8d970a7d5b
