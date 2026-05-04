---
title: "How to implement Post-Build stage using Jenkins Pipeline plug-in?"
source: "https://stackoverflow.com/questions/36651432/how-to-implement-post-build-stage-using-jenkins-pipeline-plug-in?newreg=6b81896e863c4576bdea84053d5c103f"
author:
  - "[[luka5z 7]]"
  - "[[93577 gold badges3232 silver badges5252 bronze badges]]"
  - "[[Amedee Van Gasse – Amedee Van Gasse]]"
  - "[[Mohamed Thoufeeque 87688 silver badges1818 bronze badges]]"
  - "[[Subrat Sahoo Subrat Sahoo Over a year ago]]"
  - "[[Jason Jason Over a year ago]]"
  - "[[Mohamed Thoufeeque Mohamed Thoufeeque Over a year ago]]"
  - "[[thecoshman thecoshman Over a year ago]]"
  - "[[red888 red888 Over a year ago]]"
  - "[[Will 3]]"
published: 2016-04-16
created: 2026-05-01
description: "After reading Jenkins tutorial explaining Pipeline plug-in, it seems that plug-in should make it possible to implement Post-Build steps. However documentation is rather limited in regard to specific"
tags:
  - "clippings"
---
### 概要
Jenkins Pipelineにおける「Post-Build（ビルド後処理）」の実装方法に関する技術的な質問と、それに対するコミュニティからの回答まとめです。

### 要点
- **Declarative Pipelineの場合**
  - `post` セクションを使用するのが標準的。
  - `always`, `success`, `failure`, `unstable` などの条件で処理を分岐可能。
- **Scripted Pipelineの場合**
  - `try-catch-finally` ブロックを利用して実装する。
  - `finally` ブロックで常に実行される処理を記述可能。
- **注意点**
  - ビルド結果を明示的に制御したい場合は `currentBuild.result` を使用する。
  - Pipelineのバージョンや環境によって挙動が異なる場合があるため、状況に応じた実装が必要。