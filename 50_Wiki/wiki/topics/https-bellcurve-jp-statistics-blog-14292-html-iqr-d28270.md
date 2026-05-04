---
title: "外れ値の見つけ方"
type: "topic"
tags:
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/外れ値の見つけ方.md"
summary: "外れ値の検出方法：IQR（四分位範囲）を用いたアプローチ"
---

# 外れ値の見つけ方

## 概要

外れ値の検出方法：IQR（四分位範囲）を用いたアプローチ

*発行: 2017-08-19 / [[https-bellcurve-jp-statistics-blog-14292-html-iqr-d28270]]*

## 主要なトピック


## 詳細

- 本記事では、正規分布を前提としない「IQRを用いた外れ値の特定手法」について解説しています。
- 重要なポイント
- **IQR（四分位範囲）とは**
- 第三四分位数から第一四分位数を引いた値（箱ひげ図の箱の長さ）。
- Excelでは `=QUARTILE(範囲, 3) - QUARTILE(範囲, 1)` で算出可能。
- **外れ値の判定基準**
- **上側の境界値**: 第三四分位数 + (IQR × 1.5)
- **下側の境界値**: 第一四分位数 - (IQR × 1.5)
- 上記の範囲外にあるデータを外れ値とみなす。

*発行: 2017-08-19 / [[https-bellcurve-jp-statistics-blog-14292-html-iqr-d28270]]*

## 関連テーマ


## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/外れ値の見つけ方.md`
- https://bellcurve.jp/statistics/blog/14292.html
