---
title: "Authentication"
type: "concept"
tags:
  - "security"
  - "auth"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/@spurreiterwstun.md"
  - "../60_Resources/AIエージェントに使わせるCLIの設計原則8選.md"
  - "../60_Resources/APIトークン認証の論理設計.md"
  - "../60_Resources/AWS CloudFormationでWAFを設定したELBを構築しよう.md"
  - "../60_Resources/Admin UI.md"
  - "../60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md"
  - "../60_Resources/Claude Code に Codex の対立レビューを挟むと見えるもの — codex-plugin-cc で始めるセカンドオピニオン駆動開発.md"
  - "../60_Resources/Claude CodeでSkillsを定期実行で自動化する方法.md"
  - "../60_Resources/Dropbox Business APIの基礎知識.md"
  - "../60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md"
  - "../60_Resources/ES2016 asyncawait キャンセル可能な非同期関数を実装する方法.md"
  - ".wiki/atoms/wiki/atomswiki/atoms/wiki/atomswiki/atoms/../60_Resources/Javascripthtml in gitlab wiki page?.md"
  - "../60_Resources/Jira APIをたたく｜wiki/atoms/shu223.md"
  - "../60_Resources/Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform.md"
  - "../60_Resources/Node.js でメモリ肥大化の原因を特定してみた.md"
  - "../60_Resources/PuppeteerでCookieを使ってログインする方法.md"
  - "../60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md"
  - "../60_Resources/TunnelReverse Tunnel over websocket を作った.md"
  - "../60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md"
  - "../60_Resources/kintone REST APIの共通仕様.md"
  - "../60_Resources/openapi-generatordocsgeneratorscwiki.md at master.md"
  - "../60_Resources/puppeteerでproxyを利用する方法.md"
  - "../60_Resources/socket.ioのv3で知らなかったこと.md"
  - "../60_Resources/vshnasciidoctor-confluence-exporter Command and Docker image to export Confluence wiki content to AsciiDoc.md"
  - "../60_Resources/「ハーネスが大事」の先にある、3つの設計判断｜Workato Japan.md"
  - "../60_Resources/サーバーレスなデータ収集APIを作るときの困りポイント.md"
  - "../60_Resources/チーム スペースを使用するチームへの対応ガイド.md"
  - "../60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート.md"
summary: "認証・トークン・mTLS などの設計論点をまとめるページ。"
---

# Authentication

## 概要




























Authentication はシステム境界を守るための確認手段で、トークン管理や相互 TLS を含む。




























## 詳細

