---
title: "製造業のDXで良く使うopenpyxl入門"
source: "https://zenn.dev/tikita/articles/bc2e2d40cd4764"
author:
published: 2023-06-07
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 概要
Pythonライブラリ「openpyxl」を使用して、Excel（.xlsx形式）の読み書きや自動化を行うための基礎知識と応用テクニックを解説した記事です。

### 要点まとめ
- **openpyxlの役割**
  - Excelをインストールしていない環境でも利用可能。データ分析や自動化に最適。
  - 書式の読み書きが可能（pandasとの大きな違い）。
- **基本操作の構成**
  - ワークブック（Workbook）、ワークシート（Worksheet）、セル（Cell）の階層構造で扱う。
  - `load_workbook`で読み込み、`save`で保存を行う。
- **データ操作のテクニック**
  - 行・列の反復には `iter_rows()` や `iter_cols()` が便利。
  - `cell.row`, `cell.column` を使用してセルの位置情報を取得可能。
- **Excel装飾のカスタマイズ**
  - `styles` モジュールのクラス（PatternFill, Alignment, Font, Border）を使用し、色・配置・フォント・枠線を制御可能。
- **便利な周辺機能**
  - `max_row` / `max_column` による範囲取得。
  - 列の英字（A, B, C...）と数値（1, 2, 3...）の相互変換。
  - ハイパーリンクの設定や、行列の挿入・削除。