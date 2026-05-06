---
title: "OpenID ConnectのJWTとJWKを手軽につくりたい"
type: "topic"
tags:
  - "takahikokawasaki"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/OpenID ConnectのJWTとJWKを手軽につくりたい.md"
summary: "OpenID ConnectのJWT（IDトークン）とJWKを、値を変更しながら手軽に生成するためのシェルスクリプトを紹介する技術記事です。"
---

# OpenID ConnectのJWTとJWKを手軽につくりたい

## 概要

OpenID ConnectのJWT（IDトークン）とJWKを、値を変更しながら手軽に生成するためのシェルスクリプトを紹介する技術記事です。

*発行: 2019-07-25 / [[takahikokawasaki-openid-connect-jwt-jwk-f987e8]]*

## 主要なトピック

- [[takahikokawasaki]]

## 詳細

- OpenID ConnectのJWT（IDトークン）とJWKを、値を変更しながら手軽に生成するためのシェルスクリプトを紹介する技術記事です。
- 要点
- **必要なツール**
- `openssl` (鍵生成・署名用)
- `nodejs` & `pem-jwk` (PEMからJWKへの変換用)
- `jq` (JSON整形用)
- **主な処理フロー**
- 1. `openssl`でRSA秘密鍵・公開鍵を生成。
- 2. ヘッダ・ペイロードをBase64エンコードし、秘密鍵で署名を作成してJWTを生成。

*発行: 2019-07-25 / [[takahikokawasaki-openid-connect-jwt-jwk-f987e8]]*

## 関連テーマ

- [[takahikokawasaki]]

## 出典

- `../60_Resources/OpenID ConnectのJWTとJWKを手軽につくりたい.md`
- https://qiita.com/shu-yusa/items/36855cf1e9b4ec2adf28
