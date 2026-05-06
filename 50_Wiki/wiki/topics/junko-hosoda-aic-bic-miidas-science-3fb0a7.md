---
title: "AICとBIC？情報量基準とは？ – MIIDAS Science Blog"
type: "topic"
tags:
  - "junko-hosoda"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/AICとBIC？情報量基準とは？ – MIIDAS Science Blog.md"
summary: "本記事は、モデル選択の指標となる「情報量基準（AIC・BIC）」の概念と使い分け、および関連するKLダイバージェンスの性質について解説しています。"
---

# AICとBIC？情報量基準とは？ – MIIDAS Science Blog

## 概要

本記事は、モデル選択の指標となる「情報量基準（AIC・BIC）」の概念と使い分け、および関連するKLダイバージェンスの性質について解説しています。

*発行: 2019-04-10 / [[junko-hosoda-aic-bic-miidas-science-3fb0a7]]*

## 主要なトピック

- [[junko-hosoda]]

## 詳細

- 本記事は、モデル選択の指標となる「情報量基準（AIC・BIC）」の概念と使い分け、および関連するKLダイバージェンスの性質について解説しています。
- 要点まとめ
- **情報量基準の目的**
- モデルの誤差（error）を最小化しつつ、パラメータの過剰な増加による「過学習（overfitting）」を防ぐために使用されます。
- **AICとBICの違い**
- **AIC**: 未知の高次元な現実を記述するためのモデル選択に適しており、過学習を抑制する基準。
- **BIC**: 候補モデルの中に「真のモデル」が含まれていると仮定して計算される、より厳しい基準。データ数が増えるほどペナルティが強くなる。
- **使い分けのヒント**
- 両方の指標を併用し、それぞれの値が小さいモデルを選択するのが推奨されます。

*発行: 2019-04-10 / [[junko-hosoda-aic-bic-miidas-science-3fb0a7]]*

## 関連テーマ

- [[junko-hosoda]]

## 出典

- `../60_Resources/AICとBIC？情報量基準とは？ – MIIDAS Science Blog.md`
- https://research.miidas.jp/2019/04/aic%E3%81%A8bic%EF%BC%9F%E6%83%85%E5%A0%B1%E9%87%8F%E5%9F%BA%E6%BA%96%E3%81%A8%E3%81%AF%EF%BC%9F/
