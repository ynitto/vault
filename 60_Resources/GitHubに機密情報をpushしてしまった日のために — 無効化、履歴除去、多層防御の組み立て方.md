---
title: "GitHubに機密情報をpushしてしまった日のために — 無効化、履歴除去、多層防御の組み立て方"
source: "https://zenn.dev/okamyuji/articles/github-secret-removal-multi-layer-defense"
author:
published: 2026-05-04
created: 2026-05-07
description:
tags:
  - "clippings"
---
### 記事の要約
GitHubに機密情報（APIキー、秘密鍵、個人情報など）を誤ってpushしてしまった際の、無効化・履歴削除・多層防御の方法を解説した実践的ガイド。

### 要点まとめ
- **優先順位は「無効化」から**
    - 認証情報であれば、Git履歴削除の前にまず無効化（revoke）・再生成（rotate）を行う。
- **履歴削除の判断基準**
    - 認証情報は無効化で済む場合があるが、個人情報や秘密鍵など「残存自体がリスク」なデータはGit履歴およびGitHub上のキャッシュ等まで含めた完全削除が必要。
- **多層防御のレイヤー**
    - **コミット前:** `pre-commit` (Gitleaks等) で開発者の手元でブロック。
    - **push時:** `GitHub Push Protection` や `GHES pre-receive hook` でリモートへの流入を阻止。
    - **CI/定期スキャン:** GitHub Actions等で継続的な監視を実施。
- **履歴削除の手順**
    - `git-filter-repo` が現在の推奨ツール。
    - 履歴削除後は `git push --force --mirror` を実施し、GitHub Supportへの連絡や管理部門によるキャッシュ削除（GitHub側の残存除去）を依頼する。
- **再汚染の防止**
    - 履歴改変後は、全開発者が古いローカルリポジトリを破棄し、再クローンすることを徹底する。
