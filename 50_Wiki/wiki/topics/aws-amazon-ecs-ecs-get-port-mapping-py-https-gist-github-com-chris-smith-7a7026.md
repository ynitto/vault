---
title: "ecs-get-port-mapping.py"
type: "topic"
tags:
  - "aws"
  - "amazon-ecs"
  - "git"
  - "docker"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/ecs-get-port-mapping.py.md"
summary: "このページは、ECS（Amazon Elastic Container Service）環境において、実行中のコンテナから動的なホストポートマッピングを取…"
---

# ecs-get-port-mapping.py

## 概要

このページは、ECS（Amazon Elastic Container Service）環境において、実行中のコンテナから動的なホストポートマッピングを取得するためのPythonスクリプトと、その実行用シェルスクリプトを共有したGitHub Gistです。

## 主要なトピック

- [[aws]]
- [[amazon-ecs]]
- [[git]]
- [[docker]]

## 詳細

- このページは、ECS（Amazon Elastic Container Service）環境において、実行中のコンテナから動的なホストポートマッピングを取得するためのPythonスクリプトと、その実行用シェルスクリプトを共有したGitHub Gistです。
- 要点
- **目的**: Dockerコンテナ内で実行されているアプリケーションから、ホスト側の動的なポートを環境変数として取得する。
- **主な機能**:
- `ecs-get-port-mapping.py`: ECSのイントロスペクションAPIを利用してコンテナ情報とタスクARNを特定し、Boto3でECSから正確なポートマッピング情報を取得・エクスポートする。
- `entry_point.sh`: コンテナ起動時に上記のPythonスクリプトを呼び出し、取得したポートマッピングを環境変数としてシェルに展開する。
- **ライセンス**: 作者により「Apache License 2.0」での利用が許諾されている。
- **用途例**: Selenium Gridなどの、ホストポート情報が必要な分散システム構築時に有用。

## 関連テーマ

- [[aws]]
- [[amazon-ecs]]
- [[git]]
- [[docker]]

## 出典

- `../60_Resources/ecs-get-port-mapping.py.md`
- https://gist../.github.com/chris-smith-zocdoc/126db78651046c67ac66dbd87393b1dc
