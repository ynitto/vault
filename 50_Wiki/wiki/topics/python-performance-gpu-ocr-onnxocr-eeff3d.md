---
title: "GPUなしローカルでも高速・高精度なOCRができるOnnxOCRが凄い"
type: "topic"
tags:
  - "python"
  - "performance"
  - "resource-ingest"
created: "2026-05-02"
updated: "2026-05-02"
sources:
  - "../60_Resources/GPUなしローカルでも高速・高精度なOCRができるOnnxOCRが凄い.md"
summary: "本記事は、クラウド利用や低スペックPCなどの制約がある環境下でも、高速かつ高精度なOCR処理を実現できるライブラリ「OnnxOCR」を紹介・検証しています。"
---

# GPUなしローカルでも高速・高精度なOCRができるOnnxOCRが凄い

## 概要

本記事は、クラウド利用や低スペックPCなどの制約がある環境下でも、高速かつ高精度なOCR処理を実現できるライブラリ「OnnxOCR」を紹介・検証しています。

*発行: 2025-09-28 / [[python-performance-gpu-ocr-onnxocr-eeff3d]]*

## 主要なトピック

- [[python]]
- [[performance]]

## 詳細

- 本記事は、クラウド利用や低スペックPCなどの制約がある環境下でも、高速かつ高精度なOCR処理を実現できるライブラリ「OnnxOCR」を紹介・検証しています。
- OnnxOCRの主な特徴
- **概要**: PaddleOCRをベースにした軽量かつ高速なOCRエンジン。
- **高速性**: 深層学習フレームワーク（PaddlePaddle）を介さずONNX形式で直接推論を行うため、従来のフレームワーク使用時よりも約5倍高速。
- **商用利用**: Apacheライセンスのため、商用利用が可能。
- **手軽さ**: Python（`pip install onnxocr`）で簡単に導入でき、モデルのダウンロードも自動で行われる。
- 検証結果のポイント
- **比較対象**: EasyOCR、PaddleOCR、OnnxOCRの3種でCPU推論による比較を実施。
- **パフォーマンス**:

*発行: 2025-09-28 / [[python-performance-gpu-ocr-onnxocr-eeff3d]]*

## 関連テーマ

- [[python]]
- [[performance]]

## 出典

- `../60_Resources/GPUなしローカルでも高速・高精度なOCRができるOnnxOCRが凄い.md`
- https://zenn.dev/harumikun/articles/fb9c435acf4070
