---
task_id: {{key}}
title: {{{summary}}}
jira_id: {{id}}
status: {{status}}
statusCategory: {{statusCategory}}
priority: {{priority}}
issueType: {{issuetype}}
assignee: {{assignee}}
reporter: {{reporter}}
dueDate: {{duedate}}
created: {{created}}
updated: {{updated}}
urgency: 中
effort: M
{{#if labels.length}}
labels: [task, jira, {{#each labels}}"{{this}}"{{#unless @last}}, {{/unless}}{{/each}}]
{{else}}
labels: [task, jira]
{{/if}}
{{#if sprint}}
sprint: "{{sprint}}"
{{/if}}
{{#if storyPoints}}
storyPoints: {{storyPoints}}
{{/if}}
{{#if parentKey}}
parent: "{{parentKey}}"
{{/if}}
webUrl: {{webUrl}}
source_daily:
---
```button
name 🤵 Task Assistant
type command
action Shell commands: Execute: Breakdown Task
color blue
```
```button
name 📝 Post Issue
type command
action Shell commands: Execute: Post Issue
color blue
```
```button
name 🤖 Send to Kiro
type command
action Shell commands: Execute: Send to Kiro
color blue
```
# {{{summary}}}

## 説明
{{{description}}}

## 条件
### 前提条件

### 制約条件

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
- [View in Jira]({{webUrl}})

{{#if subtasks.length}}
### サブタスク

{{#each subtasks}}
- **[{{key}}]** {{{fields.summary}}} — _{{fields.status.name}}_
{{/each}}
{{/if}}

## メモ・懸念点
{{#if comments.length}}
### コメント（Jiraより）

{{#each comments}}
**{{author}}** _{{created}}_

> {{{bodyText}}}

{{/each}}
{{/if}}
