---
title: "Networking"
type: "concept"
tags:
  - "networking"
created: "2026-05-02"
updated: "2026-05-06"
sources:
  - "../60_Resources/@spurreiterwstun.md"
  - "../60_Resources/ALBとバックエンドEC2間をHTTPS通信させてみた.md"
  - "../60_Resources/AWS CloudFormationでWAFを設定したELBを構築しよう.md"
  - "../60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md"
  - "../60_Resources/Admin UI.md"
  - "../../60_Resources/ApplicationLoadBalancer(ALB)の自己証明書を用いたHTTPS化.md"
  - "../60_Resources/ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定.md"
  - "../60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md"
  - "../60_Resources/Express×Helmetでウェブセキュリティを学ぶ.md"
  - "../60_Resources/Fargate利用時のヘルスチェックを理解する - サーバーワークスエンジニアブログ.md"
  - "../60_Resources/GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った.md"
  - "../../60_Resources/How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API.md"
  - "../60_Resources/Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform.md"
  - "../60_Resources/Node.js で https をサポートする http proxy サーバを 80行で書いた.md"
  - "../60_Resources/Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化.md"
  - "../60_Resources/Obsidian textlintの導入方法を解説.md"
  - "../60_Resources/ObsidianでZennを書く！git submoduleで一元管理.md"
  - "../60_Resources/S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介.md"
  - "../../60_Resources/Stacked Diffs (and why you should know about them).md"
  - "../60_Resources/Start XState inspector locally · statelyaixstate.md"
  - "../60_Resources/TunnelReverse Tunnel over websocket を作った.md"
  - "../60_Resources/esbuild を使おう.md"
  - "../60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md"
  - "../60_Resources/kintone REST APIの共通仕様.md"
  - "../60_Resources/librespeedspeedtest Self-hosted Speed Test for HTML5 and more. Easy setup, examples, configurable, mobile friendly. Supports PHP, Node, Multiple servers, and more.md"
  - "../60_Resources/puppeteerでproxyを利用する方法.md"
  - "../60_Resources/sebhildebrandthttp-graceful-shutdown Gracefully shuts down node http server - can be used with http, express, koa, ....md"
  - "../../60_Resources/socket.ioのパケットを(触りだけ)キャプチャ.md"
  - "../../60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md"
  - "../60_Resources/vshnasciidoctor-confluence-exporter Command and Docker image to export Confluence wiki content to AsciiDoc.md"
  - "../60_Resources/websocket ALB.md"
  - "../60_Resources/web-tunnellite-http-tunnel-client.md"
  - "../60_Resources/【2024年最新版】ブックマークすべきGitHubリポジトリまとめ.md"
  - "../60_Resources/【Fiddler】Windows 上で HTTP  HTTPS 通信をキャプチャする.md"
  - "../60_Resources/【GitHub Actions】PRが来たら自動でJSONスキーマを検証する.md"
  - "../60_Resources/ウン十万接続のECSサービスを平和にアップデートしたい.md"
  - "../60_Resources/クォータ.md"
summary: "通信・接続・トンネリングに関する知識を扱うページ。"
---

# Networking

## 概要




































Networking は HTTPS、TCP、WebSocket、VPC などを含む通信設計の基礎領域。




































## 詳細

