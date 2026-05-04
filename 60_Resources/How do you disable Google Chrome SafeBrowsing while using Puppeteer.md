---
title: "How do you disable Google Chrome SafeBrowsing while using Puppeteer?"
source: "https://stackoverflow.com/questions/78124291/how-do-you-disable-google-chrome-safebrowsing-while-using-puppeteer"
author:
  - "[[Crazy Redd 61911 gold badge88 silver badges2525 bronze badges]]"
  - "[[ggorlen – ggorlen]]"
  - "[[Crazy Redd – Crazy Redd]]"
  - "[[Saurabh Gupta Saurabh Gupta Over a year ago]]"
  - "[[Raj Omer Mustafa 16911 gold badge11 silver badge66 bronze badges]]"
  - "[[a hmed.gamer_1_ 133 bronze badges]]"
  - "[[user26506696 1]]"
  - "[[Crazy Redd Crazy Redd Over a year ago]]"
  - "[[LitileXueZha 65699 silver badges1111 bronze badges]]"
published: 2024-03-08
created: 2026-05-01
description: "I've been using Puppeteer to automate user journeys through various web portals and one of the things I've run into is the constant popups caused by using bad credentials. In this case, the browser..."
tags:
  - "clippings"
---
### 内容の要約
Puppeteerを使用して自動化を行う際、Google Chromeの「SafeBrowsing（セーフブラウジング）」機能やパスワード流出通知がポップアップし、スクリプトの実行を阻害する問題への解決策を議論したトピックです。

### 要点まとめ
- **問題の背景**: ログイン時に特定のパスワードを使用すると、ブラウザがデータ流出警告ダイアログを表示し、スクリプトが停止・失敗する。
- **主な解決策**:
  - **`puppeteer-extra`の活用**: `puppeteer-extra-plugin-user-preferences`プラグインを使用して、`safebrowsing.enabled`や`enhanced`を`false`に設定する。
  - **コマンドライン引数の追加**: `args`に`--disable-features=SafeBrowsing`や`--suppress-message-center-popups`などのフラグを追加してポップアップを抑制する。
  - **外部設定**: システム上のChromeパスを明示的に指定し、適切な権限で起動させることで動作が安定する場合がある。
- **注意点**: 以前有効だった手法がブラウザの更新により効かなくなる場合があるため、複数の引数やプラグインの組み合わせを試す必要がある。
