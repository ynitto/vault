---
title: "XStateで状態遷移を共通言語にしよう"
source: "https://qiita.com/nsyee/items/9e67485c7af785ffd087"
author:
  - "[[nsyee]]"
published: 2019-12-25
created: 2026-05-01
description: "Poll: do you use finite state machines for UI design/development?— David K. 🎹 (@DavidKPiano) June 30, 2017 オブジェクトベースのUIモデリングが注目されることに..."
tags:
  - "clippings"
---
### 内容の要約
この記事では、UI設計における「状態遷移」の重要性を説き、JavaScriptライブラリ「XState」を活用したモデルの可視化と設計手法について解説しています。

### 要点まとめ
- **静的構造と動的振る舞いの両立**
  - UI設計では静的な構造（UIクラス図等）だけでなく、「時間」や「イベント」を含む動的な状態変化のモデリングが不可欠。
- **XStateの活用**
  - 状態遷移をJSON形式で定義・実行できるライブラリ。
  - アクション、条件分岐、階層化、直交性、履歴保持などの高度な状態表現をサポート。
  - フレームワークに依存せず、ReactやVueなどとも容易に連携可能。
- **XState Visualizerによる可視化**
  - 定義した状態遷移図をリアルタイムで可視化・インタラクティブに操作可能。
  - 実装前にプロトタイプとして振る舞いを検証でき、仕様の曖昧さを早期に排除可能。
- **チームでの共通言語化**
  - 思考を外部化（可視化）することで、職種を越えた議論が促進され、開発チーム全体の共通認識を形成できる。