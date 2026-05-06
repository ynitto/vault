---
title: "Electron開発の覚書"
type: "topic"
tags:
  - "sy250f"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Electron開発の覚書.md"
summary: "Electron開発時に使用したライブラリと、VS Codeでのデバッグ方法に関する備忘録です。"
---

# Electron開発の覚書

## 概要

Electron開発時に使用したライブラリと、VS Codeでのデバッグ方法に関する備忘録です。

*発行: 2024-01-11 / [[sy250f-electron-https-qiita-com-sy250f-items-1e568f7ae17003199f32-vs-5f7d83]]*

## 主要なトピック

- [[sy250f]]

## 詳細

- Electron開発時に使用したライブラリと、VS Codeでのデバッグ方法に関する備忘録です。
- 要点まとめ
- 使用ライブラリ
- **electron-store**: アプリの設定値（JSON形式）をユーザーフォルダ内に永続的に保存するために使用。
- **dotenv**: `.env` ファイルから環境変数を読み込み、Mainプロセス全体で利用可能にする。※UTF-8エンコード必須。
- **electron-log**: ログをファイルへ簡単に出力するライブラリ。v5はElectron v13+、v4はそれ以前のバージョンに対応。
- デバッグ設定
- **VS Codeでのデバッグ**: `launch.json` を作成・編集し、`runtimeExecutable` にElectronのパスを指定することで、F5キーからメインプロセスのデバッグを実行可能。

*発行: 2024-01-11 / [[sy250f-electron-https-qiita-com-sy250f-items-1e568f7ae17003199f32-vs-5f7d83]]*

## 関連テーマ

- [[sy250f]]

## 出典

- `60_Resources/Electron開発の覚書.md`
- https://qiita.com/sy250f/items/1e568f7ae17003199f32
