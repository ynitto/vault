---
title: "AI-DLC とは何か ― AWS Labs が公開した「承認ゲート × 適応型」AIエージェント向け開発ワークフローの全体像"
source: "https://qiita.com/y-morimatsu/items/c0f41d3901160be7e334"
author:
  - "[[y-morimatsu]]"
published: 2026-05-13
created: 2026-05-31
description: "はじめに 🎯 生成 AI を業務開発に組み込もうとすると、必ずぶつかる課題があります。「要件定義・設計のフェーズを、AI とどう協働すべきか」という問いです。コードを書く部分はエージェントが得意でも、その前段が曖昧なままだと、出来上がったものが期待からずれます。かといっ..."
tags:
  - "clippings"
---
### AI-DLC（AI-Driven Development Life Cycle）の要約
AWS Labsが公開した、生成AIエージェントによる開発を管理するための「適応型ワークフロー」です。要件定義から実装までを6つのステージ（INCEPTION）に分解し、人間による承認プロセスを組み込むことで、AIの暴走を防ぎ、開発プロセスの再現性を高める設計になっています。

### 主要なポイント
- **設計の3本柱**
  - **承認ゲート**: 各ステージ完了時に人間がレビュー・承認を行い、誤った方向への進行を防止。
  - **3段構成（Plan → Clarification → Artifacts）**: 一気に成果物を作らず、計画→質問→生成のサイクルで精度を向上。
  - **Audit Log（記録）**: すべての対話を追記専用かつ逐語的に記録し、事後の監査を可能にする。

- **INCEPTIONの6ステージ**
  1. **Workspace Detection**: 既存環境か新規かを自動判定。
  2. **Requirements Analysis**: 12の質問と矛盾検出を通じ要件を具体化。
  3. **User Stories**: ペルソナとストーリーを作成。
  4. **Workflow Planning**: リスクを含む実行計画の策定。
  5. **Application Design**: コンポーネントおよびアーキテクチャの定義。
  6. **Units Generation**: 実装単位への分解と受入基準の確立。

- **運用のコツ**
  - **Source of Truthの固定**: `requirements.md`を唯一の正情報源とし、情報の混在を防ぐ。
  - **早期のコンセプト固め**: 後段での仕様変更は波及コストが非常に高いため、初期ステージで徹底的に詰める。
  - **整合性監査**: Claude Codeの「ultrathink」等の拡張思考モードを活用し、複数ドキュメント間の整合性を自動チェックする。
