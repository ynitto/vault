---
title: "perceptual hash(phash)を利用して画像比較をしてみる"
type: "topic"
tags:
  - "node-js"
  - "hideack"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../../60_Resources/perceptual hash(phash)を利用して画像比較をしてみる.md"
summary: "perceptual hash（pHash）を用いた画像比較の解説"
---

# perceptual hash(phash)を利用して画像比較をしてみる

## 概要

perceptual hash（pHash）を用いた画像比較の解説

## 主要なトピック

- [[node-js]]
- [[hideack]]

## 詳細

- 本記事では、画像コンテンツの類似性を判定する「perceptual hash」の仕組みと、Node.jsを用いた実装・実験について解説しています。
- pHashの主な特徴
- **静止画・音声などのマルチメディア対応**: コンテンツの内容に基づくハッシュ値生成が可能。
- **加工耐性**: 画像の縮小、色調補正、ノイズ付加などに対して堅牢。
- **ハミング距離**: 類似度をハミング距離で測定し、値が小さいほど類似度が高いと判断される。
- 実装のポイント
- **アルゴリズム**: 画像を縮小後、離散コサイン変換（DCT）を行い、低周波成分を抽出してハッシュ化。
- **Node.jsでの利用**: `phash`ライブラリと`ImageMagick`を使用して実装可能。
- 実験結果のまとめ

## 関連テーマ

- [[node-js]]
- [[hideack]]

## 出典

- `../../60_Resources/perceptual hash(phash)を利用して画像比較をしてみる.md`
- https://hideack.site/entry/2015/03/16/194336
