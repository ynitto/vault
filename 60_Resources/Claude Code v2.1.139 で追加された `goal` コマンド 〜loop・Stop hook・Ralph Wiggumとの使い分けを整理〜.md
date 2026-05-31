---
title: "Claude Code v2.1.139 で追加された `/goal` コマンド 〜/loop・Stop hook・Ralph Wiggumとの使い分けを整理〜"
source: "https://dev.classmethod.jp/articles/claude-code-goal-command/"
author:
  - "[[田中 雄一郎]]"
published: 2026-05-15
created: 2026-05-16
description:
tags:
  - "clippings"
---
### Claude Codeの新機能「/goal」の要約
Claude Code v2.1.139で導入された`/goal`コマンドは、**設定した完了条件をHaikuモデルがターンごとに自動判定し、条件達成時に自動停止する**自律実行機能です。

### 要点まとめ

- **`/goal`の仕組み**
    - 実行ターン終了のたびにHaikuが判定を実施。
    - 達成＝自動停止、未達成＝継続。
    - 判定コストはメインモデルと比較して非常に低いです。

- **自律実行アプローチの使い分け**
    - **/goal**: テスト通過など、完了条件が明確なタスク向け（最も効率的）。
    - **/loop**: 指定時間ごとの定期実行（ポーリングなど）。
    - **Stop hook**: 独自の終了条件をスクリプト等で制御したい場合。
    - **Ralph Wiggum**: 完了条件が定義しにくい場合（トークン消費が激しくRate Limitに注意）。

- **効果的な使い方**
    - **書き方**: 「何がどうなれば完了か」だけでなく、「確認コマンド（git status等）」を含めると精度向上。
    - **安全策**: 無限ループを防ぐため、条件内に「〇〇ターン経過で終了」といった上限を含めることが推奨されます。

- **基本操作**
    - 設定: `/goal [条件]`
    - 確認: `/goal`
    - 停止: `/goal clear`
