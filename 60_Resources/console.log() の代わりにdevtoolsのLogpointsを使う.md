---
title: "console.log() の代わりにdevtoolsのLogpointsを使う"
source: "https://qiita.com/Tsuyoshi84/items/e398ac4449a36286c0d7?utm_source=Qiita%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9&utm_campaign=2b58d4db17-Qiita_newsletter_590_11_01&utm_medium=email&utm_term=0_e44feaa081-2b58d4db17-53271669"
author:
  - "[[Tsuyoshi84]]"
published: 2023-10-24
created: 2026-04-30
description: "Logpointsを使おう Webフロントエンドの開発をする際、デバッグ目的で「特定の処理が実行された」ということを確認するために console.log() を使うことは多いと思います。しかし、Google Chrome や Microsoft Edge で利用可能な ..."
tags:
  - "clippings"
---
### 記事の要約
この記事では、JavaScriptのデバッグ時に `console.log()` を使わずに、ChromeやEdgeのデベロッパーツール機能である「Logpoints」を活用する方法が解説されています。

### Logpointsを使うメリット
- **コード変更が不要**: デバッグのためにソースコードを書き換える必要がない。
- **事故防止**: `console.log()` を誤って本番環境のコードに含めてコミットするリスクを防げる。
- **効率化**: 再ビルドやホットリロードを待たずに即座にログを出力できる。

### Logpointsの使い方
1. デベロッパーツールを開き「Sources」タブを選択。
2. ログを出力したいファイルを開く。
3. 該当行の行番号を右クリックし、「Add logpoint...」を選択。
4. 出力したいメッセージや変数名を入力して完了。
