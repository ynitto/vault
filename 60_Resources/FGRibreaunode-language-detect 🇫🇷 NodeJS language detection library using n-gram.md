---
title: "FGRibreau/node-language-detect: 🇫🇷 NodeJS language detection library using n-gram"
source: "https://github.com/FGRibreau/node-language-detect"
author:
published:
created: 2026-04-30
description: "🇫🇷 NodeJS language detection library using n-gram. Contribute to FGRibreau/node-language-detect development by creating an account on GitHub."
tags:
  - "clippings"
---
### 概要
`node-language-detect` は、Node.js向けの言語判定ライブラリです。PEAR::Text_LanguageDetectの移植版であり、52種類の言語を判定し、信頼度スコアを算出できます。

### 主な要点
- **機能**
  - 52種類の言語識別に対応。
  - 言語ごとの信頼度スコア算出機能。
  - 言語コード（ISO2/ISO3）やフルネームでの出力指定が可能。
- **インストールと利用**
  - `npm install languagedetect --save` で導入可能。
  - シンプルなAPIで、文字列を渡すだけで判定結果を取得可能。
- **パフォーマンス**
  - PHP実装と比較して高速（1000アイテムの処理で約4倍の速度）。
- **その他**
  - MITライセンスで提供。
  - 9名のコントリビューターにより開発、TypeScript定義ファイルも含む。
