---
title: "【GitHub Actions】PRが来たら自動でJSONスキーマを検証する"
source: "https://zenn.dev/fus1ondev/articles/858836b41f2c80"
author:
published: 2022-07-22
created: 2026-04-30
description:
tags:
  - "clippings"
---
### JSONスキーマによるPR検証の自動化

Pull Request時にJSONファイルの構造が規定のスキーマと一致しているか検証する、GitHub Actionsを利用したCI環境の構築手順です。

### 要点まとめ

- **JSONスキーマの生成**
    - [quicktype](https://app.quicktype.io/) を使用し、既存のJSONからスキーマ（schema.json）を自動生成。
- **検証環境の構築**
    - `ajv-cli` をインストールし、`package.json` に検証用スクリプト `\"validate\": \"npx ajv validate -s schema.json -d target.json\"` を追加。
- **GitHub Actionsの設定**
    - `.github/workflows/validate.yml` を作成。
    - `pull_request`（mainブランチ対象）をトリガーに、Node.jsセットアップ、依存関係インストール、`npm run validate` を実行するフローを定義。
- **効果**
    - JSONファイルに変更があった際、スキーマ違反があればCIで検知可能になり、手動チェックのコストとヒューマンエラーを削減できる。
