"""Critical dimension control (ko)."""

title = "임계 치수(CD) 제어"

content = """
CD(Critical Dimension)는 회로 동작에 직결되는 패턴의 핵심 치수입니다. 리소그래피와
식각 공정에서 제어됩니다.

**측정:** CD-SEM으로 선폭, 공간폭 등을 측정합니다. 샘플링 위치와 수가 대표성을
보장해야 합니다.

**수율 영향:** CD 편차가 과대하면 leakage, 속도 저하; 과소하면 short, open 등으로
이어질 수 있습니다.

**제어 전략:** 공정 창(process window) 내에서 타깃과 허용 범위를 정의하고, OPC 및
공정 파라미터 튜닝으로 안정성을 확보합니다.
"""

version = "0.0.1"
