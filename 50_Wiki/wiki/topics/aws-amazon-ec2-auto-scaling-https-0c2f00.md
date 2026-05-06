---
title: "Auto Scalingの段階スケーリングポリシーについて"
type: "topic"
tags:
  - "aws"
  - "amazon-ec2"
  - "cloudwatch"
  - "observability"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Auto Scalingの段階スケーリングポリシーについて.md"
summary: "段階スケーリング（Step Scaling Policies）の概要"
---

# Auto Scalingの段階スケーリングポリシーについて

## 概要

段階スケーリング（Step Scaling Policies）の概要

*発行: 2026-05-20 / [[aws-amazon-ec2-auto-scaling-https-0c2f00]]*

## 主要なトピック

- [[aws]]
- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]

## 詳細

- AWS Auto Scalingの「段階スケーリング」機能について解説した記事です。負荷状況に応じて、追加するインスタンス台数を柔軟に制御する方法を説明しています。
- 要点まとめ
- **段階スケーリングとは**
- CloudWatchアラームの閾値に応じて、スケールするインスタンスの台数や割合を細かく設定できる機能。
- 従来の「単純な追加」とは異なり、負荷の大きさに応じた効率的なスケーリングが可能です。
- **主要なパラメータ**
- **クールダウン（Cooldown）**: インスタンス起動指示後の待ち時間。連続した起動を抑制し、安定化を促します。
- **ウォームアップ（Warmup）**: インスタンスが負荷分散可能になるまでの期間。起動中のインスタンスをメトリクスから一時的に除外し、過剰なスケールアウトを防ぎます。
- **ライフサイクルフック**: インスタンス起動直後に「待ち状態」を作り、初期設定やデータロード等の処理を実行させる仕組み。

*発行: 2026-05-20 / [[aws-amazon-ec2-auto-scaling-https-0c2f00]]*

## 関連テーマ

- [[aws]]
- [[amazon-ec2]]
- [[cloudwatch]]
- [[observability]]

## 出典

- `60_Resources/Auto Scalingの段階スケーリングポリシーについて.md`
- https://dev.classmethod.jp/articles/auto-scaling-steps/
