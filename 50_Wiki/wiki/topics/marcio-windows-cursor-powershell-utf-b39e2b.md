---
title: "Windows＋CursorでPowerShellの文字化けを一掃する手順（UTF‑8化・PowerShell 7・設定まとめ）"
type: "topic"
tags:
  - "marcio"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Windows＋CursorでPowerShellの文字化けを一掃する手順（UTF‑8化・PowerShell 7・設定まとめ）.md"
summary: "WindowsとCursor（VSCode系）環境において、PowerShell実行時の日本語文字化けを解消するための手順です。旧版PowerShell…"
---

# Windows＋CursorでPowerShellの文字化けを一掃する手順（UTF‑8化・PowerShell 7・設定まとめ）

## 概要

WindowsとCursor（VSCode系）環境において、PowerShell実行時の日本語文字化けを解消するための手順です。旧版PowerShell 5.1（Shift_JIS）からPowerShell 7（UTF-8）へ移行し、環境全体をUTF-8に統一・固定することで根本解決を図ります。

*発行: 2025-10-28 / [[marcio-windows-cursor-powershell-utf-b39e2b]]*

## 主要なトピック

- [[marcio]]

## 詳細

- WindowsとCursor（VSCode系）環境において、PowerShell実行時の日本語文字化けを解消するための手順です。旧版PowerShell 5.1（Shift_JIS）からPowerShell 7（UTF-8）へ移行し、環境全体をUTF-8に統一・固定することで根本解決を図ります。
- 要点
- **PowerShell 7のインストール**
- `winget install --id Microsoft.PowerShell -e` を実行。
- **UTF-8への固定設定**
- `$PROFILE` に以下を追記し、標準入出力をUTF-8に固定する：
- `[Console]::InputEncoding = [System.Text.Encoding]::UTF8`
- `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`
- `$OutputEncoding = [System.Text.Encoding]::UTF8`

*発行: 2025-10-28 / [[marcio-windows-cursor-powershell-utf-b39e2b]]*

## 関連テーマ

- [[marcio]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Windows＋CursorでPowerShellの文字化けを一掃する手順（UTF‑8化・PowerShell 7・設定まとめ）.md`
- https://qiita.com/marcio/items/87c15f852ba7aecfb71a
