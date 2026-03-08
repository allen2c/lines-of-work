"""Inline-to-electrical correlation (ko)."""

title = "인라인-전기 테스트 상관"

content = """
인라인 검사에서 발견된 결함과 전기 테스트 fail 간의 대응 관계를 분석하여, 어떤
결함이 치명적인지 파악합니다.

**방법:** Defect-to-electrical fail (D2E) 매핑, 샘플 기반 상관 분석. 같은 die에서
결함 유무와 pass/fail을 비교합니다.

**활용:** 검사 감도 설정, 검사 샘플링 전략, 수율 예측 모델 개선. kill ratio 등
지표로 정량화합니다.

**한계:** 검출 한계 이하 결함, 비결함 수율 손실은 상관에 포함되지 않습니다.
"""

version = "0.0.1"
