---
id: "{{id}}"
iid: "{{iid}}"
title: "{{{title}}}"
webUrl: "{{web_url}}"
project: "{{references.full}}"
state: "{{state}}"
sourceBranch: "{{source_branch}}"
targetBranch: "{{target_branch}}"
draft: "{{draft}}"
author: "{{author.name}}"
related_task: ""
{{#if labels.length}}
labels: [{{#each labels}}"{{this}}"{{#unless @last}}, {{/unless}}{{/each}}]
{{/if}}
{{#if reviewers.length}}
reviewers: [{{#each reviewers}}"{{name}}"{{#unless @last}}, {{/unless}}{{/each}}]
{{/if}}
{{#if assignees.length}}
assignees: [{{#each assignees}}"{{name}}"{{#unless @last}}, {{/unless}}{{/each}}]
{{/if}}
tags: [merge-request]
---

# !{{iid}} {{{title}}}

| 項目 | 値 |
|---|---|
| ブランチ | `{{source_branch}}` → `{{target_branch}}` |
| 作成者 | {{author.name}} |
| 状態 | {{state}}{{#if draft}} (Draft){{/if}} |
| プロジェクト | {{references.full}} |

{{{description}}}

[GitLab で見る]({{web_url}})

{{#if activities.length}}
## アクティビティ（状態変化）

| 日時 | ユーザー | 状態 |
|---|---|---|
{{#each activities}}
| {{created_at}} | {{user.name}} | `{{state}}` |
{{/each}}
{{/if}}

{{#if discussions.length}}
## コード指摘（Diff ノート）

{{#each discussions}}
{{#each notes}}
{{#unless system}}
{{#if position}}
---
**📍 [`{{position.new_path}}`{{#if position.new_line}} L{{position.new_line}}{{/if}}{{#unless position.new_line}}{{#if position.old_line}} L{{position.old_line}}（削除行）{{/if}}{{/unless}}]({{permalink}})**
{{#if resolved}} · ✅ 解決済み{{/if}}

> **{{author.name}}** · _{{created_at}}_
>
> {{{body}}}

{{/if}}
{{/unless}}
{{/each}}
{{/each}}

## ディスカッション

{{#each discussions}}
{{#each notes}}
{{#unless system}}
{{#unless position}}
**{{author.name}}** · _{{created_at}}_

{{{body}}}

{{/unless}}
{{/unless}}
{{/each}}
{{/each}}
{{/if}}
