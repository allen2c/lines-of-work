"""Statistical process control (ko)."""

title = "통계적 공정 관리(SPC)"

content = """
SPC는 공정 파라미터가 관리 한계 내에 있는지 통계적으로 감시하여, 이상을 조기에
감지하는 방법입니다.

**관리 한계:** UCL(상한), LCL(하한)은 보통 ±3σ로 설정. 2σ 또는 Cpk 기반 설정도
사용됩니다.

**규칙:** Western Electric 규칙 등으로 연속 이탈, 트렌드, 런 등 이상 패턴을 탐지합니다.

**대응:** OOC(Out of Control) 발생 시 lot 홀드, 공정 조정, 원인 조사를 수행합니다.
수율 공학은 SPC 이탈과 수율 변동의 상관 분석을 담당합니다.
"""

version = "0.0.1"
