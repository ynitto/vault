---
title: "TypeScript 5.0: new mode bundler & ESM"
source: "https://ayc0.github.io/posts/typescript-50-new-mode-bundler-esm/"
author:
published: 2023-04-11
created: 2026-05-01
description: "TypeScript 5.0 is out and introduced a new compilation option: `moduleResolution: bundler`, let’s see how we can use it"
tags:
  - "clippings"
---
### TypeScript 5.0の新機能：ESMとバンドル対応

TypeScript 5.0で導入された `allowImportingTsExtensions` と `moduleResolution: bundler` は、ESM環境やバンドルツール利用時のモジュール解決の問題を解決するための機能です。

#### 主要な変更点
- **allowImportingTsExtensions**: 
  - import文で `.ts` 拡張子の使用を許可します。
  - ただし、JavaScriptへのトランスパイル（Emit）は行えません（`noEmit` または `emitDeclarationOnly` が必須）。
- **moduleResolution: bundler**:
  - WebpackやViteなどのバンドラー環境向けの設定です。
  - 拡張子なしのインポートを許可し、バンドラーが処理することを前提とした柔軟なモジュール解決を行います。

#### 背景と解決の意義
- **ESMの制約**: ESMではファイル拡張子の明示が必須ですが、開発時のソースコードに `.js` と書く不自然さを解消します。
- **柔軟性**: バンドラーを通す開発環境において、TypeScriptの厳格なパス解決ルールを緩和し、現代的な開発体験を向上させます。