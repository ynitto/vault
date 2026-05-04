---
title: "MS謹製のanything to Markdownライブラリ: markitdownを試す&PRを出してみた件"
source: "https://qiita.com/sakasegawa/items/4b55deeea9c93145c4da"
author:
  - "[[sakasegawa]]"
published: 2024-12-17
created: 2026-04-30
description: "こんにちは！逆瀬川 ( https://x.com/gyakuse ) です！ このアドベントカレンダーでは生成AIのアプリケーションを実際に作り、どのように作ればいいのか、ということをわかりやすく書いていければと思います。アプリケーションだけではなく、プロダクト開発に必要..."
tags:
  - "clippings"
---
### 記事の要約
マイクロソフトが公開した、あらゆるファイルをMarkdown形式に変換できるライブラリ「MarkItDown」の紹介と、著者による機能追加（Pull-Request）の実践記録。

### 要点まとめ
* **MarkItDownとは**
    * 多様なファイル形式（PDF, PowerPoint, Word, Excel, 画像, 音声など）をMarkdownに変換するツール。
    * LLMへのデータ入力（RAG）やGit管理での差分確認に有用。
* **利用のメリット**
    * LLMに適した形式への変換が容易。
    * シンプルな構造で、初心者でも実装やカスタマイズがしやすい。
* **著者による貢献（PRの内容）**
    * 現状のMarkItDownで非対応だった「PowerPointのチャート（グラフ）」のMarkdown化を実装し、PRを提出。
* **学べるアクション**
    * オープンソースプロジェクトへの気軽な参加（コントリビュート）の重要性。
    * 既存実装を解析し、足りない機能を補うという具体的なエンジニアリングアプローチ。
