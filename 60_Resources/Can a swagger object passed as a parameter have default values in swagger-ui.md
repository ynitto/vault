---
title: "Can a swagger object passed as a parameter have default values in swagger-ui?"
source: "https://stackoverflow.com/questions/45852383/can-a-swagger-object-passed-as-a-parameter-have-default-values-in-swagger-ui"
author:
  - "[[intotecho 5]]"
  - "[[81433 gold badges4747 silver badges6868 bronze badges]]"
  - "[[Helen 100k1919 gold badges284284 silver badges356356 bronze badges]]"
  - "[[Mateusz Kaleta Mateusz Kaleta Over a year ago]]"
  - "[[spacether 2]]"
  - "[[86122 gold badges3131 silver badges4646 bronze badges]]"
  - "[[PAA PAA Over a year ago]]"
published: 2017-08-24
created: 2026-04-30
description: "I define a path that takes MyObject as a parameter.MyObject has properties for cats and dogs. These have default values.In swagger-editor, the example doesn't show the default values, but try-it-..."
tags:
  - "clippings"
---
### Swagger UIでデフォルト値を表示する方法

Swagger UIでオブジェクトパラメータのデフォルト値を表示・反映させるための解決策は以下の通りです。

#### 解決策：`example` キーワードを使用する
`default` キーワードは主にサーバー側のバリデーションや任意項目用です。Swagger UIの画面上で「例（Example Value）」としてデフォルト値を表示させたい場合は、`example` キーワードを使用します。

**修正例:**
```yaml
properties:
  cats:
    type: number
    example: 9
  dogs:
    type: string
    example: \\"fido\\"
```

#### その他の考慮事項
- **サーバー側での補完:** `default` を設定すると、クライアントが値を送らなかった場合にサーバー側でその値が補完される挙動になります。
- **強制的な固定値:** もし特定の値を強制したい場合は、`enum` を使用して選択肢を1つに絞ることで、実質的な固定値として扱う手法もあります。
