---
title: "TypeScript 5.0: new mode bundler & ESM"
type: "topic"
tags:
  - "javascript"
  - "typescript"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/TypeScript 5.0 new mode bundler & ESM.md"
summary: "TypeScript 5.0の新機能：ESMとバンドル対応"
---

# TypeScript 5.0: new mode bundler & ESM

## 概要

TypeScript 5.0の新機能：ESMとバンドル対応

*発行: 2023-04-11 / [[javascript-typescript-typescript-5-0-mode-42a627]]*

## 主要なトピック

- [[javascript]]
- [[typescript]]

## 詳細

- TypeScript 5.0で導入された `allowImportingTsExtensions` と `moduleResolution: bundler` は、ESM環境やバンドルツール利用時のモジュール解決の問題を解決するための機能です。
- 主要な変更点
- **allowImportingTsExtensions**:
- import文で `.ts` 拡張子の使用を許可します。
- ただし、JavaScriptへのトランスパイル（Emit）は行えません（`noEmit` または `emitDeclarationOnly` が必須）。
- **moduleResolution: bundler**:
- WebpackやViteなどのバンドラー環境向けの設定です。
- 拡張子なしのインポートを許可し、バンドラーが処理することを前提とした柔軟なモジュール解決を行います。
- 背景と解決の意義

*発行: 2023-04-11 / [[javascript-typescript-typescript-5-0-mode-42a627]]*

## 関連テーマ

- [[javascript]]
- [[typescript]]

## 出典

- `60_Resources/TypeScript 5.0 new mode bundler & ESM.md`
- https://ayc0.github.io/posts/typescript-50-new-mode-bundler-esm/
