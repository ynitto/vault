---
title: "Approximate data structures"
type: topic
tags:
  - "statistics"
  - "performance"
  - "algorithm"
  - "resource-ingest"
created: "2026-05-06"
updated: "2026-05-06"
sources:
  - "60_Resources/q-digestREADME.md at master.md"
  - "60_Resources/barefootsrcmainjavacombmwcaritbarefootanalysisDBRCAN.java at master.md"
summary: "近似分位点計算や周期データの密度クラスタリングなど、大規模データを扱うための特殊データ構造・アルゴリズム。"
---

# Approximate data structures

## 概要

大規模データセットを効率的に扱うための近似アルゴリズムや特殊データ構造の実装例。分位点近似や周期データのクラスタリングのように、通常の配列処理では重い課題に効く。

## 主要なトピック

- [[performance]]

## 詳細

- `Q-Digest` は大量の整数データに対して、圧縮率を保ちながら近似パーセンタイルを計算する
- `DBRCAN` は周期データに対する密度ベースクラスタリングを行い、ゼロ境界をまたぐクラスタも扱える

## 関連テーマ

- [[performance]]

## 出典

- `60_Resources/q-digestREADME.md at master.md`
- `60_Resources/barefootsrcmainjavacombmwcaritbarefootanalysisDBRCAN.java at master.md`
