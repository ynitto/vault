---
title: "Electron開発の覚書"
source: "https://qiita.com/sy250f/items/1e568f7ae17003199f32"
author:
  - "[[sy250f]]"
published: 2024-01-11
created: 2026-05-01
description: "Electron関連の開発時に調べたことの覚書です。 それ以上のことは特にありません。 現在のプロジェクトで利用している範囲のため、使っているライブラリがそもそも古いなどがあるかもしれません。 ライブラリ electron-store 設定値とかを保存するやつですね。 ..."
tags:
  - "clippings"
---
### 記事の要約
Electron開発時に使用したライブラリと、VS Codeでのデバッグ方法に関する備忘録です。

### 要点まとめ
#### 使用ライブラリ
*   **electron-store**: アプリの設定値（JSON形式）をユーザーフォルダ内に永続的に保存するために使用。
*   **dotenv**: `.env` ファイルから環境変数を読み込み、Mainプロセス全体で利用可能にする。※UTF-8エンコード必須。
*   **electron-log**: ログをファイルへ簡単に出力するライブラリ。v5はElectron v13+、v4はそれ以前のバージョンに対応。

#### デバッグ設定
*   **VS Codeでのデバッグ**: `launch.json` を作成・編集し、`runtimeExecutable` にElectronのパスを指定することで、F5キーからメインプロセスのデバッグを実行可能。
