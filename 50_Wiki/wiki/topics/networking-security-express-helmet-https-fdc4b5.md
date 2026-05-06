---
title: "Express×Helmetでウェブセキュリティを学ぶ"
type: "topic"
tags:
  - "networking"
  - "security"
  - "qianer-fengtian"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Express×Helmetでウェブセキュリティを学ぶ.md"
summary: "Expressアプリケーションにおいて、セキュリティ対策ライブラリ「Helmet」を導入する意義と、各HTTPヘッダーが提供する具体的なセキュリティ効果を…"
---

# Express×Helmetでウェブセキュリティを学ぶ

## 概要

Expressアプリケーションにおいて、セキュリティ対策ライブラリ「Helmet」を導入する意義と、各HTTPヘッダーが提供する具体的なセキュリティ効果を学習した記録です。

*発行: 2020-11-21 / [[networking-security-express-helmet-https-fdc4b5]]*

## 主要なトピック

- [[networking]]
- [[security]]
- [[qianer-fengtian]]

## 詳細

- Expressアプリケーションにおいて、セキュリティ対策ライブラリ「Helmet」を導入する意義と、各HTTPヘッダーが提供する具体的なセキュリティ効果を学習した記録です。
- 要点まとめ
- Helmetとは
- **目的**: HTTPレスポンスヘッダーを適切に設定し、Webアプリを脆弱性から保護する。
- **注意点**: セキュリティの万能薬ではなく、XSSやクリックジャッキング対策には有効だが、CSRFやSQLインジェクション等の対策は別途必要。
- 主なセキュリティヘッダーと役割
- **Content-Security-Policy (CSP)**: 許可されたリソースのみを実行させ、XSS攻撃を軽減。
- **X-Frame-Options**: サイトの埋め込みを制限し、クリックジャッキングを防止。
- **Strict-Transport-Security (HSTS)**: HTTPS通信を強制し、中間者攻撃を防止。

*発行: 2020-11-21 / [[networking-security-express-helmet-https-fdc4b5]]*

## 関連テーマ

- [[networking]]
- [[security]]
- [[qianer-fengtian]]

## 出典

- `60_Resources/Express×Helmetでウェブセキュリティを学ぶ.md`
- https://qiita.com/qianer-fengtian/items/148602c437e1703aa764
