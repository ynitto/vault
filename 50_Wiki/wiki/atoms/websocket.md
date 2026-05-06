---
title: "WebSocket"
type: "term"
tags:
  - "websocket"
  - "networking"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "60_Resources/Start XState inspector locally · statelyaixstate.md"
  - "60_Resources/TunnelReverse Tunnel over websocket を作った.md"
  - "60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md"
  - "60_Resources/librespeedspeedtest Self-hosted Speed Test for HTML5 and more. Easy setup, examples, configurable, mobile friendly. Supports PHP, Node, Multiple servers, and more.md"
  - "60_Resources/socket.ioのパケットを(触りだけ)キャプチャ.md"
  - "60_Resources/websocket ALB.md"
  - "60_Resources/【Fiddler】Windows 上で HTTP  HTTPS 通信をキャプチャする.md"
  - "60_Resources/ウン十万接続のECSサービスを平和にアップデートしたい.md"
summary: "双方向通信のためのプロトコル。"
---

# WebSocket

## 概要








WebSocket は長時間接続と双方向通信を必要とするケースで使われる。








## 詳細

- [[networking-performance-start-xstate-inspector-8b1469]]: XState InspectorをWebブラウザ以外（React Native等）の環境でローカル実行する方法についての議論。外部サービス（statecharts.io）に依存せ…
- [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]: 「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題を解決するため、Go言語…
*発行: 2020-05-29 / [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]*
- [[authentication-networking-ifritjp-kptunnel-tunnel-reverse-tunnel-789d3b]]: `kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続が一時的に切断されても、…
- [[testing-docker-librespeed-speedtest-self-hosted-speed-395b94]]: LibreSpeed は、Flash、Java、Websocket を一切使用しない、非常に軽量な HTML5 ベースのインターネット速度測定ツールです。
- [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]: この記事は、Node.jsのエンジニアがSocket.io（v1.3.5）の通信パケットを実際にキャプチャし、その内部挙動を理解するために調査・まとめた記録です。
*発行: 2015-09-30 / [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]*
- [[networking-websocket-websocket-alb-https-a5066e]]: 本スクラップは、WebSocketをAWSのApplication Load Balancer (ALB) で運用する際の構成および注意点をまとめたものです。
*発行: 2024/04/03にコメント追加 / [[networking-websocket-websocket-alb-https-a5066e]]*
- [[networking-websocket-fiddler-windows-http-0958d1]]: Windows環境におけるHTTP/HTTPS通信のキャプチャ・解析ツール「Fiddler Classic」の導入から、基本的な操作方法およびログ保存手順を解説しています。
*発行: 2021-06-07 / [[networking-websocket-fiddler-windows-http-0958d1]]*
- [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]: ECS上で長時間接続（WebSocket）を保持する「streamサーバ」をデプロイする際、AWSのデフォルトの停止処理では予期せぬ切断が発生していました。これを回避するため、A…
  *発行: 2023-07-19 / [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]*

## 関連

- [[networking-performance-start-xstate-inspector-8b1469]]
- [[networking]]
- [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]
- [[authentication-networking-ifritjp-kptunnel-tunnel-reverse-tunnel-789d3b]]
- [[testing-docker-librespeed-speedtest-self-hosted-speed-395b94]]
- [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]
- [[networking-websocket-websocket-alb-https-a5066e]]
- [[networking-websocket-fiddler-windows-http-0958d1]]
- [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]

## 出典

- `60_Resources/Start XState inspector locally · statelyaixstate.md`
- https://github.com/statelyai/xstate/discussions/1626
- `60_Resources/TunnelReverse Tunnel over websocket を作った.md`
- https://ifritjp.github.io/blog2/public/posts/2020/2020-05-29-tunnel/
- `60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md`
- https://github.com/ifritJP/kptunnel
- `60_Resources/librespeedspeedtest Self-hosted Speed Test for HTML5 and more. Easy setup, examples, configurable, mobile friendly. Supports PHP, Node, Multiple servers, and more.md`
- https://github.com/librespeed/speedtest?tab=readme-ov-file
- `60_Resources/socket.ioのパケットを(触りだけ)キャプチャ.md`
- https://qiita.com/gitseitanaka/items/77e5d647fa364020d3f1
- `60_Resources/websocket ALB.md`
- https://zenn.dev/ymktmk/scraps/71c69a061a9acd
- `60_Resources/【Fiddler】Windows 上で HTTP  HTTPS 通信をキャプチャする.md`
- https://qiita.com/nt-7/items/c897e9460ef43af6ed14
- `60_Resources/ウン十万接続のECSサービスを平和にアップデートしたい.md`
- https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown
