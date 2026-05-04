---
title: "WebGLでGPGPU（gpu.js / turbo.js / deeplearn.js / WebDNN）"
source: "https://qiita.com/spring_raining/items/a040d647373cfe0e2201"
author:
  - "[[spring_raining]]"
published: 2017-12-16
created: 2026-04-30
description: "WebGLはコンピュータグラフィックスのための機能しかないと思われがちですが，数値計算のようにグラフィックとは関係ないGeneral-purpose computing on GPU（GPGPU）に転用することもできます．そこで，WebGLを使ってGPGPUを実現しているラ..."
tags:
  - "clippings"
---
### 記事の要約
WebGLを用いたGPGPU（汎用GPU計算）を実現するJavaScriptライブラリを紹介する記事です。グラフィックス専用と思われがちなWebGLを数値計算に応用する手法と、代表的な4つのライブラリの特徴を解説しています。

### 紹介されているライブラリの要点
- **gpu.js**
    - Kernel functionを定義し、GPU上で並列計算を実行。
    - 関数をパースしてGLSLへ変換する直感的なAPIが特徴。
- **turbo.js**
    - 200行程度の軽量ライブラリ。
    - GLSLコードを直接記述するため、カスタマイズ性が高く高速。
- **deeplearn.js (現 TensorFlow.js)**
    - ディープラーニングの計算に特化。
    - 行列演算やモデル構築用のAPIが豊富で、学習済みモデルの実行にも対応。
- **WebDNN**
    - DNNモデルの高速実行に特化。
    - WebAssemblyやWebGPUを活用し、ブラウザ上で学習済みモデルを効率的に推論可能。

### 結論
- ライブラリを活用することで手軽にGPU並列計算が可能。
- GPU特有の挙動や計算を深く理解するには、WebGLおよびGLSLの直接的な学習が推奨される。
