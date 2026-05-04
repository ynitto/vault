---
title: "Express×Helmetでウェブセキュリティを学ぶ"
source: "https://qiita.com/qianer-fengtian/items/148602c437e1703aa764"
author:
  - "[[qianer-fengtian]]"
published: 2020-11-21
created: 2026-05-01
description: "この記事は エニプラ Advent Calendar 2020 の 11 日目の記事です。 はじめに Express 公式の『実稼働環境における Express のセキュリティーに関するベスト・プラクティス』というドキュメントでは、「脆弱性対策のために Helmet を使..."
tags:
  - "clippings"
---
### 記事の概要
Expressアプリケーションにおいて、セキュリティ対策ライブラリ「Helmet」を導入する意義と、各HTTPヘッダーが提供する具体的なセキュリティ効果を学習した記録です。

### 要点まとめ

#### Helmetとは
- **目的**: HTTPレスポンスヘッダーを適切に設定し、Webアプリを脆弱性から保護する。
- **注意点**: セキュリティの万能薬ではなく、XSSやクリックジャッキング対策には有効だが、CSRFやSQLインジェクション等の対策は別途必要。

#### 主なセキュリティヘッダーと役割
- **Content-Security-Policy (CSP)**: 許可されたリソースのみを実行させ、XSS攻撃を軽減。
- **X-Frame-Options**: サイトの埋め込みを制限し、クリックジャッキングを防止。
- **Strict-Transport-Security (HSTS)**: HTTPS通信を強制し、中間者攻撃を防止。
- **X-Content-Type-Options**: MIMEタイプを固定し、不正なスニッフィングによる実行を防止。
- **Referrer-Policy**: リファラ情報の送出を制御し、情報漏洩を防止。

#### 運用上の注意
- **X-Powered-Byの削除**: フレームワーク名を隠蔽し、攻撃者に情報を与えないようにする。
- **設定の取捨選択**: すべてのヘッダーがデフォルトで万能ではないため、仕組みを理解して適切に運用することが重要。
