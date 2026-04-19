---
created: 2026-04-19T10:05:19+09:00
source: 00_Inbox/Clippings/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md
tags: [ナレッジ, LLM, Memory, PKM]
---

# LLM長期記憶と第二の脳

## 概要
長期記憶の実装は「検索機能を足す」より、「人が読めて更新できる知識層を育てる」方向が強い。Inbox の記事群では、第二の脳、LLM Wiki、Copilot Memory、CLAUDE.md がそれぞれ別の角度から同じ課題を解いていた。

## 詳細
### 記憶の分離
- **raw source**: クリッピングやログのような元資料
- **wiki / brain**: 再利用しやすい要約・概念・関係性の層
- **project / how**: その場の実装や実行手順

### 重要な考え方
- RAG 的に毎回生資料を掘るより、一度要約・編集した知識層を持つ方が精度と継続性が上がる
- CLAUDE.md のような役割定義ファイルは、知識そのものより「どう考えるか」を揃えるために効く
- 長期記憶は最初から完全自動にせず、段階的に権限を広げていく方が安全

### 運用メモ
- 生データは捨てずに残し、ナレッジ層で再構成する
- query 結果を何でも保存せず、再利用価値があるものだけ残す
- brain / project の境界が曖昧になると、知識ノートがすぐに腐る

## 関連リンク
- [[10_Daily/2026-04-19]]
- [[30_Notes/ObsidianとAIエージェント連携]]

## 出典・参照
- `00_Inbox/Clippings/Claude Codeで「第二の脳」を作り、最終的にAIが自律運用するようになった話.md`
- `00_Inbox/Clippings/LLMに長期記憶を実装する.md`
- `00_Inbox/Clippings/Karpathy 氏が言語化した「LLM Knowledge Base」というパターン.md`
- `00_Inbox/Clippings/【LLM Wiki】Obsidian x Claude Codeで学んだ知識を構造化し記憶媒体を脳からAIに移行する.md`
- `00_Inbox/Clippings/GitHub Copilot は自ら学ぶ Copilot Memory 入門.md`
- `00_Inbox/Clippings/Boris Cherny氏の知見を元に作成された、CLAUDE.mdを理解する.md`
