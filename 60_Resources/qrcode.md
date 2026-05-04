---
title: "qrcode"
source: "https://www.npmjs.com/package/qrcode"
author:
published: 2024-08-06
created: 2026-05-01
description: "QRCode / 2d Barcode api with both server side and client side support using canvas. Latest version: 1.5.4, last published: 2 years ago. Start using qrcode in your project by running `npm i qrcode`. There are 4843 other projects in the npm registry using qrcode."
tags:
  - "clippings"
---
## 概要
`qrcode` は、Node.jsおよびブラウザ環境で利用可能なQRコード生成ライブラリです。画像ファイル、Canvas、ターミナル出力など多様な形式に対応しています。

## 主な特徴
- **クロスプラットフォーム**: サーバーサイド、ブラウザ、React Nativeをサポート。
- **柔軟な出力**: PNG, SVG, UTF8形式での生成が可能。
- **高度なエンコーディング**: 数値、英数字、漢字、バイトモード、混合モードに対応。
- **最適化**: データ圧縮を自動最適化し、最小サイズのQRコードを生成。
- **マルチバイト文字**: 絵文字や多言語文字をサポート。

## 主な利用方法
- **CLI**: コマンドラインから直接QRコード画像を生成可能。
- **Node.js**: API経由でファイル出力やData URL生成が可能。
- **ブラウザ**: Canvas要素への描画やバンドラーを通じた利用が可能。

## 主要オプション
- **Error Correction Level**: L(~7%), M(~15%), Q(~25%), H(~30%)から選択可能。
- **Version**: 1から40のシンボルサイズを指定可能（デフォルトは自動選択）。
- **カスタマイズ**: 色（dark/light）、マージン、スケール調整が可能。