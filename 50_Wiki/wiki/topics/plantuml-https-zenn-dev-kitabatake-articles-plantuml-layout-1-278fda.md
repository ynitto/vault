---
title: "PlantUMLのレイアウトのコツと指定方法についてのまとめ"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/PlantUMLのレイアウトのコツと指定方法についてのまとめ.md"
summary: "PlantUMLのレイアウトを整えるコツと指定方法"
---

# PlantUMLのレイアウトのコツと指定方法についてのまとめ

## 概要

PlantUMLのレイアウトを整えるコツと指定方法

*発行: 2021-01-22 / [[plantuml-https-zenn-dev-kitabatake-articles-plantuml-layout-1-278fda]]*

## 主要なトピック


## 詳細

- PlantUMLで意図した図を描くための、レイアウト制御の要点は以下の通りです。
- 1. 接続線の長さによる配置制御
- `-` (ハイフン1つ): 関連性の高い要素を結び、近くに配置する。
- `--` (ハイフン2つ以上): 通常の関連。いい感じに配置する。
- ハイフンの数を増やすと、要素間の距離を長くできる。
- 2. 要素の記述順と方向
- 要素を記述する順番が配置に影響する（例：`-`は左から右、`--`は上から下へ配置される）。
- `top to bottom direction` や `left to right direction` で図全体の方向を指定可能。
- 3. レイアウトを制御するヒント

*発行: 2021-01-22 / [[plantuml-https-zenn-dev-kitabatake-articles-plantuml-layout-1-278fda]]*

## 関連テーマ


## 出典

- `../60_Resources/PlantUMLのレイアウトのコツと指定方法についてのまとめ.md`
- https://zenn.dev/kitabatake/articles/plantuml-layout
