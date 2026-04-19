---
original_source: 00_Inbox/Clippings/GitHub Copilot は自ら学ぶ Copilot Memory 入門.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, git, 2026-04]
---

---
title: "GitHub Copilot は自ら学ぶ: Copilot Memory 入門"
source: "https://zenn.dev/microsoft/articles/50863342150992"
author:
published: 2026-04-05
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 記事の要約
GitHub Copilotがセッションを跨いで学習・記憶する「メモリ機能」の全体像と仕組みを解説する連載の第1回。メモリの分類（保存場所・共有範囲）を整理し、特にGitHubクラウド上に保存される「Copilot Memory」の重要性と技術的特性（リアルタイム検証機能など）について詳説しています。

### 要点まとめ

#### 1. メモリ機能の全体マップ
- **保存場所**: ローカル保存型（各環境依存）とクラウド保存型（GitHub CAPI経由）の2種類。
- **共有範囲**: ユーザー単位、リポジトリ単位、チャットセッション単位の3階層。

#### 2. Copilot Memory（クラウド保存型）
- **リポジトリスコープ**: チームで共有可能な唯一のメモリ。
- **Just-in-time Verification**: `citations`（根拠となるコード場所）を保存し、使用時に現在のコードベースと一致するかリアルタイム検証するため、情報の陳腐化を防げる。
- **寿命と延命**: 未使用期間が28日を超えると自動削除されるが、使用されるたびに寿命がリセットされる。
- **適用範囲**: 全実行環境（VS Code, CLI, Cloud Agent等）で知識のクロス共有が可能。

#### 3. ローカル保存型メモリ
- **VS Code**: User/Repository/Sessionの3種類のメモリ領域を持ち、仮想ファイルシステムを通じて操作。
- **Copilot CLI**: SQLiteを用いた永続的な作業ログとして機能。

#### 4. 注意点
- **権限**: Copilot Memoryの作成はWrite権限が必要。
- **共有**: 保存された情報はリポジトリの全コントリビューターと共有されるため、個人の好みを保存する際は注意が必要。