- [[authentication-networking-spurreiter-wstun-https-www-npmjs-com-package-s-276e96]]: `@spurreiter/wstun` は、ファイアウォール越しやグローバルIPを持たない環境での通信を可能にする、WebSocketベースのTCPトンネリング（前方および逆方向…
*発行: 2026-03-29 / [[authentication-networking-spurreiter-wstun-https-www-npmjs-com-package-s-276e96]]*
- [[networking-hiroyuki-kaji-alb-ec2-https-bd802e]]: 本記事は、AWSのApplication Load Balancer (ALB) とバックエンドのEC2インスタンス間でHTTPS通信を確立する方法の解説です。ALBでSSLオフ…
*発行: 2026-05-20 / [[networking-hiroyuki-kaji-alb-ec2-https-bd802e]]*
- [[aws-authentication-aws-cloudformation-waf-7f41c8]]: 本記事は、AWS CloudFormationを使用して、WAF（Web Application Firewall）を統合したELB（Elastic Load Balancer）…
*発行: 2021-02-03 / [[aws-authentication-aws-cloudformation-waf-7f41c8]]*
- [[aws-lambda-aws-lambda-api-cafc43]]: AWS Lambdaをバックエンドとする際、呼び出し元として選択する「API Gateway」と「Application Load Balancer (ALB)」の主な違いを比較…
*発行: 2019-08-07 / [[aws-lambda-aws-lambda-api-cafc43]]*
- [[authentication-networking-admin-ui-https-50c9f0]]: Socket.IO Admin UI は、Socket.IO デプロイメントの状態を可視化・管理するための公式ツールです。
*発行: 2026-03-03 / [[authentication-networking-admin-ui-https-50c9f0]]*
- [[networking-ykarakita-applicationloadbalancer-alb-https-950d4a]]: AWSのApplication Load Balancer (ALB) を自己署名証明書を使用してHTTPS化する手順について解説した記事です。
*発行: 2022-05-30 / [[networking-ykarakita-applicationloadbalancer-alb-https-950d4a]]*
- [[amazon-ecs-networking-ecs-fargate-nginx-057a0d]]: NLBとECS Fargate（Nginx + gRPC）構成において、gRPCの死活監視を適切に行うためのヘルスチェック設定に関する技術解説です。
*発行: 2019-12-24 / [[amazon-ecs-networking-ecs-fargate-nginx-057a0d]]*
- [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]: ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確認すべき項目を整理してい…
*発行: 2021-01-25 / [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]*
- [[networking-security-express-helmet-https-fdc4b5]]: Expressアプリケーションにおいて、セキュリティ対策ライブラリ「Helmet」を導入する意義と、各HTTPヘッダーが提供する具体的なセキュリティ効果を学習した記録です。
*発行: 2020-11-21 / [[networking-security-express-helmet-https-fdc4b5]]*
- [[aws-amazon-ecs-fargate-https-blog-serverworks-co-jp-fargate-07d2dd]]: AWS Fargate環境における、Application Load Balancer (ALB) および ECSタスク定義による2種類のヘルスチェックの仕様と運用上の注意点を解…
*発行: 2022-02-25 / [[aws-amazon-ecs-fargate-https-blog-serverworks-co-jp-fargate-07d2dd]]*
- [[ai-agent-git-copilot-agent-teams-6dc7c4]]: GitHubのリポジトリを「掲示板」として利用することで、離れた場所にある2台のPC間でGitHub Copilot Agentを協調させる仕組み「GH-Copilot Mult…
*発行: 2026-04-17 / [[ai-agent-git-copilot-agent-teams-6dc7c4]]*
- [[networking-user9196065-perform-resumable-upload-b8caa4]]: Microsoft Graph API でのSharePointへのレジューム可能なアップロード方法
*発行: 2020-02-26 / [[networking-user9196065-perform-resumable-upload-b8caa4]]*
- [[authentication-networking-microsoft-entra-id-bc229d]]: Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する方法
- [[networking-node-js-node-js-https-http-a88720]]: Node.jsを用いて、HTTPS通信をサポートする簡易的なHTTPプロキシサーバーを約80行のコードで実装する方法を解説した技術記事です。
*発行: 2013-09-02 / [[networking-node-js-node-js-https-http-a88720]]*
- [[networking-node-js-node-js-axios-http-daa2fa]]: Node.js環境において、`axios`を用いたHTTPリクエスト時に`keepAlive`を設定することで、TCPコネクションを再利用し、2回目以降のリクエスト処理時間を大幅…
*発行: 2023-03-29 / [[networking-node-js-node-js-axios-http-daa2fa]]*
- [[obsidian-git-obsidian-textlint-https-cf1f21]]: Obsidianで文章校正を自動化するプラグイン「Obsidian textlint」の導入・設定方法を解説した記事。本プラグインは公式コミュニティプラグインではないため、手動で…
- [[obsidian-git-obsidian-git-submodule-81a1a1]]: ObsidianとZennの連携：git submoduleによる一元管理
*発行: 2025-11-26 / [[obsidian-git-obsidian-git-submodule-81a1a1]]*
- [[amazon-ec2-cloudformation-s3-express-one-a725cf]]: S3 Express One Zone 用 VPC エンドポイント構築の要約
*発行: 2024-01-21 / [[amazon-ec2-cloudformation-s3-express-one-a725cf]]*
- [[cloudformation-code-review-stacked-diffs-why-142485]]: この記事は、MetaやGoogleで採用されている効率的なコードレビュー手法「Stacked Diffs（スタックド・ディフ）」について解説しています。これは、大きな機能を小さな…
- [[networking-performance-start-xstate-inspector-8b1469]]: XState InspectorをWebブラウザ以外（React Native等）の環境でローカル実行する方法についての議論。外部サービス（statecharts.io）に依存せ…
- [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]: 「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題を解決するため、Go言語…
*発行: 2020-05-29 / [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]*
- [[git-javascript-esbuild-https-qiita-com-tsukina-76ec3a]]: esbuild は、Go言語で記述された高速なモジュールバンドラです。従来のWebビルドツール（Webpack等）と比較して非常に高速で、JavaScript/TypeScrip…
*発行: 2025-09-20 / [[git-javascript-esbuild-https-qiita-com-tsukina-76ec3a]]*
- [[authentication-networking-ifritjp-kptunnel-tunnel-reverse-tunnel-789d3b]]: `kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続が一時的に切断されても、…
- [[authentication-networking-kintone-rest-api-33bbe5]]: kintone REST APIは、アプリ、レコード、スペースを操作するためのインターフェースです。以下に重要なポイントをまとめます。
- [[testing-docker-librespeed-speedtest-self-hosted-speed-395b94]]: LibreSpeed は、Flash、Java、Websocket を一切使用しない、非常に軽量な HTML5 ベースのインターネット速度測定ツールです。
- [[authentication-networking-puppeteer-proxy-https-96b647]]: Puppeteerを使用してブラウザ通信にプロキシを通すための2つの主要なアプローチを解説しています。
*発行: 2022-01-22 / [[authentication-networking-puppeteer-proxy-https-96b647]]*
- [[javascript-networking-sebhildebrandt-http-graceful-shutdown-gracefully-s-4ad72d]]: `http-graceful-shutdown` は、Node.jsのHTTPサーバーを安全に終了させるためのライブラリです。接続中のクライアントに影響を与えず、リクエスト処理の…
- [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]: この記事は、Node.jsのエンジニアがSocket.io（v1.3.5）の通信パケットを実際にキャプチャし、その内部挙動を理解するために調査・まとめた記録です。
*発行: 2015-09-30 / [[networking-node-js-socket-io-https-qiita-com-gitseitanaka-items-77e5d647-0003e2]]*
- [[lambda-networking-vpc-lambda-invoke-ec6acf]]: VPC内のLambdaから別のLambdaを呼び出す（invokeする）際のネットワーク構成別（パブリック/プライベートサブネット）の疎通可否を検証した技術解説記事です。
*発行: 2022-11-15 / [[lambda-networking-vpc-lambda-invoke-ec6acf]]*
- [[python-authentication-vshn-asciidoctor-confluence-exporter-command-docke-4c2f30]]: Confluence to AsciiDoc Exporter の概要
- [[networking-websocket-websocket-alb-https-a5066e]]: 本スクラップは、WebSocketをAWSのApplication Load Balancer (ALB) で運用する際の構成および注意点をまとめたものです。
*発行: 2024/04/03にコメント追加 / [[networking-websocket-websocket-alb-https-a5066e]]*
- [[git-javascript-2024-https-qiita-com-knr109-items-b5dadd056da9b227041b-fbcde3]]: エンジニアの学習や開発に役立つ、ブックマーク推奨のGitHubリポジトリをまとめた紹介記事です。初心者から上級者まで、スキルアップや効率化に繋がるリソースが網羅されています。
*発行: 2023-12-10 / [[git-javascript-2024-https-qiita-com-knr109-items-b5dadd056da9b227041b-fbcde3]]*
- [[networking-websocket-fiddler-windows-http-0958d1]]: Windows環境におけるHTTP/HTTPS通信のキャプチャ・解析ツール「Fiddler Classic」の導入から、基本的な操作方法およびログ保存手順を解説しています。
*発行: 2021-06-07 / [[networking-websocket-fiddler-windows-http-0958d1]]*
- [[git-ci-cd-actions-pr-json-a8cf77]]: Pull Request時にJSONファイルの構造が規定のスキーマと一致しているか検証する、GitHub Actionsを利用したCI環境の構築手順です。
*発行: 2022-07-22 / [[git-ci-cd-actions-pr-json-a8cf77]]*
- [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]: ECS上で長時間接続（WebSocket）を保持する「streamサーバ」をデプロイする際、AWSのデフォルトの停止処理では予期せぬ切断が発生していました。これを回避するため、A…
*発行: 2023-07-19 / [[networking-websocket-ecs-https-engineering-nature-global-entry-websocket-4b9252]]*
- [[aws-lambda-https-docs-aws-amazon-com-ja-jp-amazoncloudfront-latest-devel-ab9d59]]: 本ドキュメントは、Amazon CloudFrontにおける各種制限事項（クォータ）の一覧です。多くの項目はService QuotasやAWSサポートを通じて引き上げが可能です。

## 関連

- [[authentication-networking-spurreiter-wstun-https-www-npmjs-com-package-s-276e96]]
- [[security]]
- [[cloudfront]]
- [[networking-hiroyuki-kaji-alb-ec2-https-bd802e]]
- [[aws-authentication-aws-cloudformation-waf-7f41c8]]
- [[aws-lambda-aws-lambda-api-cafc43]]
- [[authentication-networking-admin-ui-https-50c9f0]]
- [[networking-ykarakita-applicationloadbalancer-alb-https-950d4a]]
- [[amazon-ecs-networking-ecs-fargate-nginx-057a0d]]
- [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]

## 出典

- `../60_Resources/@spurreiterwstun.md`
- https://www.npmjs.com/package/@spurreiter/wstun
- `../60_Resources/ALBとバックエンドEC2間をHTTPS通信させてみた.md`
- https://dev.classmethod.jp/articles/alb-backend-https/
- `../60_Resources/AWS CloudFormationでWAFを設定したELBを構築しよう.md`
- https://qiita.com/s_horikoshi/items/9b5da901601e947114ec
- `../60_Resources/AWS Lambda：API GatewayとApplication Load Balancerの違い.md`
- https://qiita.com/unhurried/items/5a497ec81e4fefe22396
- `../60_Resources/Admin UI.md`
- https://socket.io/docs/v4/admin-ui/
- `../../60_Resources/ApplicationLoadBalancer(ALB)の自己証明書を用いたHTTPS化.md`
- https://qiita.com/klynk2024/items/76db8d65838857227bd9
- `../60_Resources/ECS Fargate（Nginx + gRPC）構成のヘルスチェック設定.md`
- https://qiita.com/Ichi0124/items/b93e2ae4309e10b348c6
- `../60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md`
- https://qiita.com/x-color/items/8f986d01d6a6100b7d5b
- `../60_Resources/Express×Helmetでウェブセキュリティを学ぶ.md`
- https://qiita.com/qianer-fengtian/items/148602c437e1703aa764
- `../60_Resources/Fargate利用時のヘルスチェックを理解する - サーバーワークスエンジニアブログ.md`
- https://blog.serverworks.co.jp/fargate_healthcheck
- `../60_Resources/GitHub リポジトリを掲示板にして GitHub Copilot Agent を複数台で協調させる「なんちゃって Agent Teams」を作った.md`
- https://qiita.com/aktsmm/items/28f38fd1edea4edab31b
- `../../60_Resources/How to perform a resumable Upload to a SharePoint Site (Not Root) Subfolder using MS Graph API.md`
- https://stackoverflow.com/questions/60402838/how-to-perform-a-resumable-upload-to-a-sharepoint-site-not-root-subfolder-usin
- `../60_Resources/Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform.md`
- https://learn.microsoft.com/ja-jp/entra/identity-platform/howto-convert-app-to-be-multi-tenant
- `../60_Resources/Node.js で https をサポートする http proxy サーバを 80行で書いた.md`
- https://qiita.com/LightSpeedC/items/5c1edc2c974206c743f4
- `../60_Resources/Node.jsでのaxiosによるhttpリクエスト時にKeepAliveを設定して高速化.md`
- https://qiita.com/omukaik/items/caef4953c2580fdee5ee
- `../60_Resources/Obsidian textlintの導入方法を解説.md`
- https://notes.spisignal.jp/Esseys/Obsidian+textlint%E3%81%AE%E5%B0%8E%E5%85%A5%E6%96%B9%E6%B3%95%E3%82%92%E8%A7%A3%E8%AA%AC
- `../60_Resources/ObsidianでZennを書く！git submoduleで一元管理.md`
- https://zenn.dev/ktr17/articles/3505fab842af79
- `../60_Resources/S3 Express One Zone 用の VPC エンドポイント Gateway 型を作成する CloudFormation テンプレートの紹介.md`
- https://dev.classmethod.jp/articles/cloudformation-template-for-s3-express-one-zone-vpc-endpoint/
- `../../60_Resources/Stacked Diffs (and why you should know about them).md`
- https://newsletter.pragmaticengineer.com/p/stacked-diffs
- `../60_Resources/Start XState inspector locally · statelyaixstate.md`
- https://github.com/statelyai/xstate/discussions/1626
- `../60_Resources/TunnelReverse Tunnel over websocket を作った.md`
- https://ifritjp../.github.io/blog2/public/posts/2020/2020-05-29-tunnel/
- `../60_Resources/esbuild を使おう.md`
- https://qiita.com/Tsukina_7mochi/items/0aa38da6b9b4dd22eacd
- `../60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md`
- https://github.com/ifritJP/kptunnel
- `../60_Resources/kintone REST APIの共通仕様.md`
- https://cybozu.dev/ja/kintone/docs/rest-api/overview/kintone-rest-api-overview/
- `../60_Resources/librespeedspeedtest Self-hosted Speed Test for HTML5 and more. Easy setup, examples, configurable, mobile friendly. Supports PHP, Node, Multiple servers, and more.md`
- https://github.com/librespeed/speedtest?tab=readme-ov-file
- `../60_Resources/puppeteerでproxyを利用する方法.md`
- https://kagasu.hatenablog.com/entry/2022/01/22/023324
- `../60_Resources/sebhildebrandthttp-graceful-shutdown Gracefully shuts down node http server - can be used with http, express, koa, ....md`
- https://github.com/sebhildebrandt/http-graceful-shutdown/tree/master
- `../../60_Resources/socket.ioのパケットを(触りだけ)キャプチャ.md`
- https://qiita.com/gitseitanaka/items/77e5d647fa364020d3f1
- `../../60_Resources/vpc 内 Lambda から Lambda を呼ぶ( invoke する)場合、public subnet や private subnet などのパターン別に呼べるか検証してみた.md`
- https://qiita.com/hirai-11/items/f16b326061956fb85c9c
- `../60_Resources/vshnasciidoctor-confluence-exporter Command and Docker image to export Confluence wiki content to AsciiDoc.md`
- https://github.com/vshn/asciidoctor-confluence-exporter
- `../60_Resources/websocket ALB.md`
- https://zenn.dev/ymktmk/scraps/71c69a061a9acd
- `../60_Resources/【2024年最新版】ブックマークすべきGitHubリポジトリまとめ.md`
- https://qiita.com/KNR109/items/b5dadd056da9b227041b
- `../60_Resources/【Fiddler】Windows 上で HTTP  HTTPS 通信をキャプチャする.md`
- https://qiita.com/nt-7/items/c897e9460ef43af6ed14
- `../60_Resources/【GitHub Actions】PRが来たら自動でJSONスキーマを検証する.md`
- https://zenn.dev/fus1ondev/articles/858836b41f2c80
- `../60_Resources/ウン十万接続のECSサービスを平和にアップデートしたい.md`
- https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown
- `../60_Resources/クォータ.md`
- https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html
## 詳細

- リバーストンネル系では WebSocket や専用トンネルクライアントを使い、ローカル HTTP サーバを外部公開する運用がある。
- `lite-http-tunnel-client` は Node.js 製の軽量トンネルクライアントで、開発中のローカル Web サービスを一時公開する用途に向く。
