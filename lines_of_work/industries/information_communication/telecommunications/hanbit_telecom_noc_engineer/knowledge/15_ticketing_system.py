title = "ITSM 티켓·로그 관리"

content = """
- 사용 시스템: Jira Service Management(JSM), ITSM 표준 ITIL v4 프로세스(Incident·Problem·Change·Request·Knowledge) 적용.
- INC 티켓 필드: ①티켓 번호(HBT-INC-YYYYMMDD-NNNN), ②접수 시각, ③증상, ④영향 범위, ⑤Severity, ⑥담당자, ⑦현재 단계, ⑧SLA 잔여 시각, ⑨근본 원인, ⑩종결 시각.
- 티켓 상태: New → In Progress → Investigating → Mitigated → Resolved → Closed, 인하는 Severity Drop 사유 코멘트 필수.
- 코멘트 작성 규칙: 5W1H, 시각은 ISO 8601(KST, +09:00), 첨부 파일은 1건당 20MB 이하, 로그·스크린샷은 zip 1개로 묶어 첨부.
- 티켓 보관: 종결 후 3년(중요 INC 5년), KB(Knowledge Base) 후보는 종결 후 자동 추천, 1개월 내 승인 시 KB 등록.
- 티켓 간 링크: 부모-자식(병합·분리), 참조(관련), 복제(중복) 3종, 동일 INC로 병합 시 자식은 Closed, 부모는 Resolved 유지.
"""  # noqa: E501

version = "0.0.1"
