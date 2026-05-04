---
title: "How to implement Post-Build stage using Jenkins Pipeline plug-in?"
type: "topic"
tags:
  - "ci-cd"
  - "luka5z-7"
  - "93577-gold-badges3232-silver"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How to implement Post-Build stage using Jenkins Pipeline plug-in?.md"
summary: "Jenkins Pipelineにおける「Post-Build（ビルド後処理）」の実装方法に関する技術的な質問と、それに対するコミュニティからの回答まとめ…"
---

# How to implement Post-Build stage using Jenkins Pipeline plug-in?

## 概要

Jenkins Pipelineにおける「Post-Build（ビルド後処理）」の実装方法に関する技術的な質問と、それに対するコミュニティからの回答まとめです。

*発行: 2016-04-16 / [[ci-cd-luka5z-7-implement-post-build-stage-c5a71f]]*

## 主要なトピック

- [[ci-cd]]
- [[luka5z-7]]
- [[93577-gold-badges3232-silver]]

## 詳細

- Jenkins Pipelineにおける「Post-Build（ビルド後処理）」の実装方法に関する技術的な質問と、それに対するコミュニティからの回答まとめです。
- 要点
- **Declarative Pipelineの場合**
- `post` セクションを使用するのが標準的。
- `always`, `success`, `failure`, `unstable` などの条件で処理を分岐可能。
- **Scripted Pipelineの場合**
- `try-catch-finally` ブロックを利用して実装する。
- `finally` ブロックで常に実行される処理を記述可能。
- **注意点**

*発行: 2016-04-16 / [[ci-cd-luka5z-7-implement-post-build-stage-c5a71f]]*

## 関連テーマ

- [[ci-cd]]
- [[luka5z-7]]
- [[93577-gold-badges3232-silver]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/How to implement Post-Build stage using Jenkins Pipeline plug-in?.md`
- https://stackoverflow.com/questions/36651432/how-to-implement-post-build-stage-using-jenkins-pipeline-plug-in?newreg=6b81896e863c4576bdea84053d5c103f
