---
title: "ぼくがかんがえた最強のObsidian設定｜古村藍"
source: "https://note.com/indigo372/n/nae1e72203c5b"
author:
  - "[[古村藍]]"
published: 2023-10-06
created: 2026-04-19
description: "私はObsidianを使い始めて一年近くが経ちます。 例に漏れず本ツールの有用性やカスタム性に魅了されて使い続けているわけですが、活発に更新されるツールなので使い方や設定も日々変わっていきます。 そんな中、ここ最近「これでFAじゃね？」という設定に落ち着いてきたので、今の私のObsidian環境を晒します。 はじめに書いておきたいのは、「すべての人にとって最適な形などない」ということです。ある人にとっては有用なカスタマイズでも、ある人にとっては不便なだけかも知れない。 なので今回は「対象となる人」をはじめに宣言しておきます。以下に当てはまる人であれば私が使っている設定は有用に働くかも知"
tags:
  - "clippings"
---
# ぼくがかんがえた最強のObsidian設定：要約

この設定は、Obsidianを1年近く使用した著者が「これでFAじゃね？」と考える最適化された環境です。特に以下のユーザーにおすすめです。

- **筋金入りのめんどくさがり**：細かい作業をルーチン化したくない人。
- **多くの情報を記録したい**：後で情報を探すのに苦労したくない人。
- **軽量運用を重視**：機能を多少犠牲にしてもソフトを軽くしたい人。
- **複数デバイスで使いたい**：課金なしでスマホ等と同期したい人。
- ある程度のObsidian基本用法を理解している中級者向け。

## オフにする機能 (軽量化のため)

- **グラフビュー**：ビジュアル目的以外に理由がないためオフ。
- **キャンバス**：面倒くさがりには扱いにくく、動作が不安定なためオフ。
- その他：スライド、オーディオレコーダー、パブリッシュ、同期（好みによる）。

## コミュニティプラグイン

### 必須級プラグイン

- **Advanced Tables**: Table作成を容易にする。
- **Advanced URI**: ウェブクリップ機能に必須。
- **Auto Template Trigger**: 「ものぐさproperty」に必須。
- **Dataview**: Obsidian上でJSなどを有効にする最強プラグイン。
- **Floating Search**: 検索機能をモーダル表示し、サイドパネルを専有しない。
- **oblogger**: タグ管理ビューの改善に貢献。
- **Obsidian Git**: PCでの同期・バックアップ用（最も安定・高速）。
- **Obsidian Memos**: デイリーノートのハードルを下げるミニTwitter的なツール。
- **Pane Relief**: タブに「戻る/進む」機能を追加。
- **Quick Explorer**: パンくずリスト表示、ファイルのフォルダ移動が容易になる。
- **Recent Files**: 最近見たファイルを表示。
- **Remotely Save**: スマホ・iPadでの同期手段。

### あれば便利プラグイン

- **Admonition**: calloutの予測変換用。
- **Auto Card Link**: URLをカードリンク形式で表示し、可読性向上。
- **Calendar**: 有名プラグイン。
- **Copy Image and URL context menu**: 画像の右クリックコピー機能を追加。
- **File Explorer++**: デフォルトのファイルエクスプローラーでフォルダのピン化・hide化が可能に。
- **Global Search and Replace**: 「検索して置換」機能を追加。
- **Icon Folder**: フォルダにアイコンを追加し、可読性UP。
- **Image Toolkit**: ノート上の画像に様々な処理を可能にする。
- **Scroll to Top Plugin**: 長いノートで役立つ「トップへ戻る」ボタン。
- **txt as md**: .txtファイルをObsidian上で読めるようにする。

### 好みで導入するプラグイン

- **Dialogue**: ChatGPTなどAIとの会話記録に便利。
- **Minimal Theme Settings**: Minimalテーマの色合いを簡単に変更できる。
- **Home Tab**: デフォルトより使いやすい新規タブ画面。

## フォルダ構成 (7つ、運用は4つ)

- **General Notes**: デフォルトディレクトリ。一時的なノート、移動可能。
- **Info Notes**: 仕入れた情報（コピペ可）を「1ノート1情報」で格納。ベクトルを持たない辞書的な役割。
- **Complete Notes**: 外部公開前提・可能な品質のノート（本記事のようなもの）。
- **FAQ**: 困りごとへの解決策を格納（例：「～する方法」）。
- **Archive**: ほぼ見なくなったファイルのゴミ箱候補（非表示推奨）。
- **res**: Obsidian内の画像や非ノートファイルを収容（非表示推奨）。
- **Web Clip**: Advanced URIでWebクリッピングしたMarkdownの保管場所。

## テーマ

- **Minimal**を推奨：人気、手厚いサポート、カスタマイズ性、軽量。

## 基本的な運用法

- **ものぐさproperty**:
    - Auto Template Triggerとビルトインのプロパティ機能を活用。
    - 面倒なテンプレート挿入を自動化するため、テンプレートは「タグ」「作成日時」のみのシンプルなものを一つだけ用意し、脳死でEnterを押せるようにする。
    - DataviewJSで「関連ノート」を表示し、Scrapbox的ブラウジングを実現。
```dataviewjs
dv.header(3, \\"関連ノート\\");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,\\"desc\\").limit(15).file.link);
}

for (let outgo of dv.pages('outgoing([[' + dv.current().file.name + ']])')) {
    dv.header(4, outgo.file.name);
    dv.list(outgo.file.inlinks.sort());
}
```

- **タグ管理**:
    - デフォルトのタグビューの視認性の悪さをobloggerで解決。
    - obloggerでタグをエクスプローラーのようにツリー表示し、タグに含まれるノート一覧を見やすくする。
    - obloggerの機能はシンプルさ・軽量化のため、Show dailies, Show files, Show untaggedなどをオフにする。

- **Floating Searchの威力**:
    - 検索機能をモーダルウィンドウで表示することで、サイドパネルを専有せず、視線移動も少なく、快適な検索が可能。
    - `Ctrl+Shift+F`にショートカット登録を推奨。

- **サイドパネル構成**:
    - ファイルエクスプローラーに可能な限り大きな面積を与える。
    - パネル分割は最大二つまでとし、それ以上はパネル内のタブで分ける。
    - 例：左パネル（上Oblogger/下Recent Notes）、右パネル（上エクスプローラー/下Source Controlなど）。

- **Web Clip**:
    - Advanced URIとmarkdownloadブラウザ拡張機能でウェブサイトをクリッピング。
    - markdownloadの設定でfrontmatterからタグを削除推奨（タグ一覧のカオス化防止）。

- **Memosの威力**:
    - Obsidian Memosはデイリーノートの敷居を劇的に下げるローカルツイッター的なツール。

- **内部リンクについて**:
    - 最初はノートを書き、後から「アウトゴーイングリンク」欄で随時リンクを更新するのが推奨。
    - `[[]]`形式のリンクはエクスポート性を考慮し、依存しすぎないよう注意が必要。

## 終わりに

Obsidianに「正解の用法」はなく、各々が使いやすい形を見つけることが重要。本記事は効率的で快適な環境構築のヒントとなれば幸いである。定期的な情報収集とコミュニティ交流も推奨されている。
