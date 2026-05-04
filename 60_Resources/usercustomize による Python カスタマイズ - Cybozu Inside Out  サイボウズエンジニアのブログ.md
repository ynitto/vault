---
title: "usercustomize による Python カスタマイズ - Cybozu Inside Out | サイボウズエンジニアのブログ"
source: "https://blog.cybozu.io/entry/2126"
author:
  - "[[cybozuinsideout]]"
published: 2012-12-10
created: 2026-04-30
description: "「サイボウズ・アドベントカレンダー2012」も、第2週に入りました。今週もバラエティに富んだ内容でお送りします（これまでの記事一覧）。 こんにちは。 Hazama チームの深谷です。 Hazama チームは cybozu.com のインフラ開発チームのことで、仮想マシンの操作や、各種モニタリング、バックアップ等のツール作りを行なっています。 今回は、Hazama が主に利用している Python の Tips という事で、usercustomize という仕組みについて紹介したいと思います。"
tags:
  - "clippings"
---
### 概要
Pythonの起動時に任意のコードを自動実行できる「`usercustomize`」の仕組みと、その実践的な活用方法についての解説記事です。

### 要点
- **usercustomize とは**
  - Python起動時に読み込まれるユーザー固有の設定ファイル。
  - `site` モジュールにより、環境ごとの設定を柔軟に行うことが可能。

- **sitecustomize との違い**
  - `sitecustomize` はシステム全体の設定向けで、検索パスの優先順位が競合する可能性がある。
  - `usercustomize` はユーザーホームディレクトリ配下のパスが検索されるため、システム設定に干渉せず安全にカスタマイズできる。

- **実践的活用例**
  - 開発環境で特定の条件下（例：実行パスに基づく判断）のみライブラリパスを書き換え、安全にツールテストを行う。
  - 実装には `sys.argv` 等の取得タイミングに注意が必要（直接的な取得が困難な場合は `/proc/pid/cmdline` を参照するバッドノウハウも紹介）。

- **推奨事項**
  - 廃止予定の `user` モジュールよりも、`usercustomize` の利用を推奨。
