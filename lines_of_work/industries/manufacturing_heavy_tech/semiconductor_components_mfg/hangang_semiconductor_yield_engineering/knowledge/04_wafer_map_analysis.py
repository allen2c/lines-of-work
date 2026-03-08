"""Wafer map analysis (ko)."""

title = "웨이퍼맵 분석"

content = """
웨이퍼맵은 각 die의 pass/fail 또는 bin 정보를 2차원 공간에 표시한 것입니다.
수율 손실의 공간적 패턴을 파악하는 핵심 도구입니다.

**패턴 유형:** 에지 결함(edge fail), 클러스터 결함, 랜덤 결함, 링/도넛 패턴, 스크래치
등. 패턴별로 원인이 다릅니다.

**분석 절차:** 수율 급락 시 wafer map을 먼저 검토하여 패턴을 분류하고, 해당 패턴과
연관된 공정 단계·장비를 가설로 설정한 후 데이터로 검증합니다.

**도구:** KLARF, wafer map 시각화 소프트웨어, defect-to electrical fail 매핑 등.
"""

version = "0.0.1"
