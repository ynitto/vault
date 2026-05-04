---
title: "要素の差分、足し合わせを計算するNumPyのdiff関数とcumsum関数の使い方"
type: "topic"
tags:
  - "deepage"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/要素の差分、足し合わせを計算するNumPyのdiff関数とcumsum関数の使い方.md"
summary: "NumPyの要素操作関数：`np.diff` と `np.cumsum`"
---

# 要素の差分、足し合わせを計算するNumPyのdiff関数とcumsum関数の使い方

## 概要

NumPyの要素操作関数：`np.diff` と `np.cumsum`

*発行: 2017-08-16 / [[deepage-numpy-diff-cumsum-https-47669c]]*

## 主要なトピック

- [[deepage]]

## 詳細

- 本記事では、NumPy配列における要素間の差分計算と累積和計算を行う2つの関数について解説しています。
- 1. `np.diff`（差分計算）
- 配列内の隣接する要素間の差を計算し、データ変化や微分近似に用いられます。
- **主な引数**:
- `a`: 対象の配列。
- `n`: 微分階数（デフォルトは1）。
- `axis`: 差分をとる軸方向（デフォルトは最後の次元）。
- **特徴**: 実行後の配列サイズは、差分をとった軸方向に1つ減少します。
- 2. `np.cumsum`（累積和計算）

*発行: 2017-08-16 / [[deepage-numpy-diff-cumsum-https-47669c]]*

## 関連テーマ

- [[deepage]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/要素の差分、足し合わせを計算するNumPyのdiff関数とcumsum関数の使い方.md`
- https://deepage.net/features/numpy-diff.html
