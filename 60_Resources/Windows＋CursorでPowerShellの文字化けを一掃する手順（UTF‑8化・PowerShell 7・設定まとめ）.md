---
title: "Windows＋CursorでPowerShellの文字化けを一掃する手順（UTF‑8化・PowerShell 7・設定まとめ）"
source: "https://qiita.com/marcio/items/87c15f852ba7aecfb71a"
author:
  - "[[marcio]]"
published: 2025-10-28
created: 2026-04-30
description: "対象: Windows 10/11 + Cursor（VSCode系）を使っていて、PowerShell実行時に日本語が文字化けする人向け。 ゴール: Cursor の統合ターミナルで PowerShell 7（UTF‑8） を既定で起動し、出力・ファイル入出力・外部コマ..."
tags:
  - "clippings"
---
### 要約
WindowsとCursor（VSCode系）環境において、PowerShell実行時の日本語文字化けを解消するための手順です。旧版PowerShell 5.1（Shift_JIS）からPowerShell 7（UTF-8）へ移行し、環境全体をUTF-8に統一・固定することで根本解決を図ります。

### 要点
- **PowerShell 7のインストール**
  - `winget install --id Microsoft.PowerShell -e` を実行。
- **UTF-8への固定設定**
  - `$PROFILE` に以下を追記し、標準入出力をUTF-8に固定する：
    - `[Console]::InputEncoding = [System.Text.Encoding]::UTF8`
    - `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`
    - `$OutputEncoding = [System.Text.Encoding]::UTF8`
- **Cursorの設定変更**
  - 設定画面の「Terminal › Integrated › Default Profile: Windows」を「PowerShell（PowerShell 7）」に変更。
  - 反映されない場合は `settings.json` に `pwsh.exe` のパスを明示する。
- **動作確認**
  - `$PSVersionTable.PSVersion` で7系であることを確認。
  - ファイル入出力テストで文字化けがないことを検証。
