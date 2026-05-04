---
title: "How to Convert SVG to PNG in Node.js, Including Base64-Encoded Images?"
source: "https://stackoverflow.com/questions/77458490/how-to-convert-svg-to-png-in-node-js-including-base64-encoded-images"
author:
  - "[[Muhammad Usman 122 bronze badges]]"
  - "[[Blue Water 1901111 bronze badges]]"
published: 2023-11-10
created: 2026-04-30
description: "Hello Stack Overflow Community,I am working on a Node.js project where I need to convert SVG files to PNG & JPEG format. My SVG files are unique in that they include images encoded as base64 d..."
tags:
  - "clippings"
---
### 質問内容の要約
Node.js環境で、Base64エンコードされた画像を含むSVGファイルを、高品質なPNG/JPEG形式へ変換する方法についての質問です。既存の`sharp`ライブラリを使用したアプローチでは、埋め込み画像が正しくレンダリングされず、画質も不十分であるという課題を抱えています。

### 要点
- **目的**: SVG（Base64画像入り）からPNG/JPEGへの高品質な変換。
- **環境**: Node.js。
- **現状の課題**: `sharp`の単純な変換処理では、埋め込み画像が欠落または非表示になり、出力品質が低い。
- **回答のヒント**: 提供された回答案では、`sharp`の`composite`機能を利用して、個別に生成したQRコードやテキストSVGを合成する手法が示されています。
