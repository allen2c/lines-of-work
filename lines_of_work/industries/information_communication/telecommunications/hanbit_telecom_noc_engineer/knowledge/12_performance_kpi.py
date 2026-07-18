title = "성능 관리 핵심 지표"

content = """
- 일일 KPI 수집·산출: ①가입자 수(활성 4G/5G 분리), ②트래픽(DL/UL GB), ③셀 가용률, ④핸드오버 성공율, ⑤RACH 성공율, ⑥PRB 활용률, ⑦E-RAB setup success rate, ⑧PSM·eDRX 활성 비율(IoT).
- 코어 KPI: ①Attach/PDU Session 성공율, ②TAU/RAU 성공율, ③S1/N2 setup 시 지연, ④Paging 성공율, ⑤SCTP association 상태, ⑥CPU/Memory/Disk 활용률.
- 음성 KPI: ①호 성공율, ②호 손실율, ③MOS, ④SRVCC 성공율, ⑤VoLTE 호 처리 지연.
- 전송 KPI: ①OSNR, ②광 파워, ③Bit Error Rate, ④링 가용률, ⑤보호 절체 시간, ⑥트래픽 활용률(70% 이상 시 증설 검토).
- KPI는 5분 주기 수집·1시간 평균 산출, 임계치 초과 시 자동 알람, 일일 09시 KPI 리포트 자동 메일·슬랙 발송.
"""  # noqa: E501

version = "0.0.1"
