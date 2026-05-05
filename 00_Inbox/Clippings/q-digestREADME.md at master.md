---
title: "q-digest/README.md at master"
source: "https://github.com/dhruvbird/q-digest/blob/master/README.md"
author:
published:
created: 2026-05-05
description: "C++ Implementation of the Q-Digest. Contribute to dhruvbird/q-digest development by creating an account on GitHub."
tags:
  - "clippings"
---
### 概要
このリポジトリは、大規模なデータセットのパーセンタイルを近似計算するためのデータ構造「Q-Digest」のC++実装です。

### 主な要点
* **Q-Digestとは**:
    * 整数値を持つ大規模データセットに対して、効率的に近似パーセンタイルを算出するための空間制約型データ構造。
    * 論文 [UCsb.sensys04.pdf](http://www.cs.virginia.edu/~son/cs851/papers/ucsb.sensys04.pdf) に基づく。

* **圧縮パラメータ (K)**:
    * `K` は圧縮率を制御するパラメータ。
    * 小さい値：圧縮率が高い（精度は低い）。
    * 大きい値：圧縮率が低い（精度は高い）。

* **主な機能（API）**:
    * `insert(key, count)`: データの挿入。
    * `percentile(p)`: 指定したパーセンタイルの算出。
    * `merge(rhs)`: 他のQ-Digestとの統合。
    * `toString()` / `fromString()`: シリアライズとデシリアライズ（保存・送信用）。

* **補足**:
    * コピーは高コストなため、統合演算子 (`+=`) を使用してコピーを作成する手法が推奨されています。
