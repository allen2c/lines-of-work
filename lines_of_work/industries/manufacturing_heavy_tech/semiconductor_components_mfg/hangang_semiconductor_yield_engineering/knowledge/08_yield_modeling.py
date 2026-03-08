"""Yield modeling fundamentals (ko)."""

title = "수율 모델링 기초"

content = """
수율 모델링은 수율을 결함 밀도, die 면적, 공정 단계 수 등과 연결하여 예측하고
비용·목표 수율을 산정하는 방법입니다.

**Murphy 모델:** 결함 밀도가 균일할 때의 수율. 수학적 형태가 단순해 개략 추정에 사용됩니다.

**Poisson 모델:** 랜덤 결함에 기반. Y = exp(-A·D) (A=die 면적, D=결함 밀도).
작은 die 또는 낮은 수율 구간에서 합리적입니다.

**혼합 모델:** systematic과 random 수율 손실을 분리하여 모델링. 실제 수율 분석에
가깝습니다.
"""

version = "0.0.1"
