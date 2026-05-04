---
title: "PyAutoGUIの使い方～Pythonで画面操作を自動化する方法～ | 挑戦！プログラミングブログ"
source: "https://challenge-pg.com/2023/02/25/pyautogui/"
author:
published: 2023-11-13
created: 2026-04-30
description: "作業の自動化に役立つライブラリ「PyAutoGUI」の使い方をサンプル付きで解説します。"
tags:
  - "clippings"
---
### PyAutoGUIによる自動化の要点
PyAutoGUIは、Pythonを用いてマウス操作やキーボード入力を自動化するための強力なライブラリです。

#### 1. 準備とインストール
- `pyautogui`をインストール。
- 日本語入力には`pyperclip`、スクリーンショットには`pillow`が必要。
- コマンド例: `python -m pip install pyautogui pyperclip pillow`

#### 2. マウス操作
- **クリック系**: `leftClick()`, `rightClick()`, `doubleClick()`で特定座標をクリック可能。
- **ドラッグ**: `mouseDown()`と`mouseUp()`、または`drag()`で操作可能。
- **画像認識**: `locateCenterOnScreen()`で画面上の画像位置を検出し、クリック可能。

#### 3. キーボード操作
- **基本操作**: `press()`で単一キー、`hotkey()`で修飾キー（Ctrl, Alt等）を組み合わせた入力が可能。
- **注意点**: `ctrl + alt + delete`などは操作不可。

#### 4. 日本語入力
- クリップボード経由で文字列を貼り付ける方法（`pyperclip.copy` + `hotkey('ctrl', 'v')`）が一般的。

#### 5. 便利機能
- **待機**: `sleep()`で処理間隔を調整可能。
- **画面取得**: `screenshot()`で画像として保存。
- **安全装置**: `fail-safe機能`（マウスを画面四隅に動かすと強制終了）でプログラムの暴走を防止可能。
- **確認**: `countdown()`で実行前に猶予期間を設けることが可能。
