---
type: gitlab-issue
id: {{iid}}
project: {{project_id}}
title: "{{title}}"
state: {{state}}
author: {{author.username}}
assignees: [{{#each assignees}}{{username}}{{#unless @last}}, {{/unless}}{{/each}}]
labels: [{{#each labels}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}]
milestone: {{milestone.title}}
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: {{updated_at}}
due: {{due_date}}
web_url: {{web_url}}
tags:
  - task
---
```button
name 📝 Post Issue
type command
action Shell commands: Post Issue
color blue
```
```button
name 🤖 Send to Kiro
type command
action Shell commands: Send to Kiro
color blue
```
# {タスク名}

## 背景・目的
<!-- なぜこのタスクが必要か、どんな問題を解決するか -->

## やること（ステップ）

- [ ] ステップ1
- [ ] ステップ2
- [ ] ステップ3

## リポジトリ
```git-manager
show: all
```

## 完了条件
<!-- どうなれば完了とみなすか -->
- [ ] 

## 参考情報・出典
<!-- 関連する 60_Resources/ のリンクや外部情報 -->
- [[60_Resources/YYYY-MM-DD-ファイル名]]

## メモ・懸念点
<!-- 特記事項 -->