- [[authentication-networking-spurreiter-wstun-https-www-npmjs-com-package-s-276e96]]: `@spurreiter/wstun` は、ファイアウォール越しやグローバルIPを持たない環境での通信を可能にする、WebSocketベースのTCPトンネリング（前方および逆方向…
*発行: 2026-03-29 / [[authentication-networking-spurreiter-wstun-https-www-npmjs-com-package-s-276e96]]*
- [[authentication-ai-cli-8-https-5b1b56]]: 本記事は、AIエージェントが操作しやすい「エージェントフレンドリーなCLI」を設計するための8つの原則を提案しています。MCPやAPIスキルとの使い分けを整理した上で、信頼性と探…
*発行: 2026-04-21 / [[authentication-ai-cli-8-https-5b1b56]]*
- [[authentication-api-https-zenn-dev-ad5-articles-fae2e929fca79e-f92f0b]]: API開発における「トークン認証」の論理的な設計手法と課題について、特にフロントエンドとの整合性や複数端末利用の観点から考察した技術記事です。
*発行: 2023-09-16 / [[authentication-api-https-zenn-dev-ad5-articles-fae2e929fca79e-f92f0b]]*
- [[aws-authentication-aws-cloudformation-waf-7f41c8]]: 本記事は、AWS CloudFormationを使用して、WAF（Web Application Firewall）を統合したELB（Elastic Load Balancer）…
*発行: 2021-02-03 / [[aws-authentication-aws-cloudformation-waf-7f41c8]]*
- [[authentication-networking-admin-ui-https-50c9f0]]: Socket.IO Admin UI は、Socket.IO デプロイメントの状態を可視化・管理するための公式ツールです。
*発行: 2026-03-03 / [[authentication-networking-admin-ui-https-50c9f0]]*
- [[aws-lambda-amazon-api-gateway-1339da]]: Amazon API Gateway の相互 TLS（mTLS）認証では、デフォルトでは証明書の失効確認が行われないという課題があります。本記事では、この問題を Lambda オ…
*発行: 2021-12-06 / [[aws-lambda-amazon-api-gateway-1339da]]*
- [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]: Claude Code向け公式プラグイン「codex-plugin-cc」を活用し、AnthropicのClaudeとOpenAIのCodexという異なるモデルを組み合わせること…
*発行: 2026-04-24 / [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]*
- [[claude-code-git-claude-skills-https-2f1a7a]]: Claude Codeの「Skills（カスタムワークフロー）」をヘッドレスモード（`-p`オプション）で実行し、Task Schedulerやcronと組み合わせることで、**…
*発行: 2025-12-29 / [[claude-code-git-claude-skills-https-2f1a7a]]*
- [[authentication-nkmk1215-dropbox-business-api-0c2684]]: 本記事は「DBX Platform デベロッパーガイド」を読んだ際の個人メモです。Dropbox APIの認証方式や名前空間（チームフォルダ/チームスペース）の概念について解説し…
*発行: 2021-09-12 / [[authentication-nkmk1215-dropbox-business-api-0c2684]]*
- [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]: ECSでタスクが起動しない（または停止する）際のトラブルシューティングガイド。主な原因である「ネットワーク」「IAM権限」「リソース不足」に焦点を当て、確認すべき項目を整理してい…
*発行: 2021-01-25 / [[amazon-ecr-authentication-ecs-https-qiita-com-x-color-items-8f986d01d6a6-59e47b]]*
- [[authentication-es2016-async-await-https-qiita-com-sukobuto-items-298de3f-57cd39]]: ES2016（当時のES7）の `async/await` に標準で存在しない「非同期処理のキャンセル」を、.NET Frameworkの `CancellationToken`…
*発行: 2016-11-14 / [[authentication-es2016-async-await-https-qiita-com-sukobuto-items-298de3f-57cd39]]*
- [[git-authentication-javascript-html-gitlab-wiki-4cfde2]]: Gitlab WikiでのJavaScript利用に関する回答の要約
*発行: 2019-12-06 / [[git-authentication-javascript-html-gitlab-wiki-4cfde2]]*
- [[python-authentication-jira-api-shu223-2bdd07]]: Jiraの各種タスクを自動化するために、Jira APIを利用するための準備・手順をまとめた技術メモです。
*発行: 2022-07-05 / [[python-authentication-jira-api-shu223-2bdd07]]*
- [[authentication-networking-microsoft-entra-id-bc229d]]: Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する方法
- [[authentication-javascript-node-js-https-zenn-dev-ubie-f2ad55]]: Node.js環境下で`langchain`ライブラリを使用中に発生したメモリ肥大化問題について、デバッグ手法から原因特定、解決に至るまでのプロセスを解説した技術記事です。
*発行: 2023-12-07 / [[authentication-javascript-node-js-https-zenn-dev-ubie-f2ad55]]*
- [[authentication-orange634nty-puppeteer-cookie-https-b30ecb]]: Puppeteerを使用してWebサイトへのログインを自動化し、Cookie情報を保存・再利用することで、ログイン状態が必要なページを効率的にスクレイピングする方法の解説記事です。
*発行: 2019-06-09 / [[authentication-orange634nty-puppeteer-cookie-https-b30ecb]]*
- [[aws-lambda-rest-api-http-47b62c]]: Amazon API Gateway：REST API と HTTP API の比較要約
- [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]: 「kptunnel」は、ネットワーク制限下でTCP通信を可能にする、WebSocketベースのトンネルツールです。既存のフリーツールで頻発していた切断問題を解決するため、Go言語…
*発行: 2020-05-29 / [[authentication-networking-tunnel-reverse-tunnel-over-117d08]]*
- [[authentication-networking-ifritjp-kptunnel-tunnel-reverse-tunnel-789d3b]]: `kptunnel` は、WebSocketおよびTCP/IP上でトンネル通信（通常のトンネルおよびリバーストンネル）を行うためのツールです。トンネル接続が一時的に切断されても、…
- [[authentication-networking-kintone-rest-api-33bbe5]]: kintone REST APIは、アプリ、レコード、スペースを操作するためのインターフェースです。以下に重要なポイントをまとめます。
- [[authentication-security-openapi-generator-docs-generators-cwiki-md-at-ma-9addec]]: 本ドキュメントは、OpenAPI Generatorにおける「cwiki」ジェネレーターの仕様書です。このジェネレーターは、OpenAPI定義からConfluence Wiki用…
- [[authentication-networking-puppeteer-proxy-https-96b647]]: Puppeteerを使用してブラウザ通信にプロキシを通すための2つの主要なアプローチを解説しています。
*発行: 2022-01-22 / [[authentication-networking-puppeteer-proxy-https-96b647]]*
- [[authentication-socket-io-v3-https-zenn-dev-dove-scraps-8112539765d869-7e8e20]]: 本記事はSocket.io v3の主要機能と開発上の注意点をまとめた技術メモです。サーバー・クライアントの初期化から、ルーム、ミドルウェア、CORS、エラーハンドリング、バイナリ…
*発行: 2020/12/12にクローズ / [[authentication-socket-io-v3-https-zenn-dev-dove-scraps-8112539765d869-7e8e20]]*
- [[python-authentication-vshn-asciidoctor-confluence-exporter-command-docke-4c2f30]]: Confluence to AsciiDoc Exporter の概要
- [[mcp-authentication-3-workato-japan-ad95cc]]: AIエージェントの構築において、モデルの性能以上に重要な「エージェントハーネス（インフラ環境）」の具体的な設計判断を解説。AIの「間違い」を前提とし、業務事故を防ぐための3つのレ…
*発行: 2026-04-08 / [[mcp-authentication-3-workato-japan-ad95cc]]*
- [[aws-api-gateway-api-https-engineers-fenrir-inc-com-entry-2023-03-16-1728-603157]]: AWS API Gateway、Kinesis、S3を組み合わせたデータ収集APIの構築において、実務で発生しやすい課題とその解決策を解説した記事です。
*発行: 2023-03-16 / [[aws-api-gateway-api-https-engineers-fenrir-inc-com-entry-2023-03-16-1728-603157]]*
- [[authentication-sayo-https-navi-dropbox-jp-guide-to-adding-support-for-te-e64e68]]: Dropboxが提供する「チームスペース」への移行に伴い、APIを利用した連携アプリケーションで必要となる仕様変更や対応方法を解説した技術ガイドです。
*発行: 2023-03-09 / [[authentication-sayo-https-navi-dropbox-jp-guide-to-adding-support-for-te-e64e68]]*
- [[aws-authentication-amazon-cloudfront-mtls-2f6191]]: Amazon CloudFront が mTLS をサポート
  *発行: 2025-12-04 / [[aws-authentication-amazon-cloudfront-mtls-2f6191]]*

