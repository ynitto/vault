---
title: "ObsidianでZennを書く！git submoduleで一元管理"
source: "https://zenn.dev/ktr17/articles/3505fab842af79"
author:
published: 2025-11-26
created: 2026-04-19
description:
tags:
  - "clippings"
---
## ObsidianとZennの連携：git submoduleによる一元管理

この記事は、ObsidianとZennのコンテンツを一元管理したいと考えている読者向けに、`git submodule` を活用した方法を解説しています。

### はじめに

*   Obsidian用リポジトリとZenn用リポジトリを別々に管理していた。
*   Zennの記事もObsidianで執筆したいというニーズから、サブモジュール導入を検討。

### git submoduleの活用

*   `git submodule` を使うことで、親リポジトリ（Obsidian）内に子リポジトリ（Zenn）を格納できる。
*   **サブモジュールの追加方法:**
    ```bash
    cd 親リポジトリ
    git submodule add https://github.com/<子リポジトリ>.git <子リポジトリ用のフォルダパス>
    ```
*   **子リポジトリへのpush:**
    1.  子リポジトリのフォルダに移動し、`git add .` と `git commit` を実行。
    2.  `git push origin main` でプッシュ。
    3.  親リポジトリに戻り、`git add .` と `git commit`、`git push origin main` で変更を登録。
*   **サブモジュールを含めたclone:**
    ```bash
    git clone --recurse-submodules https://github.com/<親リポジトリ>
    ```

### まとめ

*   `git submodule` を利用することで、ObsidianとZennのデータを一元管理でき、メンテナンスが容易になる。
*   ObsidianでのZenn記事執筆環境を整えることを推奨。