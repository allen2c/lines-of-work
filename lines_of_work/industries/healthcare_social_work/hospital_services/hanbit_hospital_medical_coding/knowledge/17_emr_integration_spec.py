title = "EMR 연동 인터페이스 사양"

content = """
- 프로토콜: HL7‑FHIR R4, RESTful API, OAuth2.0 Bearer 토큰 인증  
- 주요 리소스: Patient, Encounter, Condition(진단), Procedure(처치), Claim(청구)  
- 동기화 주기: 실시간(이벤트 드리븐) + 일일 배치(02:30) 전체 동기화  
- 오류 처리: 5xx 응답 시 5분 간격 3회 재시도, 지속 시 알림·수동 동기화 버튼 제공  
- 버전 관리: API 버전 헤더(v1, v2) 사용, 하위 호환 12개월 보장
"""  # noqa: E501

version = "0.0.1"
