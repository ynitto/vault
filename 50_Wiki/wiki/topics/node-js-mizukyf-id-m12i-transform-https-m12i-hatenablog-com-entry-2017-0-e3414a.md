---
title: "興味本位にTransformストリームを実装する"
type: "topic"
tags:
  - "node-js"
  - "mizukyf-id-m12i"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/興味本位にTransformストリームを実装する.md"
summary: "Node.jsのStream APIを活用し、学習目的でカスタムの`Transform`ストリームを2種類実装する手法についての技術解説です。"
---

# 興味本位にTransformストリームを実装する

## 概要

Node.jsのStream APIを活用し、学習目的でカスタムの`Transform`ストリームを2種類実装する手法についての技術解説です。

*発行: 2017-07-17 / [[node-js-mizukyf-id-m12i-transform-https-m12i-hatenablog-com-entry-2017-0-e3414a]]*

## 主要なトピック

- [[node-js]]
- [[mizukyf-id-m12i]]

## 詳細

- Node.jsのStream APIを活用し、学習目的でカスタムの`Transform`ストリームを2種類実装する手法についての技術解説です。
- 実装したTransformストリームの要点
- 1. 行分割用ストリーム (`makeLines`)
- **機能**: 渡されたチャンクを改行コード（LF, CR, CRLF）で分割して行単位で出力します。
- **ポイント**:
- チャンクの途中で行が切れる場合に対応するため、未処理分を`remaining`変数に保持するロジックを実装。
- `_transform`内で`this.push`を直接呼び出すとレシーバの問題が発生するため、専用のプロキシ関数を経由させています。
- `_final`メソッドで残存する文字列を処理する工夫がされています。
- 2. 改行除去用ストリーム (`trimEol`)

*発行: 2017-07-17 / [[node-js-mizukyf-id-m12i-transform-https-m12i-hatenablog-com-entry-2017-0-e3414a]]*

## 関連テーマ

- [[node-js]]
- [[mizukyf-id-m12i]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/興味本位にTransformストリームを実装する.md`
- https://m12i.hatenablog.com/entry/2017/07/17/124617
