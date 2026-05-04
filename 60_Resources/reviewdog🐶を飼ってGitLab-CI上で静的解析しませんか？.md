---
title: "reviewdog🐶を飼ってGitLab-CI上で静的解析しませんか？"
source: "https://qiita.com/parupappa2929/items/b1071c716cfe937b2210"
author:
  - "[[parupappa2929]]"
published: 2023-04-02
created: 2026-04-30
description: "はじめに レビュワーの工数削減とヒューマンエラーを防ぎコードの品質をさらに向上させていく取り組みの一環として、自動コードレビュー（静的解析） を検討しました。 そこで、reviewdogというツールを用いて実装しようとしたのですが、 reviewdogはgithub-ac..."
tags:
  - "clippings"
---
### 概要
GitLab CI環境において、静的コード解析ツール「reviewdog」を導入し、解析結果をマージリクエスト（MR）に自動コメントさせるための手順を解説した記事です。

### 要点まとめ
* **reviewdogとは**
    * ツールで検出されたリンターの指摘を、MRの該当箇所に直接コメントとして表示するGo言語製のOSS。
* **導入の主要ステップ**
    1. **GitLabユーザー作成**: reviewdog用に専用ユーザーを作成し、APIアクセストークンを発行。
    2. **Runnerの設定**: パイプライン実行用のGitLab Runnerを登録し、タグ（reviewdog等）を付与。
    3. **`.gitlab-ci.yml`の構成**: `reviewdog`ステージを定義し、各リンター（textlint, ESLint, RuboCop）の実行コマンドを記述。
    4. **パイプライン連携**: `reviewdog`コマンドへ各リンターの結果をパイプ（`|`）で渡し、`reporter=gitlab-mr-discussion`オプションでMRにコメントさせる。
* **導入のポイント**
    * 開発用ブランチを活用し、CIコンソールでデバッグを繰り返しながら構築する。
    * 共通変数にAPIトークンを定義し、各ジョブで適切に呼び出す。
    * `allow_failure: true`を設定することで、Lintエラーが発生してもMRのマージを阻害しない運用が可能。
* **メリット**
    * レビュワーの工数削減、ヒューマンエラーの防止、コード品質の自動的な向上。
