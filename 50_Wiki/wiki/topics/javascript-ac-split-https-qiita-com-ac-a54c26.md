---
title: "引用符で囲まれた場合も考慮してカンマ区切りされた文字列を split して配列に変換する"
type: "topic"
tags:
  - "javascript"
  - "ac"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/引用符で囲まれた場合も考慮してカンマ区切りされた文字列を split して配列に変換する.md"
summary: "引用符（"）で囲まれたカンマを含む文字列を、適切に分割して配列に変換する JavaScript の関数 `convertListToArray` について…"
---

# 引用符で囲まれた場合も考慮してカンマ区切りされた文字列を split して配列に変換する

## 概要

引用符（"）で囲まれたカンマを含む文字列を、適切に分割して配列に変換する JavaScript の関数 `convertListToArray` について解説した記事です。単純な `split` では対応できないケース（金額の桁区切りなど）を解決する手法を紹介しています。

*発行: 2023-09-19 / [[javascript-ac-split-https-qiita-com-ac-a54c26]]*

## 主要なトピック

- [[javascript]]
- [[ac]]

## 詳細

- 引用符（"）で囲まれたカンマを含む文字列を、適切に分割して配列に変換する JavaScript の関数 `convertListToArray` について解説した記事です。単純な `split` では対応できないケース（金額の桁区切りなど）を解決する手法を紹介しています。
- 要点
- **解決する課題**: 単純な `split(',')` では、引用符内のカンマを区切り文字と誤認してしまう問題を解消。
- **主な実装機能**:
- `startsWith` / `endsWith` を用いて、引用符の開始と終了を判定。
- `slice` を使い、引用符で囲まれた部分を正しく抽出。
- 設定により区切り文字（`splitMark`）や引用符（`quoteMark`）の変更が可能。
- **メリット**: 数値の桁区切りや、引用符そのものが含まれるデータにも柔軟に対応可能。

*発行: 2023-09-19 / [[javascript-ac-split-https-qiita-com-ac-a54c26]]*

## 関連テーマ

- [[javascript]]
- [[ac]]

## 出典

- `60_Resources/引用符で囲まれた場合も考慮してカンマ区切りされた文字列を split して配列に変換する.md`
- https://qiita.com/ac_qiita/items/36ba56a71a40bb13edc6
