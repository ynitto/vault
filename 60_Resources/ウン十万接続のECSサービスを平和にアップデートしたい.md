---
title: "ウン十万接続のECSサービスを平和にアップデートしたい"
source: "https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown"
author:
  - "[[mxg]]"
published: 2023-07-19
created: 2026-05-01
description: "こんにちは大塚(@maaash)です。7月からCTOに復帰しました。引き続きよろしくお願いいたします。 これは第2回 Nature Engineering Blog 祭11日目のエントリです。 昨日はファームウェア・エンジニアの村田さんによる Matterでやりたかったけどできなかったこと - Nature Engineering Blog でした。 今日のお話は、話題の新製品Remo nanoやMatterとは関係ありません。 背景 先週、黒田さんが ウン十万接続のALB SSL証明書を平和に更新したい - Nature Engineering Blog を書いてくれました。 その話は AL…"
tags:
  - "clippings"
---
### 記事の要約
ECS上で長時間接続（WebSocket）を保持する「streamサーバ」をデプロイする際、AWSのデフォルトの停止処理では予期せぬ切断が発生していました。これを回避するため、ALBのターゲットグループの状態をアプリ側でポーリングし、適切なタイミングで独自にグレースフルシャットダウンを行うことで、平和なデプロイを実現した事例です。

### 要点
- **課題**: ECSのデプロイ時、SIGTERM受信後にALBが一定時間（約8秒）で強制的に接続を切断してしまうため、WebSocket接続がバッサリ切られ、クライアントが一斉に再接続してくる負荷が発生していた。
- **原因**: ALBはECSのStopTimeout（最大120秒）を関知せず、独自にコネクションを終了させる仕様である。
- **解決策**: 
    - アプリケーションコード内で`DescribeTargetHealth`を定期的にポーリングする。
    - ターゲット状態が「draining」になったことを検知する。
    - 設定した猶予期間内に、自発的にWebSocket接続を段階的に切断する実装に変更した。
- **成果**: 接続の切断が急激なスパイクにならず、グラフ上で緩やかに推移するようになり、デプロイ時のサービス負荷を抑えることに成功した。