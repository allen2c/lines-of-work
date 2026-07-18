title = "5G/4G 코어 운영 포인트"

content = """
- 5G NSA 옵션 3x는 4G EPC 기반이며, 5G NR은 데이터 트래픽 전용으로 부착, 음성은 VoLTE IMS 경로 그대로 사용. 장애 시 NR Cell 자동 비활성화, EPC만으로 서비스 유지 모드 전환.
- 5G SA는 AMF 장애 시 1차 AMF에서 2차 AMF로 N2 인터페이스 핸드오버가 자동으로 진행되며, 60초 내 미완료 시 가입자 단말 5G attach 실패가 시작된다.
- MME·AMF의 CPU 70% 이상 5분 지속, 메모리 80% 이상, S1-U/N3 인터페이스 throughput 평소 대비 30% 이상 급증/급감, SCTP association down, Diameter/Rx 세션 폭주 등을 주요 모니터링 지표로 관리한다.
- 코어 노드 계획 작업은 Maintenance Window 내(평일 22:00~06:00, 주말 00:00~06:00)에만 허용, 핵심 노드(중앙 MME·AMF·UPF)는 1개 노드 단위 작업, 동시 2개 이상 작업 금지.
- 코어 장애 시 가상 머신(VM) 단위 Live Migration, 컨테이너(Pod) 단위 재기동 자동화, 복구 시간은 VM 5분, Pod 1분 목표.
"""  # noqa: E501

version = "0.0.1"
