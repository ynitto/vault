---
title: "barefoot/src/main/java/com/bmwcarit/barefoot/analysis/DBRCAN.java at master"
source: "https://github.com/bmwcarit/barefoot/blob/master/src/main/java/com/bmwcarit/barefoot/analysis/DBRCAN.java"
author:
published:
created: 2026-05-05
description: "Java map matching library for integrating the map into software and services with state-of-the-art online and offline map matching that can be used stand-alone and in the cloud. - barefoot/src/main/java/com/bmwcarit/barefoot/analysis/DBRCAN.java at master · bmwcarit/barefoot"
tags:
  - "clippings"
---
### DBRCAN クラスの概要
DBRCAN（Density-Based Clustering Analysis in Residue Classes）は、周期的なデータ（剰余クラス）に対して密度ベースのクラスタリングを行うJavaクラスです。特に「ゼロ境界をまたぐクラスタ」（例：深夜0時をまたぐ時間帯のデータ）を検出できる点が特徴です。

### 主な特徴と機能
- **周期的なデータ対応**: モジュロ（剰余）演算を使用し、循環構造（リング）上でのクラスタリングを実現。
- **高精度な浮動小数点比較**: `epsilon` 定数を用いた浮動小数点数の丸め誤差を考慮した比較処理を実装。
- **密度ベースのクラスタリング**: 指定した半径（epsilon）と最小要素数（minimum）に基づき密度クラスタを抽出。
- **階層的クラスタリング**: `minimum` を指数的に増加させることで、密度の階層構造をステップ関数として解析可能。

### 主要なアルゴリズムの構成要素
*   **`modulo` / `epsilonRound`**: 周期的なデータの正規化と精度の維持。
*   **`moduloBetween`**: ある値が循環区間内にあるかを判定。
*   **`SearchIndex`**: 剰余クラス上の効率的な近傍探索を実現するインデックス構造。
*   **`bounds`**: 抽出されたクラスタの論理的な開始・終了境界を算出。
*   **`function`**: 密度に基づいて階層的なクラスタ境界をステップ関数形式で生成。
