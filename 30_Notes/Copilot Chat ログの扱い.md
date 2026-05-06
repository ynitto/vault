---
created: 2026-05-05T21:31:17+09:00
source_tool: copilot
tags: [notes/experience, copilot, logging, vscode]
---

# Copilot Chat ログの扱い

## 概要
VS Code の `GitHub Copilot Chat.log` は会話本文よりも、モデル呼び出し・接続状態・ワークスペース解決失敗などの運用ログとして読む方が有効だった。

## ポジティブな学び
会話本文は薄くても、実行基盤の観察には十分使える。

- **モデル利用状況の痕跡は追える**: `gpt-5.3-codex` の `panel/editAgent`、`gpt-4o-mini` の `healApplyPatch` など、どの系統の処理が走ったかをログから把握できた。
- **MCP/接続系の不調はすぐ見える**: `net::ERR_ADDRESS_UNREACHABLE`、`No repository properties found`、`enumDescriptions` スキーマ警告など、会話本文がなくても障害切り分け材料は得られる。
- **ウィンドウ単位で切れば保全しやすい**: 同一日付でも `window1` / `window2` に分けることで、少なくとも実行単位のログ断片として保存しやすくなった。

## ネガティブな学び（失敗・回り道）
経験学習の元データとしては粒度が粗い。

- **ユーザーとアシスタントの往復本文が残らない**: 何を質問し、なぜ解決したかの抽出には向かず、学びの中心をここに置くと内容が薄くなる。
- **1ファイルに複数リクエストが混在する**: セッション境界が明示されず、日次・ウィンドウ単位の運用ログとして扱うしかない。

## 結論・決定事項
Copilot Chat.log は「経験ノートの主資料」ではなく「運用トラブルの証跡」として使う。会話内容レベルの学習が必要な場合は、別の明示的なエクスポート手段が必要。

## 次のアクション
Copilot の経験取り込みでは会話本文の自動収集を期待しすぎず、ログからはモデル・接続・ツール実行の失敗傾向だけを拾う。

<!-- updated: 2026-05-06 -->
## 追加で見えた失敗パターン
- `2026-05-06` の取り込みログでは、`ERR_ADDRESS_UNREACHABLE` / `ENOTFOUND api.github.com` によりトークン取得や session 一覧取得が連鎖的に失敗していた
- つまり Copilot の運用ログは「本文の代替」ではなく、**認証・ネットワーク・MCP 起動状態のヘルスチェック**として読むのが正しい
- 外部取得系の検証では、成功したはずの処理でも「接続失敗時に何を根拠に成功と判断したか」を別途確かめる必要がある
- 出典: [[60_Resources/Logs/copilot-2026-05-06-cae269c6]]
- 出典: [[60_Resources/Logs/copilot-2026-05-05-6aeba88b]]

## 出典・参照
- [[60_Resources/2026-05-05-copilot-session-20260505t194454-window1.md]]
- [[60_Resources/2026-05-05-copilot-session-20260505t194454-window2.md]]
- [[60_Resources/2026-05-02-copilot-session-20260502t045136-window2.md]]
- [[60_Resources/Logs/copilot-2026-05-06-cae269c6]]
- [[60_Resources/Logs/copilot-2026-05-05-6aeba88b]]

## 長期記憶
<!-- ltm-saved: 2026-05-05T22:05:00+09:00 -->
- 保存済み（ltm-use）
