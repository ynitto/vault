---
title: "TypeScriptでCLIツールを作って、npmパッケージにする"
source: "https://qiita.com/suzuki_sh/items/f3349efbfe1bdfc0c634"
author:
  - "[[sakai-akinobu]]"
published: 2021-02-07
created: 2026-04-30
description: "環境 node 9.4.0 TypeScript 2.9.2 npm 6.1.0 webpack 4.16.3 Visual Studio Code 1.25.1 予めtj/n: Node version management等を使って、Node.jsをインストールし..."
tags:
  - "clippings"
---
### 記事の要約
TypeScriptを用いてCLIツールを開発し、npmパッケージとして公開するためのビルド環境構築と設定方法を解説した技術ガイドです。webpackを使用して開発と本番それぞれのビルドプロセスを最適化し、Gitとnpmパッケージの配布内容を整理する手順がまとめられています。

### 主要なポイント
- **環境構築とビルド設定**
    - `webpack`と`ts-loader`を使用してTypeScriptのビルド環境を構築。
    - `tsconfig.json`によるTypeScriptの設定と、ターゲット環境（Node.js）の指定。
- **CLIツールの実装**
    - `package.json`の`bin`フィールドでCLIコマンドを定義。
    - `npm link`を活用して、開発中にローカル環境でCLIツールをテスト可能に。
- **開発効率の向上**
    - `webpack-merge`を使用し、開発用（watchモード・ソースマップ）と本番用でビルド設定を分離。
    - VSCodeのタスク機能（`tasks.json`）を活用し、エディタ上からビルドプロセスを管理。
- **パッケージ公開の管理**
    - `.gitignore`でビルド済みファイルを無視し、`.npmignore`でソースコードを無視する構成により、リポジトリとパッケージを最適化。
    - `npm publish`時には、npmスクリプトを活用して自動的に本番ビルドが実行される仕組みを構築。
