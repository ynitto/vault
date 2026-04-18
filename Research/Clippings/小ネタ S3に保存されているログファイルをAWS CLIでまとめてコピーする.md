---
title: "[小ネタ] S3に保存されているログファイルをAWS CLIでまとめてコピーする"
source: "https://dev.classmethod.jp/articles/s3-logfile-copy-by-awscli/"
author:
  - "[[清水俊也]]"
published: 2016-09-24
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
AWS CLIを使用して、S3上の大量のログファイルから特定の日付・条件のファイルをローカルへ効率的にコピーする方法の解説。

### 要点
- **ワイルドカードの制限**
  - S3コマンドでは標準的なUNIXのワイルドカードは使用不可。
  - `--recursive` オプションと `--exclude` / `--include` オプションを組み合わせてフィルタリングを行う。

- **コピーの基本戦略**
  - `--exclude \\"*\\"` で一旦すべてを除外し、`--include \\"特定文字列\\"` で対象を指定するのが定石。
  - コピー対象が多い場合、ローカルでの処理負荷を抑えるため、S3 URI（パス）はできるだけ深く（詳細に）指定する。

- **活用例**
  - **S3ログ**: `--include \\"YYYY-MM-DD*\\"` で指定。
  - **ELBログ**: `--include \\"*.log\\"` やパス階層での絞り込みを活用。
  - **CloudFrontログ**: `--include \\"*YYYY-MM-DD*.gz\\"` 等で指定。

- **運用のアドバイス**
  - 実行前に `--dryrun` オプションを使い、コピー対象が正しいか事前に確認することを推奨。