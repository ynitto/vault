---
title: "GitLab API で Merge Request のコメントを一括取得する方法"
source: "https://qiita.com/akkie76/items/2cc798e309b0e82f13fc"
author:
  - "[[akkie76]]"
published: 2021-12-21
created: 2026-05-01
description: "はじめに GitLab API は以前から知っていましたが、これまで業務で利用する機会がなかなかありませんでした。この記事をご覧の方はご存知だと思いますが、GitLab API は REST API として非常に充実しており、GitLabの画面上で操作することができる A..."
tags:
  - "clippings"
---
### 概要
GitLab APIを活用し、チーム開発におけるコードレビューの質や量を定量化するための「Merge Request（MR）コメント集計ツール」の作成手法を解説した記事です。

### 要点
- **目的**: 若手メンバーのレビュー支援と、育成のための指標作成。
- **主な利用API**:
    - **Merge Requests API**: 対象となるMR情報の取得。
    - **Notes API**: 各MRのコメント取得（ただしDiscussionと重複が発生する点に注意）。
    - **Discussions API**: コメント内容をスレッド単位で取得するために使用。
- **実装のポイント**:
    - **Kotlinでの実装**: `fuel`を使用したHTTPリクエストと`Kotlinx.Serialization`によるデータパース。
    - **データ整形**: 抽出したコメントに正規表現でプレフィックス（独自ルール）を付与し、品質分析に活用。
    - **重複排除**: Note APIとDiscussions APIで重複するデータを除去し、CSV形式で出力して集計を行う。
- **結論**: GitLab APIを組み合わせることで、チームの状況を可視化する独自の分析ツールが構築可能。