---
title: "spec-kit Runtime View"
type: topic
tags:
  - "spec-kit"
  - "design"
  - "testing"
  - "workflow"
  - "resource-ingest"
created: "2026-05-06"
updated: "2026-05-06"
sources:
  - ".50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる.md"
  - "60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる.md"
  - ".50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った.md"
  - "60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った.md"
summary: "Plan と Tasks の間に Runtime View を挟み、AI 実装の抜け漏れを減らす軽量な設計ステップ。"
---

# spec-kit Runtime View

## 概要

`spec-kit` 系の運用では、Plan から Tasks へ直接落とすだけでは、UI 遷移やコンポーネント連携の責務が抜けやすい。`Runtime View` はその間を埋める軽量な中間成果物である。

## 主要なトピック

- [[ai-agent]]
- [[testing]]
- [[code-review]]

## 詳細

- 粗いシーケンス図や Runtime View を 1 枚追加するだけで、AI の迷走と実装漏れを減らせる
- チケット駆動では「計画 → レビュー → 実装 → 観点ベース検証」の流れに組み込むと、軽量さと確実性のバランスが良い
- Runtime View は重い設計書ではなく、境界・主体・データの流れを押さえる最小表現に寄せるのが実用的

## 関連テーマ

- [[testing]]
- [[code-review]]
- [[claude-code]]

## 出典

- `.50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる.md`
- `60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる.md`
- `.50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/50_Wiki/wiki/topics50_Wiki/wiki/topics/60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った.md`
- `60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った.md`
