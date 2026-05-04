---
title: "ARM系マシンでx86系のDockerイメージを作成する方法"
source: "https://qiita.com/sakai00kou/items/b83994c97d8d970a7d5b"
author:
  - "[[toyoyuto618]]"
published: 2022-11-13
created: 2026-05-01
description: "はじめに 先日AWS公式ハンズオンとなる「AWS ハンズオン資料」の「Amazon Elastic Container Service 入門 コンテナイメージを作って動かしてみよう」を試そうとした際、エラーでECSのサービスがデプロイできない問題が発生したため、記事に残し..."
tags:
  - "clippings"
---
### 記事の要約
ARMアーキテクチャ（Apple M2 Macなど）環境でDockerイメージをビルドした際、x86系環境（AWS ECSなど）にデプロイすると発生する「アーキテクチャ不一致」によるエラーの対処法についての解説記事です。

### 要点まとめ
- **原因**: 開発環境（ARM）と実行環境（x86）のCPUアーキテクチャが異なるために発生する互換性エラー。
- **解決策**: ビルド時に `--platform` オプションを使用して、明示的にターゲット環境（linux/amd64）を指定する。
  - **コマンド実行時**: `docker build --platform linux/amd64 -t [タグ名] .`
  - **Dockerfile**: `FROM --platform=linux/amd64 [ベースイメージ]`
  - **docker-compose.yml**: `platform: linux/amd64` を指定。
- **補足**: Docker Desktopに含まれるQEMUエミュレーション機能を利用することで、異種アーキテクチャ向けのイメージ作成が可能。
