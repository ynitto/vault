---
title: "OpenID ConnectのJWTとJWKを手軽につくりたい"
source: "https://qiita.com/shu-yusa/items/36855cf1e9b4ec2adf28"
author:
  - "[[TakahikoKawasaki]]"
published: 2019-07-25
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 概要
OpenID ConnectのJWT（IDトークン）とJWKを、値を変更しながら手軽に生成するためのシェルスクリプトを紹介する技術記事です。

### 要点
* **必要なツール**
  * `openssl` (鍵生成・署名用)
  * `nodejs` & `pem-jwk` (PEMからJWKへの変換用)
  * `jq` (JSON整形用)

* **主な処理フロー**
  1. `openssl`でRSA秘密鍵・公開鍵を生成。
  2. ヘッダ・ペイロードをBase64エンコードし、秘密鍵で署名を作成してJWTを生成。
  3. `pem-jwk`を使用して公開鍵をJWK形式に変換。
  4. `jq`でJWKに公開鍵のメタデータを付与して整える。

* **活用シーン**
  * IDトークンの検証テスト（iss, exp, aud等の各クレームを変更して検証エラーを再現するなど）