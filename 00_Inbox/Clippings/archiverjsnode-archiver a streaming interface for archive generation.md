---
title: "archiverjs/node-archiver: a streaming interface for archive generation"
source: "https://github.com/archiverjs/node-archiver/tree/master"
author:
published:
created: 2026-05-05
description: "a streaming interface for archive generation. Contribute to archiverjs/node-archiver development by creating an account on GitHub."
tags:
  - "clippings"
---
### 概要
`archiver`は、Node.js向けのストリーミング方式によるアーカイブ生成ライブラリです。ZIPおよびTAR形式の圧縮をサポートしており、ファイルやストリーム、バッファからアーカイブを作成できます。

### 主な特徴と要点
- **ストリーミング対応**: Node.jsのStream APIを活用し、効率的なデータ処理が可能。
- **柔軟な追加手法**:
  - `append()`: ファイルストリーム、文字列、Bufferからデータ追加。
  - `file()`: ローカルファイルから直接追加。
  - `directory()`: 指定ディレクトリ配下のファイルを一括追加。
  - `glob()`: Globパターンを使用して特定のファイルを一括追加。
- **導入方法**: `npm install archiver --save` でインストール。
- **イベント駆動**: `close`, `end`, `warning`, `error` などのイベントを監視し、ライフサイクルやエラーハンドリングを制御。
- **利用状況**: GitHub上で3,000以上のスターを獲得し、約91万件のリポジトリで使用されている非常に人気のあるパッケージです。
