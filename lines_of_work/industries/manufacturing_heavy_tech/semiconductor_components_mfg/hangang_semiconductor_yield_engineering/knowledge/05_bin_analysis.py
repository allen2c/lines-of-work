"""Bin and fail-mode analysis (ko)."""

title = "빈 분석 및 실패 모드"

content = """
빈(bin)은 전기 테스트 결과에 따라 die를 분류한 카테고리입니다. 빈별 수율 분포는
실패 메커니즘 추정에 핵심입니다.

**빈 정의:** speed bin, power bin, functional fail bin 등. 각 bin은 특정 성능 또는
결함 유형과 연결됩니다.

**실패 모드:** 특정 테스트 항목 fail이 어떤 구조·공정과 연관되는지 매핑합니다.
예: scan fail → 로직 결함, leakage fail → junction/ gate oxide 이슈.

**활용:** 빈 분포 변화로 새 결함 메커니즘 또는 공정 드리프트를 추정하고, FA
샘플링 우선순위를 정합니다.
"""

version = "0.0.1"
