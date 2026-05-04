---
title: "Radix UIがよさそう"
source: "https://zenn.dev/ynakamura/articles/d30ee1cb6f3a15"
author:
published: 2021-09-13
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 概要
Radix UIは、スタイルを持たない「Headless UI」ライブラリです。UIの「振る舞い」と「アクセシビリティ」を担保しつつ、スタイリングを完全に開発者に委ねることで、自由度の高いデザインシステム構築を可能にします。

### 要点
- **Headless UIの利点**
  - スタイリングライブラリ（Tailwind, styled-components等）に依存せず、自由なデザインが可能。
  - 複雑なアクセシビリティ（a11y）やインタラクションの挙動をライブラリ側に任せ、開発の本質的な機能実装に集中できる。
- **Chakra UIとの違い**
  - **Chakra UI**: スタイルやプリセットが組み込まれた包括的なデザインシステム。
  - **Radix UI**: より抽象度が高いプリミティブなコンポーネント群。自由にスタイルを当てたい場合に最適。
- **信頼性と将来性**
  - メンテナンス体制が整っており、今後のUI開発のスタンダードになり得る技術として注目されている。
  - shadcn/uiのように、Radixを基盤とした高品質なUIライブラリも登場している。