---
title: aws-samples/sample-long-running-app-harness
source: https://github.com/aws-samples/sample-long-running-app-harness
author: null
published: null
created: 2026-05-06
description: Contribute to aws-samples/sample-long-running-app-harness development
  by creating an account on GitHub.
tags:
- clippings
- resource/web
- 2026-05
- harness
- reliability
- aws
- cloudfront
- bedrock
original_source: 00_Inbox/Clippings/aws-samplessample-long-running-app-harness.md
copied_at: '2026-05-06T07:24:46+09:00'
---

### 概要
このリポジトリは、GitHub上のIssueに基づいて全自動でフルスタックアプリケーションを構築する、AWS Bedrock AgentCoreを活用した自律型エージェントシステムです。

### 主な特徴
- **完全自動化**: GitHub Issueの起票から開発、テスト、プレビュー環境のデプロイまでを自動実行。
- **OIDC認証**: AWS IAMロールのOIDCフェデレーションを採用し、静的な認証情報を不要にすることでセキュリティを強化。
- **柔軟な構築計画**: `BUILD_PLAN.md` を作成することで、任意のプロジェクトをエージェントに構築させることが可能。
- **インフラ管理**: AWS CDKを活用し、S3やCloudFrontを用いたプレビュー環境の自動構築に対応。

### 動作フロー
1. **承認**: ユーザーがIssueにリアクションして開発を承認。
2. **ポーリング**: GitHub ActionsがIssueを検出し、Bedrock AgentCoreを呼び出し。
3. **開発**: エージェントがコードを生成し、テストを実行してコミット。
4. **デプロイ**: 自動的にプレビュー環境（CloudFront）へ反映。

### プロジェクト構造
- `prompts/`: 各プロジェクトの構築計画（`BUILD_PLAN.md`等）を格納。
- `.github/workflows/`: 自動化用のCI/CDワークフロー。
- `infrastructure/`: AWS CDKによるインフラ定義。
- `bedrock_entrypoint.py`: エージェントの実行を制御するメインオーケストレーター。
