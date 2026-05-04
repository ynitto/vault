---
title: "DIコンテナの実装を理解して、軽量 DI コンテナを自作しよう"
source: "https://qiita.com/sadnessOjisan/items/d05e35e34d2d1fb7e844"
author:
  - "[[Quramy]]"
published: 2019-12-11
created: 2026-05-01
description: "なぜ DI コンテナを自作するのか 関心の分離がされているアプリケーションは変更に強く、良い設計と言えます。Dependency Injection(以下 DI) は関心の分離を実現する テクニックの 1 つとしてよく見られるパターンです。しかしクラス間の依存関係が増えれ..."
tags:
  - "clippings"
---
### 概要
この記事は、TypeScriptでDI（依存性の注入）コンテナを自作する方法を解説しています。既存のライブラリ（InversifyJSやtsyringe）の仕組みを理解した上で、decoratorとMetadata Reflection APIを用いて、必要最小限の機能を持つ軽量なDIコンテナを実装するプロセスを紹介しています。

### 要点まとめ
- **DIコンテナの役割**: クラス間の依存関係を自動的に解決し、インスタンスの生成を管理することで、設計の柔軟性を向上させる。
- **実装の鍵となる技術**:
  - **Decorator**: クラスやメソッドにメタデータを付与し、実行時にクラス情報や依存関係を取得するために使用。
  - **Reflect Metadata API**: `reflect-metadata`ライブラリを利用し、コンストラクタの引数情報（`design:paramtypes`）や、interfaceへの依存を解決するためのメタデータを操作。
- **DIコンテナの構成要素**:
  - **Register**: クラスと依存関係をMapに保存。
  - **Resolve**: 依存を再帰的に解決し、コンストラクタへ注入してインスタンスを生成。
- **Interface対応**: TypeScriptではトランスパイル後にinterface情報が消えるため、`@inject`デコレータを用いて、interfaceに対する具象クラスを明示的に紐付ける必要がある。
- **結論**: DIコンテナの基本原理を理解すればシンプルに実装可能だが、実務では機能が網羅されている`tsyringe`のような既存ライブラリの使用が推奨される。