## 関連

- [[authentication-networking-spurreiter-wstun-https-www-npmjs-com-package-s-276e96]]
- [[security]]
- [[api-gateway]]
- [[authentication-ai-cli-8-https-5b1b56]]
- [[authentication-api-https-zenn-dev-ad5-articles-fae2e929fca79e-f92f0b]]
- [[aws-authentication-aws-cloudformation-waf-7f41c8]]
- [[authentication-networking-admin-ui-https-50c9f0]]
- [[aws-lambda-amazon-api-gateway-1339da]]
- [[claude-code-authentication-claude-codex-codex-plugin-cc-e31cad]]
- [[claude-code-git-claude-skills-https-2f1a7a]]

## 出典

- `../60_Resources/@spurreiterwstun.md`
- https://www.npmjs.com/package/@spurreiter/wstun
- `../60_Resources/AIエージェントに使わせるCLIの設計原則8選.md`
- https://zenn.dev/assign/articles/b3d1d07d385b87
- `../60_Resources/APIトークン認証の論理設計.md`
- https://zenn.dev/ad5/articles/fae2e929fca79e
- `../60_Resources/AWS CloudFormationでWAFを設定したELBを構築しよう.md`
- https://qiita.com/s_horikoshi/items/9b5da901601e947114ec
- `../60_Resources/Admin UI.md`
- https://socket.io/docs/v4/admin-ui/
- `../60_Resources/Amazon API Gateway での相互 TLS 認証をちゃんとやる.md`
- https://tech.aptpod.co.jp/entry/2021/12/06/070000
- `../60_Resources/Claude Code に Codex の対立レビューを挟むと見えるもの — codex-plugin-cc で始めるセカンドオピニオン駆動開発.md`
- https://qiita.com/nogataka/items/52dcdb315c54dddede01
- `../60_Resources/Claude CodeでSkillsを定期実行で自動化する方法.md`
- https://zenn.dev/tenormusica/articles/claude-code-headless-subscription-discovery-2025
- `../60_Resources/Dropbox Business APIの基礎知識.md`
- https://qiita.com/nkmk1215/items/7b1427a74a74b473266c
- `../60_Resources/ECSでタスクが起動しない場合に確認すべきこと.md`
- https://qiita.com/x-color/items/8f986d01d6a6100b7d5b
- `../60_Resources/ES2016 asyncawait キャンセル可能な非同期関数を実装する方法.md`
- https://qiita.com/sukobuto/items/298de3f97c0862aa8c3c
- `.wiki/atoms/wiki/atomswiki/atoms/wiki/atomswiki/atoms/../60_Resources/Javascripthtml in gitlab wiki page?.md`
- https://stackoverflow.com/questions/59203694/javascript-html-in-gitlab-wiki-page
- `../60_Resources/Jira APIをたたく｜wiki/atoms/shu223.md`
- https://note.com/shu223/n/n392136487ee9
- `../60_Resources/Microsoft Entra ID でシングルテナント アプリをマルチテナントに変換する - Microsoft identity platform.md`
- https://learn.microsoft.com/ja-jp/entra/identity-platform/howto-convert-app-to-be-multi-tenant
- `../60_Resources/Node.js でメモリ肥大化の原因を特定してみた.md`
- https://zenn.dev/ubie_dev/articles/f64561d59918d1
- `../60_Resources/PuppeteerでCookieを使ってログインする方法.md`
- https://qiita.com/orange634nty/items/8971bfa9349125ba0a78
- `../60_Resources/REST API と HTTP API のどちらかを選択する - Amazon API Gateway.md`
- https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/http-api-vs-rest.html
- `../60_Resources/TunnelReverse Tunnel over websocket を作った.md`
- https://ifritjp../.github.io/blog2/public/posts/2020/2020-05-29-tunnel/
- `../60_Resources/ifritJPkptunnel TunnelReverse Tunnel over WebSocket and TCPIP..md`
- https://github.com/ifritJP/kptunnel
- `../60_Resources/kintone REST APIの共通仕様.md`
- https://cybozu.dev/ja/kintone/docs/rest-api/overview/kintone-rest-api-overview/
- `../60_Resources/openapi-generatordocsgeneratorscwiki.md at master.md`
- https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/cwiki.md
- `../60_Resources/puppeteerでproxyを利用する方法.md`
- https://kagasu.hatenablog.com/entry/2022/01/22/023324
- `../60_Resources/socket.ioのv3で知らなかったこと.md`
- https://zenn.dev/dove/scraps/8112539765d869
- `../60_Resources/vshnasciidoctor-confluence-exporter Command and Docker image to export Confluence wiki content to AsciiDoc.md`
- https://github.com/vshn/asciidoctor-confluence-exporter
- `../60_Resources/「ハーネスが大事」の先にある、3つの設計判断｜Workato Japan.md`
- https://note.com/workato/n/n4bb1c95a5347
- `../60_Resources/サーバーレスなデータ収集APIを作るときの困りポイント.md`
- https://engineers.fenrir-inc.com/entry/2023/03/16/172808
- `../60_Resources/チーム スペースを使用するチームへの対応ガイド.md`
- https://navi.dropbox.jp/guide-to-adding-support-for-team-space
- `../60_Resources/信頼は相互に Amazon CloudFront が mTLS をサポート.md`
- https://aws.amazon.com/jp/blogs/news/trust-goes-both-ways-amazon-cloudfront-now-supports-viewer-mtls/
