title = "혼합액 고형분(MLSS) 관리"

content = """
- 측정: 자동 MLSS 센서(광산란) 10분 주기, 수동 그라비메트릭 주 2회 검증
- 목표 범위: 3,000~4,500 mg/L, 편차 ±10 % 허용
- 조정 수단: 슬러지 반송 펌프 유량(Qr) 조절, 슬러지 배출량(WAS) 증감
- 반송 비율 계산: Qr = (MLSS_target / MLSS_actual) × Q_in × 0.4
- 과다 MLSS 시: 반송 비율 5 % 감소, WAS 펌프 10 % 증가
- 부족 MLSS 시: 반송 비율 5 % 증가, WAS 펌프 10 % 감소
- 기록: 일일 MLSS 평균, 최대/최소, 조정 이력 SCADA 태그 MLSS_AVG, MLSS_ADJ
"""  # noqa: E501

version = "0.0.1"
