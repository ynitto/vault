---
original_source: 00_Inbox/Clippings/【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点.md
copied_at: 2026-04-19T10:51:13+09:00
tags: [resource/web, aws, 2026-04]
---

---
title: "【実験あり】axios攻撃は2行で防げる｜.npmrc設定とignore-scriptsの注意点"
source: "https://zenn.dev/junko_ai/articles/721d89181b844f"
author:
published: 2026-04-05
created: 2026-04-19
description:
tags:
  - "clippings"
---
### 概要
2026年3月31日に発生した axios を悪用したサプライチェーン攻撃に対し、個人の開発環境を守るための具体的な設定方法を解説しています。

### 対策の要点
以下の設定を行うことで、攻撃の被害を未然に防ぐことが可能です。

#### 1. postinstall スクリプトの無効化
- **設定**: `npm config set ignore-scripts true`
- **効果**: 悪意のあるパッケージが自動実行するインストーラ（RATドロッパー等）の動作を遮断します。
- **注意**: スクリプトに依存するパッケージが動かなくなった場合は、必要なものだけ `npm rebuild [パッケージ名] --ignore-scripts=false` で個別に許可します。

#### 2. 公開直後のパッケージを除外
- **設定**: `npm config set min-release-age 3`
- **効果**: 公開から3日未満の新しいバージョンをインストール対象から除外することで、迅速に検知・削除される悪意あるパッケージの流入を防ぎます。
- **注意**: npm v11.10.0以降が必要です。

### さらなるセキュリティ強化
- **キャレット(^)の廃止**: `npm config set save-exact true` を設定し、意図しない自動更新を防止する。
- **自動更新の抑制**: 開発ツールの最新版への自動追従をオフにし、安定版を利用する。

※完璧な防御は不可能ですが、これらの対策を重ねることで攻撃の成功確率を大幅に下げることができます。