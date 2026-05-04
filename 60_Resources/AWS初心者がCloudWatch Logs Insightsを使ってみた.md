---
title: "AWS初心者がCloudWatch Logs Insightsを使ってみた"
source: "https://qiita.com/suuu/items/8387df88f134348f22c7"
author:
  - "[[kesoji]]"
published: 2020-10-08
created: 2026-05-01
description: "AWS初心者ですが、最近担当した業務で、APIが出力しているログを さくっと分析・調査したい場面があったのでCloudWatch Logs Insightsを使ってみました。 実際に調査で使ったクエリの例なども含めて、備忘録も兼ねてまとめます。 これからCloudWatch..."
tags:
  - "clippings"
---
### CloudWatch Logs Insightsの要約
AWSのCloudWatch Logs Insightsは、ログデータを効率的に検索・分析できる機能です。SQLライクな独自構文を使用し、スキャンしたデータ量に応じた従量課金制で利用可能です。

### 主要な機能とポイント
- **クエリの基本操作**
    - `fields`: 取得するフィールド（カラム）を指定
    - `filter`: 抽出条件の指定（例: `like` で文字列検索）
    - `sort`: 並び替え（`asc`/`desc`）
    - `limit`: 取得件数の制限
    - `stats`: `count`, `avg`, `sum` などの集計関数
    - `parse`: 正規表現等を用いてログから特定項目を抽出
- **活用例**
    - 特定文字列を含むログの抽出と表示
    - JSONログのフィールド単位での集計
    - 複数イベントのタイムスタンプ差分による処理時間の算出
- **メリット**
    - 初心者でも直感的に使い始められる
    - クエリ結果のダッシュボード追加や保存が可能
