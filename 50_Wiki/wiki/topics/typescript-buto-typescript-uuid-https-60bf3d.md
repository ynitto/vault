---
title: "typescript uuid桁数を短くする"
type: "topic"
tags:
  - "typescript"
  - "buto"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/typescript uuid桁数を短くする.md"
summary: "UUID（32桁）をBase64エンコードし、22桁に短縮する方法を紹介する技術メモです。"
---

# typescript uuid桁数を短くする

## 概要

UUID（32桁）をBase64エンコードし、22桁に短縮する方法を紹介する技術メモです。

*発行: 2022-05-01 / [[typescript-buto-typescript-uuid-https-60bf3d]]*

## 主要なトピック

- [[typescript]]
- [[buto]]

## 詳細

- UUID（32桁）をBase64エンコードし、22桁に短縮する方法を紹介する技術メモです。
- 短縮のポイント
- **手法**: UUIDを16進数配列に変換後、Base64エンコードを行い、末尾のパディング（==）を除去する。
- **実装例**:
- ```typescript
- const hexArray = uuidv4().split('-').join('').split('', 16).map(h => parseInt(h, 16));
- const shortId = Buffer.from(hexArray).toString('base64').replace('==', '');
- ```
- **結果**: 元の32桁のUUIDが22桁の文字列へと短縮されます。

*発行: 2022-05-01 / [[typescript-buto-typescript-uuid-https-60bf3d]]*

## 関連テーマ

- [[typescript]]
- [[buto]]

## 出典

- `60_Resources/typescript uuid桁数を短くする.md`
- https://qiita.com/buto/items/1b6cc0b244dc1d42da79
