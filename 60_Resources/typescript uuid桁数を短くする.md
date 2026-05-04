---
title: "typescript uuid桁数を短くする"
source: "https://qiita.com/buto/items/1b6cc0b244dc1d42da79"
author:
  - "[[buto]]"
published: 2022-05-01
created: 2026-05-01
description: "uuid桁数はbase64エンコードで32桁→22桁に減らすことができます！ （typescriptでの書き方が分からず苦戦したのでメモしておきます） id生成ライブラリはuuidv4を使っています const originId = uuidv4(); console.lo..."
tags:
  - "clippings"
---
### 記事要約
UUID（32桁）をBase64エンコードし、22桁に短縮する方法を紹介する技術メモです。

### 短縮のポイント
- **手法**: UUIDを16進数配列に変換後、Base64エンコードを行い、末尾のパディング（==）を除去する。
- **実装例**:
  ```typescript
  const hexArray = uuidv4().split('-').join('').split('', 16).map(h => parseInt(h, 16));
  const shortId = Buffer.from(hexArray).toString('base64').replace('==', '');
  ```
- **結果**: 元の32桁のUUIDが22桁の文字列へと短縮されます。