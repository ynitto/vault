---
title: "コピペで学ぶチュートリアル: DockerfileのCMDとENTRYPOINTの違い"
source: "https://zenn.dev/richardimaoka/articles/bd87036acd951e"
author:
published: 2022-09-05
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 概要
Dockerの `CMD` と `ENTRYPOINT` の違いを、実際に手を動かして学べる実践的なチュートリアルです。両者の挙動の違い、`exec form` と `shell form` の使い分け、およびPID 1とシグナル処理の関係を解説しています。

### 要点まとめ

#### 1. 形式の使い分け (Exec vs Shell)
- **Exec form** (`[\\"cmd\