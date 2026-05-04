以下のように改造したい。
- kiro-loop.yaml の kiro_options に no_interactive を追加し true の場合 --no-interactive を kiro-cli のオプションに追加する
	- デフォルトは false
- kiro-loop.yaml にセッションクリーンアップ設定を追加する
	- clean_session_window に指定した値（回数）間隔で定期処理実行前にセッションクリーンアップ処理を行う
	- デフォルトは1 (毎回の定期処理実行前にクリーンアップする)
	- 0以下の値を指定するとクリーンアップ処理を行わない
- セッションクリーンアップを定期実行処理に組み込む。以下の手順を実行。
	1. セッション作成日時と現在日時からクローズするか判定する
	2. クローズすると判定された場合、以下の処理を実行する
		1. no_interactive=false の場合、以下の処理を行う
			1. `/chat save .kiro/{name}.json` コマンドを対象 kiro (tmux) へ送る
			2. `/quit` コマンドを対象 kiro (tmux) へ送る
			3. `{name}.json` からセッションIDを抽出する
				- kiro-cli v1 の場合 `metadata` > `session_id` がキーになる
				- kiro-cli v2 の場合 `conversation_id` がキーになる
			4. `kiro-cli chat --delete-session <SESSION_ID>` で kiro セッションを削除
		2. `tmux kill-session {session_name}` で tmux セッションを削除
		3. `tmux new-session -s {session_name} -c kiro-cli chat <起動時の引数> >` で tmux/kiro セッションを新規作成
	3. 定期プロンプトを送る
 - プロセス終了シグナルのキャッチロジックを異常時に限定する
	 - プロセス終了シグナルをキャッチして tmux/kiro-cli セッションを自動起動する。具体的には、強制的に残存するセッションを削除して、新たにtmux/kiro-cli セッションを作成する。ただし、以下の場合は発動しない。
		 - コントロールペインにユーザーが quit と打った時
		 - no_interactive=trueでkiro-cliが自分でプロセスを終了する時
		 - セッションクリーンアップ処理によってセッションが終了した時