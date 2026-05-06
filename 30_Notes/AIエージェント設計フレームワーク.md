---
created: 2026-04-19T10:05:19+09:00
source: "[[60_Resources/AIエージェント開発の新標準 ADLC を読み解く — IBM × Anthropicのガイドへの共感と、本番運用からの実践的フィードバック]]"
tags: [ナレッジ, Agent, ADLC, Design]
---

# AIエージェント設計フレームワーク

## 概要
AI エージェント開発は、単発のプロンプト改善ではなく、評価と運用を含めたライフサイクルで捉える必要がある。ADLC、Harness as Code、夜間自律運用の記事を並べると、共通して「試行錯誤を前提にした設計」が見えてくる。

## 詳細
### ADLC の軸
- 決定論的ではなく、確率論的システムとして扱う
- 事前に全部を閉じず、運用で学習する適応型として扱う
- 実装ファーストではなく、評価ファーストで考える

### 2つのループ
- **実験ループ**: プロンプト・制約・評価を高速に往復する
- **ランタイム最適化ループ**: 本番ログやズレを観測し、改善につなげる

### 補助フレーム
- Harness as Code は、コードと設計書を乖離させないための仕組みとして有効
- 自律エージェントを夜間運用するなら、入口は安定性、出口はカンバンなどの可視化を重視する
- 設計テンプレートやガードレールは、あとから追加するより最初に置いた方が効く

<!-- updated: 2026-04-19 -->
### Daily / Kanban との接続
- 日次ノートで抽出したタスクを `40_Tasks/tasks/` に分解し、Kanban へ送る流れは「入口と出口を分ける」設計と相性がよい
- 評価ファーストを実務に落とすなら、まず完了条件をタスク詳細ファイルに先書きする運用が有効

<!-- updated: 2026-05-03 -->
### 仕様優先オーケストレーター（Kiro / Bob-The-Builder）
- Kiro の仕様優先アプローチと Claude の自律実行を組み合わせた [[50_Wiki/wiki/atoms/autonomous-cli-orchestrator|自律的CLIオーケストレーター]] パターンが実装例として公開されている
- 小規模タスクはローカル、60以上のタスクはEC2並列実行へスケールアウトする設計
- モデルコスト最適化（Haiku/Sonnet/Opus の使い分け）は運用設計の一部として組み込む
- 出典: [[60_Resources/自律的Kiro CLIオーケストレーター]]

<!-- updated: 2026-05-05 -->
### モデル特性に合わせたプロンプト設計（Opus 4.7）
- Claude Opus 4.7 は adaptive thinking への一本化により、4.6 とは最適な指示の型が異なる
- **フロントローディング**: ターンごとにコストがかかるため、最初のターンに必要情報をすべて詰め込む
- **5スロットブリーフ**: Goal / Constraints / Acceptance criteria / Context / Validation の5要素で構造化
- Validation（自己検証コマンド）が最大の品質レバーとなる
- ルーティング戦略（Haiku 4.5/Sonnet 4.5 → Opus 4.7）でコストと品質を最適化
- 出典: [[60_Resources/モデルが変われば指示も変わる ─ Opus 4.7 向け Agent Skill を作った]]

### kiro-loop の設計課題（2026-05-05時点）
- コントロールペイン拡充: 矢印キー対応・コマンド履歴・非インタラクティブモード
- 分散動作の弱点: グローバルスケジューリングが未実装
- セッション管理: 自動クリア・クリーニング・ログ収集の3系統
- `terminal-launcher` による多重起動の意味づけが未整理
- `statemachine-use` との連携実例（GitLab Issue → Jenkins → Issue更新）が検証待ち

<!-- updated: 2026-05-06 -->
### Harness Engineering と長時間実行エージェント
- AI エージェントを実戦投入する際は、モデルそのものより **状態管理・障害回復・可観測性・排他制御** を担う「ハーネス」の設計が品質を決める
- `aws-samples/sample-long-running-app-harness` のように、Issue 起点の承認フロー・OIDC・プレビュー環境デプロイまで含めて自動化すると、CLI 由来の自律実行をより安全に運用できる
- `kiro-loop` でも、`no_interactive`・セッションクリーンアップ・ログ採取を先に整える方が、機能追加より壊れにくい
- 出典: [[60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた]]
- 出典: [[60_Resources/aws-samplessample-long-running-app-harness]]

<!-- updated: 2026-05-06 -->
### Plan と Tasks の間に Runtime View を置く
- `spec-kit` 系の知見では、Plan から直接 Tasks に落とすと、画面遷移・コンポーネント連携・境界の責務が抜けやすい
- `Runtime View` / 粗いシーケンス図を 1 枚挟むだけで、AI の迷走と実装漏れを同時に抑えられる
- チケット駆動では「計画 → レビュー → 実装 → 観点ベース検証」の往復を固定した方が運用に乗せやすい
- 出典: [[60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる]]
- 出典: [[60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った]]

## 関連リンク
- [[11_Weekly/2026-W16]]
- [[30_Notes/Agent Skills運用と品質管理]]

## 出典・参照
- [[60_Resources/AIエージェント開発の新標準 ADLC を読み解く — IBM × Anthropicのガイドへの共感と、本番運用からの実践的フィードバック]]
- [[60_Resources/Harness as Code — CoDD活用ガイド 2 コード → 設計書　「神頼みデプロイ」と「深夜障害連絡電話」からの解放]]
- [[60_Resources/「ハーネスが大事」の先にある、3つの設計判断｜Workato Japan]]
- [[60_Resources/コピペで使えるエージェント設計テンプレート ── agency-agentsの5原則から学ぶ「良いエージェント」の作り方]]
- [[60_Resources/Claude Code を夜間に走らせ、朝カンバンで拾う — 自走パイプラインの入口と出口]]
- [[60_Resources/Harness Engineering Meetup に参加して、AIエージェントの「ハーネス」について考えた]]
- [[60_Resources/aws-samplessample-long-running-app-harness]]
- [[60_Resources/spec-kitをもう一段ロバストにして実装抜けを防ぐ方法：Plan→Tasksの前に“粗いシーケンス”を書かせる]]
- [[60_Resources/spec-kitが合わなかったので、チケット駆動向けにちょうどいい感じのプロセスを作った]]
