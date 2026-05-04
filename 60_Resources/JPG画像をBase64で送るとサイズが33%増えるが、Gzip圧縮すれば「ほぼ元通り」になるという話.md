---
title: "JPG画像をBase64で送るとサイズが33%増えるが、Gzip圧縮すれば「ほぼ元通り」になるという話"
source: "https://qiita.com/shiozaki/items/9d7aeac0dd6733a6e2fb"
author:
  - "[[shiozaki]]"
published: 2026-01-12
created: 2026-04-30
description: "当たり前なのではというはてぶが多かったので、画像のファイルフォーマット毎の差異もまとめてみました。 Web APIでJPG画像を送信する際、「バイナリ送信(multipart/form-data)で送るか」「Base64エンコードしてJSONに埋め込むか」で迷うこと..."
tags:
  - "clippings"
---
### 内容要約
Web APIにおけるJPG画像の送信手法（Base64によるJSON埋め込み vs multipart/form-dataによるバイナリ転送）について、通信サイズとリソース負荷の観点から解説した記事。

### 要点まとめ

- **通信サイズは同等**
    - Base64はデータサイズを約33%増加させるが、HTTP圧縮（Gzip/Brotli）を有効にすることで、その冗長な「隙間」が回収され、バイナリ転送とほぼ同じサイズになる。

- **情報理論の仕組み**
    - Base64は6bitの情報を8bitの文字で表現するため、高い冗長性を持つ。Gzipのハフマン符号化がこの偏りを検知し、効率的に再圧縮を行うため元のサイズに戻る。

- **選択の基準**
    - **Base64 (JSON埋め込み):** フロントエンドの実装が容易だが、エンコード/デコード処理が加わるため、**CPU負荷とメモリ消費量は高い**。
    - **バイナリ送信 (multipart/form-data):** 変換が不要なため、**CPU・メモリ効率において非常に有利**。
