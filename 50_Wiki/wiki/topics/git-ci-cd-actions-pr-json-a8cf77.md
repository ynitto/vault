---
title: "【GitHub Actions】PRが来たら自動でJSONスキーマを検証する"
type: "topic"
tags:
  - "git"
  - "ci-cd"
  - "networking"
  - "node-js"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/【GitHub Actions】PRが来たら自動でJSONスキーマを検証する.md"
summary: "Pull Request時にJSONファイルの構造が規定のスキーマと一致しているか検証する、GitHub Actionsを利用したCI環境の構築手順です。"
---

# 【GitHub Actions】PRが来たら自動でJSONスキーマを検証する

## 概要

Pull Request時にJSONファイルの構造が規定のスキーマと一致しているか検証する、GitHub Actionsを利用したCI環境の構築手順です。

*発行: 2022-07-22 / [[git-ci-cd-actions-pr-json-a8cf77]]*

## 主要なトピック

- [[git]]
- [[ci-cd]]
- [[networking]]
- [[node-js]]

## 詳細

- Pull Request時にJSONファイルの構造が規定のスキーマと一致しているか検証する、GitHub Actionsを利用したCI環境の構築手順です。
- 要点まとめ
- **JSONスキーマの生成**
- [quicktype](https://app.quicktype.io/) を使用し、既存のJSONからスキーマ（schema.json）を自動生成。
- **検証環境の構築**
- `ajv-cli` をインストールし、`package.json` に検証用スクリプト `\"validate\": \"npx ajv validate -s schema.json -d target.json\"` を追加。
- **GitHub Actionsの設定**
- `.github/workflows/validate.yml` を作成。
- `pull_request`（mainブランチ対象）をトリガーに、Node.jsセットアップ、依存関係インストール、`npm run validate` を実行するフローを定義。

*発行: 2022-07-22 / [[git-ci-cd-actions-pr-json-a8cf77]]*

## 関連テーマ

- [[git]]
- [[ci-cd]]
- [[networking]]
- [[node-js]]

## 出典

- `60_Resources/【GitHub Actions】PRが来たら自動でJSONスキーマを検証する.md`
- https://zenn.dev/fus1ondev/articles/858836b41f2c80
