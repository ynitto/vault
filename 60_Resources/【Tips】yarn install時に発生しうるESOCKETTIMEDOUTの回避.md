---
title: "【Tips】yarn install時に発生しうるESOCKETTIMEDOUTの回避"
source: "https://qiita.com/GandT/items/9c2afa82609ff6062fd3"
author:
  - "[[GandT]]"
published: 2019-09-18
created: 2026-04-30
description: "問題：yarn installの失敗 入力 yarnでパッケージ管理を行っているディレクトリ（フォルダ）において、 yarn install を実行すると、下記のようにESOCKETTIMEDOUTのエラーが発生し正常にインストールできない場合がある。 出力 [1/..."
tags:
  - "clippings"
---
### 要約
`yarn install`実行時に発生するエラー「ESOCKETTIMEDOUT」は、大容量パッケージのダウンロード時間が規定時間を超過することで発生します。解決策として、タイムアウト時間を延長する設定を`.yarnrc`ファイルに追加することで回避可能です。

### 対応策
* **設定ファイル**: `yarn install`を実行するディレクトリに`.yarnrc`を作成または編集する。
* **記述内容**:
  ```text
  network-timeout 600000
  ```
  * ※上記は600,000ミリ秒（10分）の設定値です。

### 補足
* **単位**: ミリ秒（ms）で指定するため、秒数に換算する場合は`値 ÷ 1000`で計算します。
* **調整**: ネットワーク環境が非常に遅い場合は、数値をさらに大きくして調整してください。
