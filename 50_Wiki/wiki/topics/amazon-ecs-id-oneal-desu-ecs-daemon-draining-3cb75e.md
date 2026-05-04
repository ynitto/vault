---
title: "ECSのDAEMONをDRAININGで直ぐに停止しないようにした"
type: "topic"
tags:
  - "amazon-ecs"
  - "id-oneal-desu"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSのDAEMONをDRAININGで直ぐに停止しないようにした.md"
summary: "ECSでのDAEMONサービス停止順序問題とその解決策"
---

# ECSのDAEMONをDRAININGで直ぐに停止しないようにした

## 概要

ECSでのDAEMONサービス停止順序問題とその解決策

*発行: 2020-04-30 / [[amazon-ecs-id-oneal-desu-ecs-daemon-draining-3cb75e]]*

## 主要なトピック

- [[amazon-ecs]]
- [[id-oneal-desu]]

## 詳細

- 本記事では、ECSインスタンスのドレイニング（終了）時に、DAEMONサービスがREPLICAサービスより先に停止してログ収集などが中断される問題を解決する方法を解説しています。
- 課題
- インスタンス終了時、全タスクに対して同時に停止命令が送られる。
- その結果、FluentdのようなDAEMONサービスが先に停止し、REPLICAサービスが終了するまでのログを取りこぼすリスクがある。
- 解決策：ecs-daemon-protectorの導入
- **アプローチ**: DAEMONサービスにサイドカーとして「ecs-daemon-protector」を追加し、`dependsOn`を活用して停止順序を制御。
- **仕組み**:
- タスクの停止順序を「保護用サイドカー → 本体のDAEMONサービス」の順にする。
- サイドカーはSIGTERM受信後、インスタンス内の全REPLICAサービスが終了するまで待機する。

*発行: 2020-04-30 / [[amazon-ecs-id-oneal-desu-ecs-daemon-draining-3cb75e]]*

## 関連テーマ

- [[amazon-ecs]]
- [[id-oneal-desu]]

## 出典

- `/Users/nitto/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/60_Resources/ECSのDAEMONをDRAININGで直ぐに停止しないようにした.md`
- https://buildersbox.corp-sansan.com/entry/2020/04/30/110000
