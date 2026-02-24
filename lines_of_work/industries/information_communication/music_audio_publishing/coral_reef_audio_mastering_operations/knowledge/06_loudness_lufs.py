title = "라우드니스(LUFS) 및 정규화"

content = """
**LUFS(Loudness Units Full Scale)**
청취자가 인지하는 음량을 나타내는 표준. 스트리밍 서비스는 integrated LUFS를 기준으로 자동 정규화를 적용합니다.

**Integrated LUFS**
전체 트랙 또는 앨범의 평균 라우드니스. -14 LUFS가 많은 서비스의 권장치입니다.

**Short-term 및 Momentary LUFS**
짧은 구간의 라우드니스를 측정. 펀치감·다이나믹스 평가에 사용됩니다.

**True Peak(dBTP)**
인터샘플 피크를 포함한 최대 레벨. 과도한 트루 피크는 디지털 클리핑을 유발하므로 -1dBTP 이하 유지가 권장됩니다.

**운영 시**
라우드니스 분석 도구(예: iZotope RX, Nugen)로 마스터 완성본의 LUFS·dBTP를 측정하고, 플랫폼 사양에
부합하는지 확인합니다. 고객이 특정 라우드니스를 요청할 경우 해당 값으로 검증합니다.
"""

version = "0.0.1"
