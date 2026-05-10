---
title: "ブルシットジョブは打首獄門。WSL2×multi-agent-shogun×CDPでブラウザ作業を全自動化する傀儡の術"
source: "https://zenn.dev/shio_shoppaize/articles/wsl2-edge-cdp-automation"
author:
published: 2026-03-07
created: 2026-05-10
description:
tags:
  - "clippings"
---
### 概要
WSL2上のAIエージェントから、ホストOS（Windows）で動作するブラウザ（Edge等）を直接操作し、定型業務（ブルシットジョブ）を自動化する手法の解説です。PlaywrightやComputer Useよりも高速・低コストで、ログイン済みのセッションを活用できるのが特徴です。

### 要点まとめ
- **仕組み**: 
    - Windows側のブラウザを「デバッグモード（CDP）」で起動。
    - WSL2内のPythonスクリプトからPowerShell経由でローカルホストへ接続し、ブラウザを制御。
- **主な利点**:
    - **高速・軽量**: DOMを直接操作するため、スクショベースの操作より遥かに高速。
    - **ログイン不要**: ブラウザの既存セッションを利用するため、SaaSへの再ログインが不要。
    - **非占有**: バックグラウンドで動作するため、自動化中もPCで別作業が可能。
    - **低コスト**: シンプルなスクリプトのため、LLMのトークン消費も最小限。
- **活用例**:
    - AIエージェントと連携し「データを取ってきて」の一言で全自動化。
    - Electronアプリ（VS Code、Slack等）への応用も可能。
    - 外出先からスマホでSSH接続し、自宅PCのブラウザを遠隔操作するサーバーとして利用。
