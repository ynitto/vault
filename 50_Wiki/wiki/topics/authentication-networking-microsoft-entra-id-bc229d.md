---
title: "Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform"
type: "topic"
tags:
  - "authentication"
  - "networking"
  - "cilwerner"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform.md"
summary: "Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する方法"
---

# Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform

## 概要

Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する方法

## 主要なトピック

- [[authentication]]
- [[networking]]
- [[cilwerner]]

## 詳細

- SaaS アプリケーションを複数の組織に提供するために必要な、マルチテナント化の手順は以下の通りです。
- 1. アプリケーション登録の更新
- Microsoft Entra 管理センターの「認証」ペインで、サポートされるアカウントの種類を「任意の組織のディレクトリ内のアカウント」に変更します。
- アプリ ID URI がすべてのテナントでグローバルに一意であることを確認します。
- 2. 要求エンドポイントの変更
- テナント固有のエンドポイントではなく、共通エンドポイント (`https://login.microsoftonline.com/common`) を使用するようにコードを更新し、サインイン要求を送信します。
- 3. Issuer（発行者）値の検証
- トークンの検証時に、`iss`（発行者）要求と `tid`（テナント ID）要求を照合し、複数のテナントからのトークンを正しく処理できるようにロジックを更新します。
- 4. 同意（Consent）の処理

## 関連テーマ

- [[authentication]]
- [[networking]]
- [[cilwerner]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform.md`
- https://learn.microsoft.com/ja-jp/entra/identity-platform/howto-convert-app-to-be-multi-tenant
