---
title: "Performance Test Running and Reporting for Jenkins CI"
type: "topic"
tags:
  - "testing"
  - "ci-cd"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Performance Test Running and Reporting for Jenkins CI.md"
summary: "JenkinsのPerformance Pluginは、各種パフォーマンス・負荷テストツールの結果を自動収集し、トレンドグラフの生成やビルドステータスの判…"
---

# Performance Test Running and Reporting for Jenkins CI

## 概要

JenkinsのPerformance Pluginは、各種パフォーマンス・負荷テストツールの結果を自動収集し、トレンドグラフの生成やビルドステータスの判定（成功・不安定・失敗）を行うためのツールです。

## 主要なトピック

- [[testing]]
- [[ci-cd]]

## 詳細

- JenkinsのPerformance Pluginは、各種パフォーマンス・負荷テストツールの結果を自動収集し、トレンドグラフの生成やビルドステータスの判定（成功・不安定・失敗）を行うためのツールです。
- 主な特徴
- **多様なツールに対応**: Taurus, JMeter, JUnit, Iago, wrk, LoadRunnerなどのレポート形式をサポート。
- **柔軟な判定**: エラー率や相対的なパフォーマンス変動に基づいてビルドステータスを制御可能。
- **視覚的な分析**: 複数のレポートをグラフ化し、ビルドごとの推移や詳細な履歴データをWeb上で確認可能。
- 設定方法
- **GUI設定**: ポストビルドアクションから「Publish Performance test result report」を選択し、レポートファイルのパスを指定。
- **Pipeline設定**: `perfReport`コマンドを使用。ファイル名の指定のみの簡潔な記述から、詳細な閾値設定まで対応しています。

## 関連テーマ

- [[testing]]
- [[ci-cd]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Performance Test Running and Reporting for Jenkins CI.md`
- https://jenkinsci.github.io/performance-plugin/Reporting.html
