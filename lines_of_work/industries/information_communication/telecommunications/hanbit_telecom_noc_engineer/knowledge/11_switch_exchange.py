title = "교환기/IMS 운영"

content = """
- 회선교환(CS) 노드는 5G SA 전환에 따라 2025년부터 단계적 퇴역, 2026년 말 완전 종료 예정, 잔여 회선은 VoLTE IMS로 라우팅.
- IMS 코어(CSCF·HSS·S-CSCF·P-CSCF·I-CSCF·ATCF/ATGW)는 중앙 2개 IDC에 이중화, 1+1 Active-Standby, DNS·ENUM·BGCF 3대 이중화.
- VoLTE 호 처리: INVITE → S-CSCF → ATCF/ATGW(media) → MMTel AS, 호 설정 지연 ≤ 4초, 호 손실율 ≤ 0.1%, MOS ≥ 3.8 유지.
- 호 라우팅 폭주(예: 지진·재난) 대비 P-CSCF 부하분산, 트래픽 우회 100% 자동화, 1분 내 평소의 3배까지 흡수 가능.
- IMS 노드 작업은 Change Window 내, 사용자 영향 예상 시 CS 본부에 사전 공지(최소 24시간 전), 긴급 작업은 4시간 사후 사인 필수.
"""  # noqa: E501

version = "0.0.1"
