---
title: "Use the Redoc CE HTML element"
source: "https://redocly.com/docs/redoc/deployment/html"
author:
published: 2026-01-15
created: 2026-05-01
description: "OpenAPI-generated documentation tool with 24k+ stars on Github - make APIs your company's superpower."
tags:
  - "clippings"
---
### Redoc CEのHTMLへの導入方法

Redoc CEをWebページに組み込み、APIドキュメントをレンダリングするためのガイドラインです。

#### 主な導入ステップ
- **HTMLテンプレートの活用**: 提供された標準HTMLテンプレートを使用し、`spec-url`にAPI仕様書（YAML/JSON）のパスまたはURLを指定します。
- **ローカル環境**: 相対パスを使用する場合は、動作確認のためにローカルHTTPサーバーが必要です。

#### 設定とカスタマイズ
- **属性指定**: HTMLタグにプロパティを追加することで、表示設定（例：必須項目の表示順序など）を調整可能です。
- **テーマ設定**: `theme`属性を使用して、サイドバーの色など詳細なデザインをJSON形式でカスタマイズできます。

#### 高度な実装方法
- **Redoc.initオブジェクト**: JavaScript経由で動的にドキュメントを初期化できます。特定のDOM要素（`<div>`など）への埋め込みや、レンダリング後のコールバック処理が可能です。
- **セルフホスト**: CDNを利用するほか、依存関係をローカル（node_modules）にインストールしてオフライン環境などでホストすることも可能です。