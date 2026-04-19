---
original_source: 00_Inbox/Clippings/Amazon Q(Kiro)CLIを起動するとターミナルが激重になるのを解消した話.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, ai-agent, 2026-04]
---

---
title: "Amazon Q(Kiro)CLIを起動するとターミナルが激重になるのを解消した話"
source: "https://qiita.com/masaozi3/items/53b98ea386397ec1ed8f"
author:
  - "[[masaozi3]]"
published: 2025-12-26
created: 2026-04-19
description: "環境 macOS 15.5 mise 2025.9.23 本題 起きたこと 気がつくとターミナルのウィンドウを立ち上げて使用できるようになるまで30秒位かかっていました。 そしてターミナルが急に落ちることもしばしば起きていました。 そんなにメモリやCPUを使いまくる..."
tags:
  - "clippings"
---
### 内容の要約
Amazon Q CLI起動時にターミナルが非常に重くなり、クラッシュする問題が発生。原因は、`mise`のPython環境設定が不完全で、shimが無限ループしていたことでした。`mise`で正しいPythonバージョンをインストール・設定することで解決しました。

### 重要なポイント
- **現象**: ターミナルの起動が極端に遅く、頻繁にクラッシュする。
- **原因**: 
    - `mise`でPythonがインストールされていないにもかかわらず、shimパスが参照されていた。
    - 不正な設定により、`mise/shims/python3`プロセスが無限に生成されCPUを圧迫。
- **解決策**:
    - 該当プロセスの強制終了 (`kill`)。
    - `mise install python@<version>` で適切に環境をインストール。
    - `mise use -g python@<version>` でグローバル設定を適用。
- **学べること**: `mise/shims`は指定したバージョンの実行ファイルを動的に切り替える仕組みのため、依存関係の解決が重要である。