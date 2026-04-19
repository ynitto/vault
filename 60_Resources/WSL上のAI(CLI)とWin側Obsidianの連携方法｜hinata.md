---
title: WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata
source: https://note.com/hinatasatou/n/n46af3c6259eb
author:
- '[[hinata]]'
published: 2025-08-30
created: 2026-04-19
description: (注釈：作業工程だけ見たい人、区切り線まで飛ばしてください)  Obsidian、流行ってますね（今更） ちょっと時間ができたので、導入してみようと思ったのが3日前。現時点で「あ、もうこれは革命だ」って気持ちになってます。  主にCLI系ツールとのコラボによって無二のツールになりつつある気がします。今回、WSL(WSL2)側の各種AIのCLIとWindows側のObsidianを連携させることで、超快適な作業環境を手に入れたので、ご紹介いたします。  まず、自分のPC周りについてですが、基本的にはwin
  11を使っているものの、株の解析であったり、副業でやっているプログラム系業務（サー
tags:
- resource/web
- obsidian
- windows
- 2026-04
- clippings
original_source: 00_Inbox/Clippings/WSL上のAI(CLI)とWin側Obsidianの連携方法｜hinata.md
copied_at: 2026-04-19 10:51:13+09:00
---
## WSL上のAI(CLI)とWindows側Obsidianの連携方法

この記事では、WSL上のAIエージェント（CLIツール）とWindows上のObsidianを連携させ、効率的な情報管理と作業フローを実現する方法について解説しています。

### 要点

*   **目的**: WSL/Linux側からObsidianのノートを直接編集できるようにし、「Linuxでの作業・Windowsでのノート整理」の二軸運用をストレスなく行う。
*   **対象読者**: コマンド操作に慣れていない初心者。
*   **所要時間**: 5〜15分。
*   **推奨方法**: 方法B（automount方式）が安定性に優れるため推奨。

### 全体像

1.  **Obsidian Vault**: Windows上に配置（例: `C:\\Users\\...\\Obsidian\\MyNote`）。
2.  **WSLからのアクセス**: `/mnt/c/Users/.../Obsidian/MyNote` として認識。
3.  **WSL入口フォルダ**: `~/vault` を作成し、ここからObsidian Vaultにアクセスする。

### 連携方法

*   **方法A（シンボリックリンク方式）**
    *   WSLの `~/vault` からWindowsのObsidian Vaultへシンボリックリンクを作成。
    *   **メリット**: 最短、トラブルが少ない。
    *   **デメリット**: 一部のツールでリンクであることが制約になる可能性（稀）。
*   **方法B（automount方式）**
    *   WSL起動時に自動でObsidian Vaultをマウントする設定を行う。
    *   `/etc/wsl.conf` と `/etc/fstab` を設定し、WSL再起動で反映。
    *   **メリット**: 使うときだけ自動接続、パスが安定、リンクに依存しない。
    *   **デメリット**: 初期設定に手間、設定ミスで警告が出る可能性。

### Obsidian側の設定

*   Vaultの場所は従来通り。
*   WSLツールは常に `~/vault` を参照するように統一。
*   Obsidian設定で「外部の変更を監視」をオンにする。

### 日報（Daily Notes）の自動運用（参考）

*   **場所**: `/home/<あなた>/vault/Dailies/`、ファイル名 `YYYY-MM-DD.md`。
*   **機能**: テンプレート、ToDoの繰越、整列、起動時の自動生成・更新。

### トラブルシューティング

*   起動時のマウントエラー: `fstab` の設定（`noauto,x-systemd.automount`）を確認。
*   OneDriveとの競合: 同期の一時停止・再開で対応。
*   Git連携時の問題: `core.autocrlf=input`、WSL設定で権限を調整。
*   同時編集の競合: どちらか一方で編集し、同時編集は避ける。

### まとめ

*   まずは**方法A（リンク方式）**で試すのがおすすめ。
*   エージェントやサンドボックス利用時は**方法B（automount方式）**が安定。
*   これにより、Linuxでの作業とWindowsのObsidianでのノート管理がシームレスに連携する。