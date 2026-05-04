---
title: "Holidays JP API (日本の祝日API)"
source: "https://holidays-jp.github.io/"
author:
published:
created: 2026-04-30
description: "Holidays JP API は、日本の祝日一覧をJSONで返却するAPIです (CSV形式もサポート)"
tags:
  - "clippings"
---
### 日本の祝日API概要
日本の国民の祝日データをJSONまたはCSV形式で提供するオープンデータAPIです。Googleカレンダーの情報を基に生成されており、過去・現在・未来のデータを取得可能です。

### 主な特徴
- **形式**: JSON および CSV
- **ライセンス**: MIT
- **対象期間**: 去年・今年・来年のデータ

### APIの種類
- **日付ベース (date)**: 日付（YYYY-MM-DD）をキーに祝日名を取得
- **UNIX時間ベース (datetime)**: UNIXタイムスタンプをキーに祝日名を取得
- **年別指定**: URLに西暦4桁を指定することで、特定年のみ抽出可能
