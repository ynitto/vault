---
title: "Codex の承認疲れを減らす常駐デスクトップアプリを Tauri + Rust + UI Automation で作る"
source: "https://qiita.com/engchina/items/78f28b4467b691c3b963"
author:
  - "[[engchina]]"
published: 2026-05-26
created: 2026-05-31
description: "アプリのPreview また、GitHubはこちらです。 先に結論 codex-approval-guard は、Codex Desktop の承認リクエストを監視し、条件に合うものだけを自動で承認・拒否・閉鎖するデスクトップ補助ツールです。 単に「Yes ボタ..."
tags:
  - "clippings"
---
### 記事の要約
本記事では、AIエージェント「Codex Desktop」の頻繁な承認リクエストによるストレスを軽減するためのデスクトップ補助ツール「codex-approval-guard」の開発・実装方法について解説しています。

### 自動化ツール開発の要点
- **開発スタック**: Tauri (Shell/Rust bridge), React (UI), Rust (Coreロジック), Windows UI Automation/Win32 API (OS操作)。
- **自動化プロセスの5段階**: 
  1. **ウィンドウ監視**: Windows UI Automationを使用してCodex関連ウィンドウのみを特定。
  2. **解析**: UIテキストからコマンド、パス、権限を抽出。
  3. **判定 (Policy Engine)**: 自動承認・拒否・閉鎖をルールに基づいて振り分け。
  4. **実行**: 安全なAPIを通じてクリックまたはウィンドウ閉鎖を実行。
  5. **監査 (Audit)**: 実行結果を安全にJSONL形式でログ出力。

### 開発における重要なこだわり
- **ユーザー操作の優先**: 直近1500ms以内にマウス等の入力がある場合は自動操作を停止する「idle guard」を搭載。
- **言語対応**: 日本語・英語・中国語等のボタン表記の揺れを吸収するマッチング処理。
- **危険回避**: Gitのコミットや追加など、誤爆のリスクがある操作はデフォルトで「拒否」または「手動確認」に設定。
- **処理の分離**: 監視と実行を切り離すことで、不具合の特定と安全性を両立。
