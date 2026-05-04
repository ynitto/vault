---
title: "puppeteerのpage.evaluate内でのlogをサーバーに出力する"
source: "https://qiita.com/joryulife/items/ce2af4fc50e0e2557958"
author:
  - "[[joryulife]]"
published: 2023-01-10
created: 2026-05-01
description: "問題 puppeteerのpage.evaluate内の結果などデバッグで見たいときにそのままconsole.logを記述すると操作しているChromeのconsoleにでるだけでGUIなしではみれない。 node.jsサーバーの出力で見たい。 解決 ブラウザを作成する..."
tags:
  - "clippings"
---
### Puppeteerのデバッグログをサーバーに出力する方法

Puppeteerの `page.evaluate()` 内で実行した `console.log` は、通常ブラウザ側（Chromeのコンソール）にしか表示されません。これをNode.jsサーバー側のコンソールに出力するための解決策は以下の通りです。

#### 解決策
`puppeteer.launch()` でブラウザを起動する際、オプションに **`dumpio: true`** を指定します。

```javascript
const browser = await puppeteer.launch({
    headless: true,
    dumpio: true, // ブラウザの出力をNode.jsプロセスに転送
    args: ['--lang=ja']
});
```

#### ポイント
- **効果**: ブラウザ上でのコンソール出力が、Node.jsの標準出力へ転送されます。
- **利点**: GUIのないヘッドレス環境でも、ブラウザ内部のデバッグ情報をターミナルで確認できるようになります。
