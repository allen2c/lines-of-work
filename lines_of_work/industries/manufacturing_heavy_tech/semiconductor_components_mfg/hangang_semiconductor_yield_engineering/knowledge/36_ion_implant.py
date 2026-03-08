"""Ion implant and electrical param correlation (ko)."""

title = "이온 주입 및 전기 파라미터"

content = """
이온 주입은 도핑 농도와 프로파일을 결정하며, Vt, Rs, junction 특성에
직접 영향을 미칩니다.

**파라미터:** dose, energy, tilt. 이탈 시 Vt shift, leakage, punch-through
등이 발생합니다.

**수율 상관:** 특정 leakage bin, functional fail이 implant 단계와 연관되는지
분석합니다. Rs, junction leakage 인라인 데이터와 테스트 수율을 비교합니다.

**수율 공학:** implant 후 Rs, spreading resistance, 수율 트렌드를 모니터링합니다.
"""

version = "0.0.1"
