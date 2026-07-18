title = "작업 승인(CR) 절차"

content = """
- 모든 망 변경 작업은 사전 CR 등록 필수, 등록 기한: 표준 작업 5영업일 전, 고위험 작업 10영업일 전, 긴급 작업은 4시간 사후 사인 + 48시간 사후 검토.
- CR 필수 항목: ①작업명·목적, ②영향 범위(사이트·서비스·가입자), ③작업 시간(시작-종료), ④Cut-over Plan(단계별 명령어·판단 기준), ⑤Backout Plan(롤백 절차·완료 시각), ⑥영향 가입자 수, ⑦위험도(High/Medium/Low), ⑧승인자(Change Manager·CAB).
- 고위험 작업(High): 코어 노드·전송 본부 링·국제 GW·IDC ToR 작업, Change Advisory Board(CAB) 주간 회의(매주 화 14:00) 승인 필요, 실 작업 전 Pre-CAB(전일 17:00) 1회 더 점검.
- 작업 중 NOC는 ①실시간 알람 감시, ②KPI 1분 단위 확인, ③복구 지연·계획 외 알람 발생 시 작업 중단 권고, ④롤백 명령 권한 보유.
- 작업 완료 후 Post-Implementation Review(PIR) 7일 내 작성, 5분 이상 지연·가입자 영향·예상 외 알람 발생 시 자동 RCA 트리거.
"""  # noqa: E501

version = "0.0.1"
