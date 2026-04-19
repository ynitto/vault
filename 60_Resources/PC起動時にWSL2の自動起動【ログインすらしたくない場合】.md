---
original_source: 00_Inbox/Clippings/PC起動時にWSL2の自動起動【ログインすらしたくない場合】.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, windows, 2026-04]
---

---
title: "PC起動時にWSL2の自動起動【ログインすらしたくない場合】"
source: "https://zenn.dev/shishimaruwo/articles/f106b12896e2ba"
author:
published: 2024-01-27
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
Windows PCの電源ONのみでWSL2を起動し、ログインなしで外部からSSH接続できるようにするための設定手順のまとめです。

### 要点
- **WSLの自動起動**
  - タスクスケジューラを使い、システム起動時に `C:\\Program Files\\WSL\\wsl.exe` を実行するように設定。
- **SSHサーバーの構築**
  - WSL内に `openssh-server` をインストールし有効化。
- **通信設定**
  - Windows側で `netsh interface portproxy` を使用し、Windowsの22番ポートへのアクセスをWSLに転送。
  - Windowsファイアウォールで22番ポートのインバウンド/アウトバウンドを許可。
- **PCの常時稼働設定**
  - カバーを閉じた際の動作を「何もしない」に設定。
  - 電源オプションにて、電源接続時のスリープを「適用しない」に設定。