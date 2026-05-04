---
title: "Java21 + Windowsにおける文字化け対策の設定のまとめ"
source: "https://zenn.dev/leoninja/articles/10831509338169"
author:
published: 2024-07-27
created: 2026-04-30
description:
tags:
  - "clippings"
---
### Java 21 + Windows における文字化け対策の要約
Windows環境でJava 21を利用する際、UTF-8への統一とコンソール出力の文字化けを防ぐための設定手順です。

### 主要な対策ポイント
- **実行環境の共通設定**: `chcp 65001` コマンドを使用して、バッチ実行時のコンソール出力をUTF-8化する（`gradlew.bat` や `mvnw.cmd` に追記）。
- **JVM引数**: `-Dfile.encoding=UTF-8` を各ツールに設定する。

### ツール別の設定要点
- **Gradle**
  - `gradle.properties`: `org.gradle.jvmargs=-Dfile.encoding=UTF-8` を追加。
  - `build.gradle.kts`: `JavaExec`, `JavaCompile`, `test` 等のタスクにエンコーディング設定を追加。
- **Maven**
  - `.mvn/jvm.config`: `-Dfile.encoding=UTF-8` を指定。
  - `pom.xml`: `maven-surefire-plugin` の `argLine` にエンコーディング設定を追加。
- **IDE**
  - **IntelliJ IDEA**: VMカスタムオプションに `-Dfile.encoding=UTF-8` を設定。
  - **Eclipse**: `eclipse.ini` に `-Dfile.encoding=UTF-8` を追記。
