"""Yield and reliability correlation (ko)."""

title = "수율과 신뢰성 상관"

content = """
일부 수율 이슈는 초기 테스트에서 pass하더라도 신뢰성(수명, TDDB, EM 등)에
잠재적 영향을 미칩니다.

**위험 유형:** marginal oxide, weak junction, 금속 void 등. 고객 필드에서
초기 고장으로 이어질 수 있습니다.

**대응:** burn-in, ELFR, 특정 테스트 추가로 위험을 스크리닝. 또는 공정
개선으로 근본적으로 제거합니다.

**수율 공학:** 수율-신뢰성 상관 데이터를 모니터링하고, 잠재 이슈를
신뢰성 팀에 전달합니다.
"""

version = "0.0.1"
