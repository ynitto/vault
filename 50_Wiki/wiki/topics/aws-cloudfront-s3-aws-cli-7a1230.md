---
title: "[小ネタ] S3に保存されているログファイルをAWS CLIでまとめてコピーする"
type: "topic"
tags:
  - "aws"
  - "cloudfront"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/小ネタ S3に保存されているログファイルをAWS CLIでまとめてコピーする.md"
summary: "AWS CLIを使用して、S3上の大量のログファイルから特定の日付・条件のファイルをローカルへ効率的にコピーする方法の解説。"
---

# [小ネタ] S3に保存されているログファイルをAWS CLIでまとめてコピーする

## 概要

AWS CLIを使用して、S3上の大量のログファイルから特定の日付・条件のファイルをローカルへ効率的にコピーする方法の解説。

*発行: 2016-09-24 / [[aws-cloudfront-s3-aws-cli-7a1230]]*

## 主要なトピック

- [[aws]]
- [[cloudfront]]

## 詳細

- AWS CLIを使用して、S3上の大量のログファイルから特定の日付・条件のファイルをローカルへ効率的にコピーする方法の解説。
- 要点
- **ワイルドカードの制限**
- S3コマンドでは標準的なUNIXのワイルドカードは使用不可。
- `--recursive` オプションと `--exclude` / `--include` オプションを組み合わせてフィルタリングを行う。
- **コピーの基本戦略**
- `--exclude \\"*\\"` で一旦すべてを除外し、`--include \\"特定文字列\\"` で対象を指定するのが定石。
- コピー対象が多い場合、ローカルでの処理負荷を抑えるため、S3 URI（パス）はできるだけ深く（詳細に）指定する。
- **活用例**

*発行: 2016-09-24 / [[aws-cloudfront-s3-aws-cli-7a1230]]*

## 関連テーマ

- [[aws]]
- [[cloudfront]]

## 出典

- `../60_Resources/小ネタ S3に保存されているログファイルをAWS CLIでまとめてコピーする.md`
- https://dev.classmethod.jp/articles/s3-logfile-copy-by-awscli/
