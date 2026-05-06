---
title: "Java21 + Windowsにおける文字化け対策の設定のまとめ"
type: "topic"
tags:
  - "testing"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Java21 + Windowsにおける文字化け対策の設定のまとめ.md"
summary: "Java 21 + Windows における文字化け対策の要約"
---

# Java21 + Windowsにおける文字化け対策の設定のまとめ

## 概要

Java 21 + Windows における文字化け対策の要約

*発行: 2024-07-27 / [[testing-java21-windows-https-zenn-dev-leoninja-articles-10831509338169-3e5777]]*

## 主要なトピック

- [[testing]]

## 詳細

- Windows環境でJava 21を利用する際、UTF-8への統一とコンソール出力の文字化けを防ぐための設定手順です。
- 主要な対策ポイント
- **実行環境の共通設定**: `chcp 65001` コマンドを使用して、バッチ実行時のコンソール出力をUTF-8化する（`gradlew.bat` や `mvnw.cmd` に追記）。
- **JVM引数**: `-Dfile.encoding=UTF-8` を各ツールに設定する。
- ツール別の設定要点
- **Gradle**
- `gradle.properties`: `org.gradle.jvmargs=-Dfile.encoding=UTF-8` を追加。
- `build.gradle.kts`: `JavaExec`, `JavaCompile`, `test` 等のタスクにエンコーディング設定を追加。
- **Maven**

*発行: 2024-07-27 / [[testing-java21-windows-https-zenn-dev-leoninja-articles-10831509338169-3e5777]]*

## 関連テーマ

- [[testing]]

## 出典

- `60_Resources/Java21 + Windowsにおける文字化け対策の設定のまとめ.md`
- https://zenn.dev/leoninja/articles/10831509338169
