---
title: "WebGLでGPGPU（gpu.js / turbo.js / deeplearn.js / WebDNN）"
type: "topic"
tags:
  - "javascript"
  - "spring-raining"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/WebGLでGPGPU（gpu.js  turbo.js  deeplearn.js  WebDNN）.md"
summary: "WebGLを用いたGPGPU（汎用GPU計算）を実現するJavaScriptライブラリを紹介する記事です。グラフィックス専用と思われがちなWebGLを数値…"
---

# WebGLでGPGPU（gpu.js / turbo.js / deeplearn.js / WebDNN）

## 概要

WebGLを用いたGPGPU（汎用GPU計算）を実現するJavaScriptライブラリを紹介する記事です。グラフィックス専用と思われがちなWebGLを数値計算に応用する手法と、代表的な4つのライブラリの特徴を解説しています。

*発行: 2017-12-16 / [[javascript-spring-raining-webgl-gpgpu-gpu-js-f89813]]*

## 主要なトピック

- [[javascript]]
- [[spring-raining]]

## 詳細

- WebGLを用いたGPGPU（汎用GPU計算）を実現するJavaScriptライブラリを紹介する記事です。グラフィックス専用と思われがちなWebGLを数値計算に応用する手法と、代表的な4つのライブラリの特徴を解説しています。
- 紹介されているライブラリの要点
- **gpu.js**
- Kernel functionを定義し、GPU上で並列計算を実行。
- 関数をパースしてGLSLへ変換する直感的なAPIが特徴。
- **turbo.js**
- 200行程度の軽量ライブラリ。
- GLSLコードを直接記述するため、カスタマイズ性が高く高速。
- **deeplearn.js (現 TensorFlow.js)**

*発行: 2017-12-16 / [[javascript-spring-raining-webgl-gpgpu-gpu-js-f89813]]*

## 関連テーマ

- [[javascript]]
- [[spring-raining]]

## 出典

- `../60_Resources/WebGLでGPGPU（gpu.js  turbo.js  deeplearn.js  WebDNN）.md`
- https://qiita.com/spring_raining/items/a040d647373cfe0e2201
