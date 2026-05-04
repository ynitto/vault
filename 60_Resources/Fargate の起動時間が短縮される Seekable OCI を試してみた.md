---
title: "Fargate の起動時間が短縮される Seekable OCI を試してみた"
source: "https://zenn.dev/lincwell_inc/articles/test_seekable_oci"
author:
published: 2023-12-07
created: 2026-05-01
description:
tags:
  - "clippings"
---
### Seekable OCI (SOCI) による Fargate 起動高速化の検証
本記事は、AWS Fargate におけるコンテナ起動時間の短縮を目的として、SOCI インデックスの効果を検証した報告です。

#### 検証結果の要点
- **起動時間の短縮効果**:
    - ECS のタスク起動時間ベースで **48% 短縮**。
    - アプリケーションが利用可能になるまでの時間ベースで **37% 短縮**。
- **実装方法**:
    - Terraform を使用し、AWS 公式の `cfn-ecr-aws-soci-index-builder` をデプロイすることで、イメージプッシュ時に自動的にインデックスが作成される構成を採用。
- **注意点**:
    - 2024年5月現在、SOCI 利用時に `CannotPullContainerError` が発生しやすくなるケースがあるため、バッチ処理など頻繁なタスク起動を行う環境では注意が必要。
    - インデックス作成にはプッシュ後 1〜6 分程度のラグが生じる可能性がある。
- **結論**:
    - デプロイフローの大幅な変更なしに高い短縮効果が得られるため、導入は非常に有効。