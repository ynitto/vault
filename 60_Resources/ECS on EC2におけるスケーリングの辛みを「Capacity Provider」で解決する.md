---
title: "ECS on EC2におけるスケーリングの辛みを「Capacity Provider」で解決する"
source: "https://dev.classmethod.jp/articles/ecs_on_ec2_capacity_provider/"
author:
  - "[[島川寿希也]]"
published: 2020-03-31
created: 2026-05-01
description:
tags:
  - "clippings"
---
### 記事の要約
ECS on EC2において、これまで手動設定が必要だったEC2のスケーリングを、ECSの「Capacity Provider」および「Cluster Auto Scaling (CAS)」を利用することで自動化・効率化する手法の検証記事。

### 要点まとめ
- **ECS on EC2の課題**
  - タスクとEC2の両方のスケーリングを管理する必要があり、運用難易度が高かった。
- **解決策：Capacity ProviderとCAS**
  - タスクのスケーリングのみ意識すれば、連動してEC2も自動で増減する。
  - AutoScalingGroupの「希望するキャパシティ」が自動調整される。
- **検証結果**
  - **スケールアウト**: EC2の追加を含め約3分で完了。
  - **スケールイン**: タスク停止後、EC2が削除されるまで約30分かかる（慎重な運用）。
- **結論**
  - 運用コストの大幅な削減が見込めるため、ECS on EC2利用者は導入を強く推奨。ただし、スケーリングポリシーの挙動を事前に検証することが重要。