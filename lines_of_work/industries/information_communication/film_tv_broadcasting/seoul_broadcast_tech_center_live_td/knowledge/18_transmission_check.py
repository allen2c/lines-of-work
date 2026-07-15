title = "송출 확인 및 모니터링"

content = """
- **송출 경로**: 메인 인코더 → ASI(270Mbps) 또는 IP(TS/UDP) → 위성/케이블/IPTV. 백업 경로 동시 활성화.
- **송출 품질**: 비트레이트 10-20Mbps(HD), 30-50Mbps(4K). CBR(Constant Bit Rate) 유지.
- **모니터링 도구**: Evertz XR, Tektronix Sentry로 TS(Transport Stream) 분석. PCR 지터 500ns 이하, PAT/PMT 주기 100ms 이하.
- **수신 확인**: 방송 시작 후 5분 이내에 주요 수신처(케이블 헤드엔드, 위성 수신소)에서 정상 수신 확인 전화.
- **송출 중단 시**: 10초 이내에 백업 인코더로 전환. 전환 후 30초 이내에 수신처 재확인.
"""

version = "0.0.1"
