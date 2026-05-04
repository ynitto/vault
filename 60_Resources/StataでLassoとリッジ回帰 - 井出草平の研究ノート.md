---
title: "StataでLassoとリッジ回帰 - 井出草平の研究ノート"
source: "https://ides.hatenablog.com/entry/2019/09/15/151920"
author:
  - "[[iDES]]"
published: 2019-09-15
created: 2026-05-01
description: "Stata16でLassoが新しく使えるようになったそうだ。 https://www.lightstone.co.jp/stata/stata16_new.html#Lasso 僕はStataはあまり使わないので、新しいStataを入手していない。今手元にあるものはバージョン13で少し古く、標準機能でLassoはできない。ただ、バージョン13以上であれば、パッケージとして作成されているlassopackが使用ができ、Lassoも問題なく使用することができる。 Stata Lasso https://statalasso.github.io/ 推定するパラメータ 最小二乗法 応答変数Y、n個の観…"
tags:
  - "clippings"
---
### 記事の要約
StataにおけるLasso回帰、リッジ回帰、Elastic Netの利用方法を解説した技術ノート。Stataの標準機能または`lassopack`パッケージを用いた推定方法、λ（ペナルティ）の最適化（情報量基準や交差検証）、および前立腺がんデータを用いた分析事例を紹介しています。

### 要点まとめ

#### 1. 推定手法とパラメータ
- **手法**: Lasso回帰、リッジ回帰、Elastic Netを利用可能。
- **パラメータ**: λ（正則化ペナルティ）の決定が重要。α=0でリッジ、α=1でLassoとなる。

#### 2. 最適なλの決定方法
- **情報量基準**: AIC, BIC, EBICなどを使用しモデルを選択する。
- **交差検証 (Cross-validation)**: `cvlasso`コマンドによるK-分割交差検証で、平均二乗予測誤差（MSPE）を最小化するλを特定する。

#### 3. 実践コマンドのポイント
- **インストール**: `ssc install lassopack`, `ssc install pdslasso`
- **情報量基準での推定**: `lasso2 [変数], lic(ebic)`
- **交差検証の実施**: `cvlasso [変数], seed(123)`
- **結果の確認**: `lopt`（予測誤差最小）または `lse`（標準誤差内での最小）オプションでモデルを選択。

#### 4. 注意点
- 交差検証のMSPEは乱数により変動する可能性があるため、シード値の指定が推奨される。
- 小標本ではMSPEが不安定になりやすいため注意が必要。