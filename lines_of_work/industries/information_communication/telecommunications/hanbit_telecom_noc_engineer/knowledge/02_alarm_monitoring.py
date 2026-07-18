title = "알람 감시 체계와 임계치"

content = """
- 주요 NMS는 코어(NetAct), 전송(OTDR·DWDM Manager), IP(CA Spectrum·Cisco Prime), IDC(DCIM), 음성(IMS EMS)의 5개 도메인으로 분리 운용하며, 단일 통합 뷰는 NMS Aggregator를 통해 60초 주기로 수집한다.
- 알람 등급은 Critical(적색, 1분 내 인지), Major(주황, 5분), Minor(황색, 30분), Warning(청색, 4시간), Info(회색, 일간 리포트)의 5단계로 분류한다.
- 반복 알람(5분 내 동일 자원·동일 코드 3건 이상)은 자동으로 그룹핑되어 카운트만 증가하며, 동일 Root Cause로 통합 처리한다.
- "알람 폭주" 기준은 1분 내 50건 또는 10분 내 200건이며, 이 경우 NMS 상관분석 룰 가동 후 동일 사이트·동일 카드·동일 링크 단위로 클러스터링한다.
- 야간·주말에도 Critical 알람은 음성 호출(PagerDuty + ARS + SMS 3중) 발송, L1·L2·팀장 동시 착신 후 미수신 3분 재시도한다.
"""  # noqa: E501

version = "0.0.1"
