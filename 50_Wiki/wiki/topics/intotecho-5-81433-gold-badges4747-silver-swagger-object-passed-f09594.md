---
title: "Can a swagger object passed as a parameter have default values in swagger-ui?"
type: "topic"
tags:
  - "intotecho-5"
  - "81433-gold-badges4747-silver"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Can a swagger object passed as a parameter have default values in swagger-ui.md"
summary: "Swagger UIでオブジェクトパラメータのデフォルト値を表示・反映させるための解決策は以下の通りです。"
---

# Can a swagger object passed as a parameter have default values in swagger-ui?

## 概要

Swagger UIでオブジェクトパラメータのデフォルト値を表示・反映させるための解決策は以下の通りです。

*発行: 2017-08-24 / [[intotecho-5-81433-gold-badges4747-silver-swagger-object-passed-f09594]]*

## 主要なトピック

- [[intotecho-5]]
- [[81433-gold-badges4747-silver]]

## 詳細

- Swagger UIでオブジェクトパラメータのデフォルト値を表示・反映させるための解決策は以下の通りです。
- 解決策：`example` キーワードを使用する
- `default` キーワードは主にサーバー側のバリデーションや任意項目用です。Swagger UIの画面上で「例（Example Value）」としてデフォルト値を表示させたい場合は、`example` キーワードを使用します。
- *修正例:**
- ```yaml
- properties:
- cats:
- type: number
- example: 9

*発行: 2017-08-24 / [[intotecho-5-81433-gold-badges4747-silver-swagger-object-passed-f09594]]*

## 関連テーマ

- [[intotecho-5]]
- [[81433-gold-badges4747-silver]]

## 出典

- `60_Resources/Can a swagger object passed as a parameter have default values in swagger-ui.md`
- https://stackoverflow.com/questions/45852383/can-a-swagger-object-passed-as-a-parameter-have-default-values-in-swagger-ui
